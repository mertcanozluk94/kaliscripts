#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("VPN Control Tool")
target_ip = raw_input("Target IP: ")
os.system("ike-scan " + target_ip)
