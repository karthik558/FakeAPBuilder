import os
import time
import argparse
import subprocess
import logging
import signal
import random

# Colors for the terminal
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
BLUE = '\033[0;34m'
VIOLET = '\033[0;35m'
CYAN = '\033[0;36m'
BLACK = '\033[0;30m'
NC = '\033[0m'  # No Color

# Create a logger object and configure it
logger = logging.getLogger('fakeapbuilder')
logger.setLevel(logging.DEBUG)
# Create a file handler and a formatter for the logger
fh = logging.FileHandler('fakeapbuilder.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# Add the file handler to the logger
logger.addHandler(fh)
# Create a stream handler for the logger
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
# Add the stream handler to the logger
logger.addHandler(sh)

# Let's start the script with a banner
def display_banner():
    banner =  "#########::::'## ::::'##:::'##:'########::::'###::::'########::\n"
    banner += "##.....::::'## ##::: ##::'##:: ##.....::::'## ##::: ##.... ##:\n"
    banner += "##::::::::'##:. ##:: ##:'##::: ##::::::::'##:. ##:: ##:::: ##:\n"
    banner += "######:::'##:::. ##: #####:::: ######:::'##:::. ##: ########::\n"
    banner += "##...:::: #########: ##. ##::: ##...:::: #########: ##.....:::\n"
    banner += "##::::::: ##.... ##: ##:. ##:: ##::::::: ##.... ##: ##::::::::\n"
    banner += "##::::::: ##:::: ##: ##::. ##: ########: ##:::: ##: ##::::::::\n"
    print(banner)

display_banner()

# Terminal header settings and information
logger.info(f"{RED}Developer    :   KARTHIK LAL (https://karthiklal.in){NC}")
logger.info(f"{RED}Created Date :   2021-12-07{NC}")
logger.info(f"{RED}Project      :   FakeAPBuilder{NC}")
logger.info(f"{RED}Purpose      :   To create a fake access point for penetration testing{NC}")
logger.info(f"{RED}Caution      :   This script is for educational purposes only. I am not responsible for any misuse of this script{NC}")
print()

# Parse command-line arguments and options
parser = argparse.ArgumentParser(description='FakeAPBuilder: A Python script to create a fake access point for penetration testing')
parser.add_argument('-a', '--adapter', type=str, default='wlan0', help='The name of the wireless adapter to use (default: wlan0)')
parser.add_argument('-n', '--name', type=str, default=None, help='The name of the fake access point to create (default: random)')
parser.add_argument('-c', '--channel', type=int, default=1, help='The channel of the fake access point to use (default: 1)')
parser.add_argument('-f', '--file', type=str, default='random___strings.lst', help='The file containing the ESSID list for the fake access point (default: random___strings.lst)')
args = parser.parse_args()

# Abort the script if the user is not root
logger.info(f"{YELLOW}Checking if you are running this script on su mode or not{NC}")
if not os.geteuid() == 0:
    logger.error(f"{RED}This script must be run as root{NC}")
    time.sleep(1)
    exit()
else:
    logger.info(f"{GREEN}You are running this script on su mode{NC}")
    time.sleep(1)
    os.system("clear")

# Install mdk4 if it is not installed
logger.info(f"{YELLOW}Checking if mdk4 is installed or not{NC}")
try:
    subprocess.run(['which', 'mdk4'], check=True)
    logger.info(f"{GREEN}mdk4 is installed{NC}")
    time.sleep(1)
except subprocess.CalledProcessError:
    logger.warning(f"{RED}mdk4 is not installed{NC}")
    time.sleep(1)
    logger.info(f"{YELLOW}Installing mdk4{NC}")
    subprocess.run(['apt-get', 'install', 'mdk4', '-y'], check=True)
    time.sleep(1)
    logger.info(f"{GREEN}mdk4 is installed{NC}")
    time.sleep(1)
    
# Check if the wireless adapter is compatible with packet injection or not
logger.info(f'{YELLOW}Checking if the wireless adapter is compatible with packet injection or not{NC}')

# List available wireless adapters
output = subprocess.check_output(['iwconfig'])
logger.info(f'Available wireless adapters:\n{output.decode()}')

# Prompt user to select a wireless adapter
adapter = input(f'Enter the name of the wireless adapter to test (default: {args.adapter}): ') or args.adapter

# Test packet-injection on the selected adapter
logger.info(f'{RED}Starting the injection test on {adapter}...{NC}')
subprocess.run(['sudo', 'ifconfig', adapter, 'down'], check=True)
subprocess.run(['sudo', 'iwconfig', adapter, 'mode', 'monitor'], check=True)
subprocess.run(['sudo', 'ifconfig', adapter, 'up'], check=True)
output = subprocess.check_output(['sudo', 'iwconfig', adapter])
logger.info(f'Wireless adapter configuration:\n{output.decode()}')
logger.info(f'{GREEN}Injecting packets on {adapter}...{NC}')
result = subprocess.run(['sudo', 'aireplay-ng', '--test', adapter], check=True)
if result.returncode == 0:
    logger.info(f'{GREEN}Packet injection test done on {adapter} and it\'s working fine.{NC}')
else:
    logger.error(f'{RED}Packet injection test failed on {adapter}.{NC}')

# Check if the file containing the ESSID list exists and is readable
logger.info(f'{YELLOW}Checking if the file {args.file} exists and is readable{NC}')
if os.path.isfile(args.file) and os.access(args.file, os.R_OK):
    logger.info(f'{GREEN}The file {args.file} is valid{NC}')
else:
    logger.error(f'{RED}The file {args.file} is missing or not readable{NC}')
    exit()

# Generate a random name for the fake access point if the user does not specify one
if args.name is None:
    logger.info(f'{YELLOW}Generating a random name for the fake access point{NC}')
    names = ['Free WiFi', 'FBI Surveillance Van', 'Virus Detected', 'Loading...', 'Hidden Network', 'Skynet']
    args.name = random.choice(names)
    logger.info(f'{GREEN}The name of the fake access point is {args.name}{NC}')

# Define a handler function to handle keyboard interrupts and other signals
def signal_handler(signal, frame):
    logger.info(f'{RED}Terminating the script{NC}')
    subprocess.run(['sudo', 'ifconfig', adapter, 'down'], check=True)
    subprocess.run(['sudo', 'iwconfig', adapter, 'mode', 'managed'], check=True)
    subprocess.run(['sudo', 'ifconfig', adapter, 'up'], check=True)
    logger.info(f'{GREEN}Restored the original configuration of {adapter}{NC}')
    exit()

# Register the handler function for keyboard interrupts and other signals
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Create a fake access point based on user input
logger.info(f'{YELLOW}Creating a fake access point with the previously tested wireless adapter : {adapter}{NC}')

# If a single SSID name is specified
if args.name:
    logger.info(f'{YELLOW}Using single SSID: {args.name}{NC}')
    subprocess.run(['mdk4', adapter, 'b', '-c', str(args.channel), '-n', args.name], check=True)
else:
    # If a file containing ESSID list is specified
    logger.info(f'{YELLOW}Using ESSID list from file: {args.file}{NC}')
    subprocess.run(['mdk4', adapter, 'b', '-c', str(args.channel), '-f', args.file], check=True)

# Press enter to exit
input(f"{GREEN}Press enter to exit{NC}")
