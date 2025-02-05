#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("""
Port Scanning Options
1) Quick Scan
2) Service and Version Detection
3) Operating System Detection
4) Vulnerability Scan
5) In-Depth Scan
6) Scan Specific Ports
""")

# Get user input for the operation number
process_no = input("Enter Operation Number (1,2,3,4,5,6): ")
# Get target IP or domain from user
target_ip = input("Enter Target IP or Domain: ")

if process_no == "1":
    # Perform a quick scan
    os.system(f"nmap -T4 {target_ip}")

elif process_no == "2":
    # Perform service and version detection
    os.system(f"nmap -sS -sV {target_ip}")

elif process_no == "3":
    # Perform OS detection
    os.system(f"nmap -O {target_ip}")

elif process_no == "4":
    # Perform a vulnerability scan
    os.system(f"nmap --script vuln {target_ip}")

elif process_no == "5":
    # Perform an in-depth scan
    os.system(f"nmap -A -T4 {target_ip}")

elif process_no == "6":
    # Get specific ports from user
    ports = input("Enter the ports to scan (comma-separated, e.g., 80,443,22): ")
    os.system(f"nmap -p {ports} {target_ip}")

else:
    print("Invalid selection!")
