from subprocess import call

class SSHController:
    def __init__(self, keypair_dir, keypair_name, keypair_extension, host):
        self.keypair = '%s/%s.%s' % (keypair_dir, keypair_name, keypair_extension)
        self.host = host

    def command(self):
        return "ssh -i %s %s" % (self.keypair, self.host)

    def ssh(self):
        command = self.command()
        call(command, shell=True)

