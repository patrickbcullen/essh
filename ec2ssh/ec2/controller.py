from ec2ssh.ec2.api import EC2
from ec2ssh.exceptions import EC2SSHException
import re

class EC2Controller:
    def __init__(self):
        self.instance_id_regex = re.compile('^i-')
        self.ip_regex = re.compile('^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
        self.api = EC2()

    def find(self, target):
        if re.search(self.instance_id_regex, target) is not None:
            return self.api.find_by_id(target)
        elif re.search(self.ip_regex, target) is not None:
            return self.api.find_by_ip(target)
        else:
            raise EC2SSHException('unknown target %s' % target)
