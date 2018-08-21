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

print "Create Working Directory"

Folder = raw_input("Enter Folder Name:")

print "Creating Working Directory"
print "--------------------------"

createdir = os.system("mkdir ~/Desktop/" + Folder)

if createdir == 0:
    print "Directory Created"

else:
    print "Directory not created, cancelling"

#Call NMAP

    print "Starting NMAP Scan"
    print "------------------"

os.system("nmap -v -p 80 >") + Folder
