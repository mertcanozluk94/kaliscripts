#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("Vulnerability Analysis Tool")
target_ip = raw_input("Target IP: ")
os.system("nikto -h " + target_ip)
