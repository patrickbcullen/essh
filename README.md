# essh
Enhanced ssh command line for EC2 that can find an instance by the instance id, instance name tag, or private IP address. 

## Install
```
pip install essh
```

## Usage
```
essh <instance id>
essh <private ip>
essh <tag name>
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
StrictHostKeyChecking no
```
### How do you change the default keypair directory or extension?
The default keypair directory is `~/.ssh` and default keypair extension is `.pem`. To change either of these set the `--keypair-dir` and/or `--keypair-extension` options on the command line.
