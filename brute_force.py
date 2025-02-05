#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("""
Port Brute Force
1) FTP
2) SSH

""")

processno = raw_input("Enter Process no: ")
targetip = raw_input("Enter Target ip: ")
username = raw_input("File Path of usernames: ")
password = raw_input("File Path of passwords: ")

if(processno == "1"):
	os.system("ncrack -p 21 -U " + username + " -P " + password + " " + targetip)

elif(processno == "2"):
	os.system("ncrack -p 22 -U " + username + " -P " + password + " " + targetip)
