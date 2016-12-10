from subprocess import call
import os

class SSHController:
    def __init__(self, keypair_dir, keypair_name, keypair_extension, host):
        self.keypair = '%s/%s.%s' % (keypair_dir, keypair_name, keypair_extension)
        self.host = host
        self.alternate_usernames = ['centos', 'ec2-user', 'ubuntu', 'admin', 'bitnami', 'root']
        self.devnull = open(os.devnull, 'w')

    def ssh(self, command=''):
        return_code = self._ssh(command)
        if return_code == 255:
            for username in self.alternate_usernames:
                return_code = self._ssh(command, username)
                if return_code != 255:
                    return



    def _ssh(self, command, username=None):
        ssh_cmd = "ssh -q -i %s " % self.keypair
        if username:
            ssh_cmd += "%s@" % username
        ssh_cmd += "%s%s" % (self.host, command)

        return call(ssh_cmd, shell=True)
