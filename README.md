# essh
Enhanced ssh command line for EC2 that can find an instance by the instance id, instance name tag, or private IP address. It even supports indexing when multiple instances share the same name (i.e. auto-scaling groups).

## Install
```
pip install essh
```

## Usage
```
# To ssh by instance id
essh <instance id>
# To run a command over ssh on instance id
essh <instance id> ls /tmp
# To ssh by private ip
essh <private ip>
# To ssh to the first instance with this name tag
essh <tag name>
# To ssh to the second instance with this name tag
essh <tag name>[1] 
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
