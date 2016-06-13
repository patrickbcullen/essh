from essh.ec2.api import EC2
from essh.exceptions import ESSHException
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
            return self.api.find_by_name(target)
