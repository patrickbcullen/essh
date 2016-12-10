from os import environ
from os.path import abspath, dirname, join, isfile
import logging
import boto3
import botocore
from time import sleep
import time, datetime
from retrying import retry
from pprint import pprint
from models import Instance
from os import environ
from essh.exceptions import ESSHException
import re

class EC2:
    def __init__(self, ec2_client=None):
        logging.basicConfig(level=logging.ERROR)
        self.logger = logging.getLogger(__name__)
        self.ec2 = ec2_client or self._get_ec2_client()
        self.array_regex = re.compile('\[([0-9]+)\]$')

    def _require_env_var(self, key):
        if key not in environ:
            raise ESSHException('Missing %s environment variable' % key)
        return environ[key]

    def _get_ec2_client(self):
        return boto3.client('ec2', aws_access_key_id=self._require_env_var('AWS_ACCESS_KEY_ID'),
                            aws_secret_access_key=self._require_env_var('AWS_SECRET_ACCESS_KEY'),
                            region_name=environ.get('AWS_REGION', 'us-east-1'))

    def find_by_name(self, name):
        name, index = self._extra_index(name)

        filters = [
            {"Name": "instance-state-name", "Values": ["running"]},
            {"Name": "tag:Name", "Values": [name]}
        ]

        return self._find(filters, index)

    def _extra_index(self, name):
        index = 0
        match = re.findall(self.array_regex, name)
        if len(match) > 0:
            name = name.split("[", 1)[0]
            index = int(match[0][0])

        return name, index

    def find_by_id(self, id):
        filters = [
            {"Name": "instance-state-name", "Values": ["running"]},
            {"Name": "instance-id", "Values": [id]}
        ]
        return self._find(filters)

    def find_by_ip(self, private_ip):
        filters = [
            {"Name": "instance-state-name", "Values": ["running"]},
            {"Name": "private-ip-address", "Values": [private_ip]}
        ]
        return self._find(filters)

    def _find(self, filters, index=0):
        instance_id, keypair, private_ip = self._find_by_index(filters, index)
        if keypair and instance_id and private_ip:
            return Instance(instance_id, private_ip, keypair)
        else:
            raise ESSHException('Could not find instance with ip address %s' % private_ip)

    def _find_by_index(self, filters, index=0):
        instance_id = None
        keypair = None
        private_ip = None

        instances = self._ec2_describe_instances(Filters=filters)
        for reservation in instances.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                if 'InstanceId' in instance:
                    instance_id = instance['InstanceId']
                    keypair = instance['KeyName']
                    private_ip = instance['PrivateIpAddress']
                    if index <= 0:
                        return instance_id, keypair, private_ip
                    index -= 1

        return instance_id, keypair, private_ip

    def _is_retryable_exception(exception):
        return not isinstance(exception, botocore.exceptions.ClientError)

    @retry(retry_on_exception=_is_retryable_exception, stop_max_delay=10000, wait_exponential_multiplier=500, wait_exponential_max=2000)
    def _ec2_describe_instances(self, **kwargs):
        return self.ec2.describe_instances(**kwargs)
