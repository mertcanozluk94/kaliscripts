#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("Wordlist Creator Program")

minimumcharacter = raw_input("Enter Minimum Number of Characters: ")
maximumcharacter = raw_input("Enter Maximum Number of Characters: ")
character = raw_input("Enter the Characters You Want: ")

os.system("crunch "+minimumcharacter+" "+maximumcharacter+" "+character)
print("Process Completed!")
