#!/usr/bin/env python3
# Duino-Coin Router Miner
#
# This script is designed to run on OpenWRT-based routers
# and mine Duino-Coin using low CPU resources.

import hashlib
import os
from socket import socket
import sys           # Standard Python libraries only
import time
import requests      # Used to fetch mining pool information


# ===================== USER CONFIGURATION =====================

# Duino-Coin username
username = "sapna"          # Change this to your Duino-Coin username

# Mining key (optional security feature)
mining_key = "None"         # Set your mining key if enabled on your account

# LED configuration (specific to OpenWRT routers)
leds = True                 # Enable/disable LED notifications

# LED names as exposed by OpenWRT (/sys/class/leds/)
accepted = "fritz4040:amber:info"   # LED for accepted shares
rejected = "fritz4040:red:info"     # LED for rejected shares


# Create a TCP socket for communication with the mining server
soc = socket()


# ===================== HELPER FUNCTIONS =====================

def current_time():
    """
    Returns the current local time in HH:MM:SS format.
    Used for timestamped logging.
    """
    t = time.localtime()
    return time.strftime("%H:%M:%S", t)


def fetch_pools():
    """
    Fetches the fastest available Duino-Coin mining pool
    from the official Duino-Coin API.
    Retries every 15 seconds on failure.
    """
    while True:
        try:
            response = requests.get(
                "https://server.duinocoin.com/getPool"
            ).json()

            NODE_ADDRESS = response["ip"]
            NODE_PORT = response["port"]

            return NODE_ADDRESS, NODE_PORT

        except Exception:
            print(f"{current_time()}: Error retrieving mining node, retrying in 15s")
            time.sleep(15)


def led(status):
    """
    Controls router LEDs to visually indicate
    accepted or rejected shares.
    """
    if leds:
        with open(f"/sys/class/leds/{accepted if status else rejected}/brightness", "w") as f:
            f.write("1")

        time.sleep(0.3)

        with open(f"/sys/class/leds/{accepted if status else rejected}/brightness", "w") as f:
            f.write("0")


# ===================== MAIN MINING LOOP =====================

while True:
    try:
        print(f"{current_time()}: Searching for fastest connection to the server")

        try:
            NODE_ADDRESS, NODE_PORT = fetch_pools()
        except Exception:
            NODE_ADDRESS = "server.duinocoin.com"
            NODE_PORT = 2813
            print(f"{current_time()}: Using default server port and address")

        soc.connect((str(NODE_ADDRESS), int(NODE_PORT)))
        print(f"{current_time()}: Fastest connection found")

        server_version = soc.recv(100).decode()
        print(f"{current_time()}: Server Version: {server_version}")

        while True:
            soc.send(bytes(
                "JOB,"
                + str(username)
                + ",LOW,"
                + mining_key,
                encoding="utf8"
            ))

            job = soc.recv(1024).decode().rstrip("\n")
            job = job.split(",")

            difficulty = job[2]
            hashingStartTime = time.time()

            base_hash = hashlib.sha1(str(job[0]).encode("ascii"))

            for result in range(100 * int(difficulty) + 1):
                temp_hash = base_hash.copy()
                temp_hash.update(str(result).encode("ascii"))
                ducos1 = temp_hash.hexdigest()

                if job[1] == ducos1:
                    hashingStopTime = time.time()
                    timeDifference = hashingStopTime - hashingStartTime
                    hashrate = result / timeDifference

                    soc.send(bytes(
                        str(result)
                        + ","
                        + str(hashrate)
                        + ",Router Miner",
                        encoding="utf8"
                    ))

                    feedback = soc.recv(1024).decode().rstrip("\n")

                    if feedback == "GOOD":
                        print(
                            f"{current_time()} : Accepted share",
                            result,
                            "Hashrate",
                            int(hashrate / 1000),
                            "kH/s",
                            "Difficulty",
                            difficulty
                        )
                        led(True)
                        break

                    elif feedback == "BAD":
                        print(
                            f"{current_time()}: Rejected share",
                            result,
                            "Hashrate",
                            int(hashrate / 1000),
                            "kH/s",
                            "Difficulty",
                            difficulty
                        )
                        led(False)
                        break

    except Exception as e:
        print(f"{current_time()}: Error occurred: {e}, restarting in 5s.")
        time.sleep(5)
        os.execl(sys.executable, sys.executable, *sys.argv)
