from subprocess import call

class SSHController:
    def __init__(self, keypair_dir, keypair_name, keypair_extension, host):
        self.keypair = '%s/%s.%s' % (keypair_dir, keypair_name, keypair_extension)
        self.host = host

    def ssh(self, command=''):
        ssh_cmd = "ssh -i %s %s%s" % (self.keypair, self.host, command)
        call(ssh_cmd, shell=True)

