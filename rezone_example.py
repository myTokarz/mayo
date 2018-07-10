'''
Simple script to rezone a host.  

For example, the following desired configuration is pushed to the switch

config t
zone name ropstg014a vsan 4
no member pwwn 50:06:0e:80:06:da:0e:00
no member pwwn 50:06:0e:80:06:da:0e:21
member pwwn 50:06:0e:80:07:50:75:08
member pwwn 50:06:0e:80:07:50:75:40
zoneset activate name Windows vsan 4
end
'''

#!/usr/bin/env python
import paramiko
import time
 
 
 
USER = 'admin'
PASSWORD = 'c!sco123'
devies = ['10.91.33.160',
           ]
 
 
 
commands = [
    'config t',
    'zone name ropstg014a vsan 4',
    'no member pwwn 50:06:0e:80:06:da:0e:00',
    'no member pwwn 50:06:0e:80:06:da:0e:21',
    'member pwwn 50:06:0e:80:07:50:75:08',
    'member pwwn 50:06:0e:80:07:50:75:40',
    'zoneset activate name Windows vsan 4',
    'end'
    ]
 
for device in devices:
 
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(device, username=USER, password=PASSWORD)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    chan = ssh.invoke_shell()
 
 
    for command in commands:
        chan.send(command+'\n')
        time.sleep(1)
        output = chan.recv(9999)
        print output
 
