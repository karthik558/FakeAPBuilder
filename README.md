![HEADER_IMAGE](src/mitm.png)

## <b> ABOUT THIS PROJECT </b>

This MITM attack is based on the MDK3 tool. MDK3 is a tool that can be used to create fake APs and MITM attacks. This script is just a wrapper around the MDK3 tool. It will check if the MDK3 tool is installed or not. If not, it will install it. Then it will check if the packet injection is working or not on the interface 0/1. If not, it will abort the script. Then it will ask the user to select the correct interface to create the fake AP. It will create the fake AP on the selected interface and will start the MITM attack. The fake AP will be created using the file.lst file. The file.lst file contains the SSID and the password of the fake AP. The user can change the SSID and the password of the fake AP by editing the file.lst file.

## <b> USAGE OF THIS SCRIPT (HOW TO USE) </b>

### This script will create a lot of fake AP's and will help you to test your network and network adapter. (pentest own network)

├── 1. Download the script from the github repository. <br>
├── 2. Open the terminal and navigate to the directory where the script is downloaded.<br>
├── 3. Run the script using the command "sudo ./start.sh" (without the quotes).<br>
├── 4. The script will ask you to select the correct interface to test the packet injection.<br>
├── 5. Select the correct interface to test the packet injection.<br>
├── 6. The script will ask you to select the correct interface to create the fake AP.<br>
├── 7. Select the correct interface to create the fake AP. (The fake AP will be created using the file.lst file)<br>
├── 8. The script will create the fake AP and will start the MITM attack.<br>
├── 9. The fake AP will be created using the SSID and the password of the file.lst file.<br>
└── 10. The user can change the SSID and the password of the fake AP by editing the file.lst file.<br>

## <b> DISCLAIMER </b>

├── 1. Run this script only with <b> sudo privileges </b>. (sudo ./start.sh) (without the quotes) <br>
├── 2. Depending on your Linux distribution, you may need to install some packages. (recommended to install `aircrack-ng`,`airmon-ng`,`mdk3`.`airodump-ng`,`aireplay-ng`,`xterm` or else you will not be able to run this script.) <br>
├── 3. This script need external_wireless_adapter. (or else it will not work). <br>
├── 4. If you are using TL-WN722N, then you need to install `TL-WN722N-driver` package. (recommended to install `TL-WN722N-driver`.) use my github link to download it. ( https://github.com/karthik558/setup_kali_env/tree/main/TP-LINK ) <br>
└── 5. This script is for educational purposes only. The author is not responsible for any misuse or damage caused by this script. Use it at your own risk. <br>

## <b> THANKS TO </b>

├── Aircrack-ng (https://www.aircrack-ng.org/) <br>
├── Airmon-ng (https://www.aircrack-ng.org/) <br>
├── MDK3 (https://www.mdk3.com/) <br>
├── Airodump-ng (https://www.aircrack-ng.org/) <br>
├── Aireplay-ng (https://www.aircrack-ng.org/) <br>
└── Kali Linux (https://www.kali.org/) <br>

## <b> CONTRIBUTE TO THIS PROJECT </b>

### If you want to contribute to this project, then you can fork this project and make changes to it. Then you can make a pull request. I will review your changes and if it is good, then I will merge it to the main branch.

 ├── 1. Fork the project.  <br>
 ├── 2. Clone the project to your local machine.  <br>
 ├── 3. Create a new branch.  <br>
 ├── 4. Make the changes.  <br>
 ├── 5. Commit the changes. (include a brief description of the changes)  <br>
 ├── 6. Push the changes to the remote repository.  <br>
 └── 7. Create a pull request. <br>

## <b> AUTHOR OF THIS PROJECT </b>

Author: KARTHIK LAL (karthik558) <br>
Author Website: https://karthiklal.live <br>

 ## <b> CONTACT AUTHOR </b>

├── 1. Email: karthik.lal558@gmail.com | karthiklal@duck.com <br>
├── 2. Website: https://karthiklal.live#contact <br>
├── 3. Twitter: https://twitter.com/_karthik558 <br>
├── 4. Instagram: https://instagram.com/_karthiklal <br>
├── 5. Facebook: https://facebook.com/karthik5588 <br>
├── 6. LinkedIn: https://linkedin.com/in/karthik558 <br>
└── 7. GitHub: https://github.com/karthik558 <br>

## <b> LICENSE </b>

This script is licensed under the GNU General Public License V3.0<br>
*  This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
*  MITM ATTACK is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
* You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.