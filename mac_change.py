#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print("""
MAC Address Changer
1) Set a Random MAC Address
2) Manually Set a MAC Address
3) Restore Original MAC Address

""")

# Get user input for the operation number
process_no = raw_input("Enter Operation Number (1,2,3): ")

if(process_no == "1"):
    # Disable the network interface
    os.system("ifconfig eth0 down")
    # Change MAC address to a random one
    os.system("macchanger -r eth0")
    # Enable the network interface
    os.system("ifconfig eth0 up")
    print("\nMAC Address Set Randomly!")

elif(process_no == "2"):
    # Get new MAC address input from user
    mac_adres = raw_input("Enter New MAC Address: ")
    # Disable the network interface
    os.system("ifconfig eth0 down")
    # Change MAC address to the user-defined value
    os.system("macchanger --mac " + mac_adres + " eth0")
    # Enable the network interface
    os.system("ifconfig eth0 up")
    print("\nMAC Address Set Manually!")

elif(islem_no == "3"):
    # Disable the network interface
    os.system("ifconfig eth0 down")
    # Restore the original MAC address
    os.system("macchanger -p eth0")
    # Enable the network interface
    os.system("ifconfig eth0 up")
    print("\nMAC Address Restored to Original!")

else:
    print("Invalid selection!")
