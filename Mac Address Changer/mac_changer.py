#!/usr/bin/env python3

import subprocess
import optparse
import re

# ----------------------------------------
# Function to handle command-line arguments
# ----------------------------------------
def parser():
    # OptionParser is used to read arguments from terminal
    parser = optparse.OptionParser()

    # -i or --interface : network interface name (eth0, wlan0, etc.)
    parser.add_option(
        "-i", "--interface",
        dest="interface",
        help="Interface to change its MAC address"
    )

    # -m or --mac : new MAC address
    parser.add_option(
        "-m", "--mac",
        dest="mac",
        help="New MAC address"
    )

    (options, args) = parser.parse_args()

    # Validation: interface must be provided
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")

    # Validation: MAC address must be provided
    if not options.mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info")

    return options


# ----------------------------------------
# Function to change MAC address
# ----------------------------------------
def mac_changer(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")

    # Bring interface down
    subprocess.call(f"ifconfig {interface} down", shell=True)

    # Change MAC address
    subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)

    # Bring interface up
    subprocess.call(f"ifconfig {interface} up", shell=True)


# ----------------------------------------
# Function to get current MAC address
# ----------------------------------------
def get_current_mac(interface):
    # Capture output of ifconfig command
    result = subprocess.check_output(["ifconfig", interface]).decode()

    # Regex pattern to match MAC address
    mac_search = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",
        result
    )

    if mac_search:
        return mac_search.group(0)
    else:
        return None


# ----------------------------------------
# Function to validate MAC address format
# ----------------------------------------
def validate_mac(mac):
    # Valid MAC format: XX:XX:XX:XX:XX:XX
    pattern = r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$"
    return re.match(pattern, mac)


# ----------------------------------------
# Main Program Execution
# ----------------------------------------
options = parser()

# Validate MAC format before applying
if not validate_mac(options.mac):
    print("[-] Invalid MAC address format")
    exit(1)

# Get and display old MAC address
current_mac = get_current_mac(options.interface)
if current_mac:
    print(f"[+] Current MAC address: {current_mac}")
else:
    print("[-] Could not read current MAC address")

# Change MAC address
mac_changer(options.interface, options.mac)

# Verify MAC address change
new_mac = get_current_mac(options.interface)

if new_mac == options.mac:
    print(f"[+] MAC address successfully changed to {new_mac}")
else:
    print("[-] MAC address change failed")
