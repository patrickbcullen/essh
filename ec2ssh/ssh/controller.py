from subprocess import call

class SSHController:
    def __init__(self, keypair, ip):
        self.keypair = keypair
        self.ip = ip

    def command(self):
        return "ssh -o StrictHostKeyChecking=no -o GlobalKnownHostsFile=/dev/null -o UserKnownHostsFile=/dev/null -i ~/.ssh/%s.pem %s" % (self.keypair, self.ip)

    def ssh(self):
        command = self.command()
        call(command, shell=True)

