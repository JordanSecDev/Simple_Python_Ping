#!/usr/bin/python

print "Python Ping Tool"

import os
hostname = raw_input("Enter Host:")
response = os.system("ping -c 3 " + hostname)

if response == 0:
    print hostname, 'Is UP!'
else:
    print hostname, 'Is DOWN!'

#Create Working Directory

Folder = raw_input("Enter Folder Name")

print "Creating Working Directory"
print "--------------------------"

os.system("mkdir ~/Desktop/ " + Folder)

print "Directory Created"

#Call NMAP

if response == 0:
    print "Starting NMAP Scan"
    print "------------------"
else:
    print "Host is DOWN, cancelling"

os.system("nmap -v -p 80")