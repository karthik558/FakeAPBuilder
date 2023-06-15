import os
import time

# Colors for the terminal
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
BLUE = '\033[0;34m'
VIOLET = '\033[0;35m'
CYAN = '\033[0;36m'
BLACK = '\033[0;30m'
NC = '\033[0m'  # No Color

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
print(f"{RED}Developer    :   KARTHIK LAL (https://karthiklal.live){NC}")
print(f"{RED}Created Date :   2021-12-07{NC}")
print(f"{RED}Project      :   FakeAPBuilder{NC}")
print(f"{RED}Purpose      :   To create a fake access point for penetration testing{NC}")
print(f"{RED}Caution      :   This script is for educational purposes only. I am not responsible for any misuse of this script{NC}")
print()

# Abort the script if the user is not root
print(f"{YELLOW}Checking if you are running this script on su mode or not{NC}")
if not os.geteuid() == 0:
    print(f"{RED}This script must be run as root{NC}")
    time.sleep(1)
    exit()
else:
    print(f"{GREEN}You are running this script on su mode{NC}")
    time.sleep(1)
    os.system("clear")

# Install mdk3 if it is not installed
print(f"{YELLOW}Checking if mdk3 is installed or not{NC}")
if os.system("which mdk3") == 0:
    print(f"{GREEN}mdk3 is installed{NC}")
    time.sleep(1)
else:
    print(f"{RED}mdk3 is not installed{NC}")
    time.sleep(1)
    print(f"{YELLOW}Installing mdk3{NC}")
    os.system("apt-get install mdk3 -y")
    time.sleep(1)
    print(f"{GREEN}mdk3 is installed{NC}")
    time.sleep(1)
    
# Check if the wireless adapter is compatible with packet injection or not
print(f'{YELLOW}Checking if the wireless adapter is compatible with packet injection or not{NC}')

# List available wireless adapters
os.system('iwconfig')

# Prompt user to select a wireless adapter
adapter = input('Enter the name of the wireless adapter to test (e.g. wlan0): ')

# Test packet-injection on the selected adapter
print(f'{RED}Starting the injection test on {adapter}...{NC}')
os.system(f'sudo ifconfig {adapter} down')
os.system(f'sudo iwconfig {adapter} mode monitor')
os.system(f'sudo ifconfig {adapter} up')
os.system(f'sudo iwconfig {adapter}')
print(f'{GREEN}Injecting packets on {adapter}...{NC}')
result = os.system(f'sudo aireplay-ng --test {adapter}')
if result == 0:
    print(f'{GREEN}Packet injection test done on {adapter} and it\'s working fine.{NC}')
else:
    print(f'{RED}Packet injection test failed on {adapter}.{NC}')

# With the help of the following code, we can create a fake access point
print(f'{YELLOW}Creating a fake access point with the previously tested wireless adapter : {adapter}{NC}')
os.system(f"mdk3 {adapter} b -c 1 -f random___strings.lst")

# Press enter to exit
print(f"{GREEN}Press enter to exit{NC}")
