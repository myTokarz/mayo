#!/usr/bin/env python
'''
Simple script to rename a system.  

For example, the following desired configuration is pushed to the switch

scope system
set owner $arg_0 
commit-buffer
show detail
'''

import paramiko
import time
import argparse

# define switch information 
USER = 'admin'
PASSWORD = 'password'
devices = ['10.91.86.207',
           '10.91.86.207'
           ]

# Parse in the inputs
parser = argparse.ArgumentParser(description='Renames the Fabric Interconnect')
parser.add_argument("-n", "--name", required=True, type=str, help='New name for the FI')
args = parser.parse_args()

print ("Renaming Fabric Interconnect to "+args.name)

# Define the commands to run 
commands = [
    'scope system',
    'set owner '+args.name,
    'commit-buffer',
    'show detail'
    ]

 
# This block of code executes the commands on each switch 
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
        print (output)

# Do some work to determine what we did was correct
 
