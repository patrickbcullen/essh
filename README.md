# ec2ssh
EC2 ssh helper command that can find an instance by the instance id, instance Name tag, or private IP address. It looks up the keypair to use from the EC2 console and assumes that the keypair PEM files are stored in an .ssh folder in your home directory.

## Usage
```
ec2ssh <instance id>
ec2ssh <private ip>
ec2ssh <tag name>
```

## FAQ
### How do you specify the username to use on the ssh command?
Add the following to your ~/.ssh/config file:
```
User centos
```
### How do you ignore IP address changes?
Add the following to your ~/.ssh/config file:
```
CheckHostIP no
```
