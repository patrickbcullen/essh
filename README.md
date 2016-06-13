# ec2ssh
EC2 ssh helper command that can find an instance by the instance id, instance name tag, or private IP address. It looks up the keypair to use from the EC2 console and uses the default keypair folder `~/.ssh` and default keypair of extension of `.pem`.

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
### How do you change the default keypair folder or extension?
Set the `--keypair-dir` and/or `--keypair-extension` options on the command line.
