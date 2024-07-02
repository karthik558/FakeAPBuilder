# FakeAPBuilder - Create Fake Access Points for Penetration Testing

![HEADER_IMAGE](src/mitm.png)

FakeAPBuilder is a Python script designed to create fake access points for penetration testing purposes. This tool can generate SSIDs from a provided list or use a single random SSID.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Running the Script](#running-the-script)
- [Generating Random SSIDs](#generating-random-ssids)
- [Script Output](#script-output)
- [Troubleshooting](#troubleshooting)
- [Logging and Debugging](#logging-and-debugging)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [Author](#author)
- [License](#license)

## Requirements

- Run the script with root privileges only (sudo).
- Make sure that your wireless card supports packet injection and monitor mode. (Use `airmon-ng start <interface>` to enable monitor mode).

## Features

- Create a fake access point with a specified wireless adapter.
- Use a list of SSIDs from a file or generate a single random SSID.
- Specify the channel for the fake access point.
- Ensure the wireless adapter supports packet injection.
- Log all actions for easy debugging.

## Installation

Clone the repository and navigate to the directory:

```bash
git clone https://github.com/karthik558/FakeAPBuilder
cd FakeAPBuilder
```

Before running the script, ensure you have the necessary dependencies installed:

- `Python 3`
- `mdk4`
- `aircrack-ng`

You can install `mdk4` and `aircrack-ng` on a Debian-based system using:

```bash
sudo apt-get update
sudo apt-get install mdk4 aircrack-ng
```

## Usage

Command-line Options
  
```
-a, --adapter: The name of the wireless adapter to use (default: wlan0).
-n, --name: The name of the fake access point to create (default: random).
-c, --channel: The channel of the fake access point to use (default: 1).
-f, --file: The file containing the ESSID list for the fake access point (default: random___strings.lst).
-h, --help: Show the help message and exit.
```
## Running the Script

To run the script, use the following command:
```bash
sudo python FakeAPBuilder.py -a <adapter> -c <channel> -f <file>
```
example:
```bash
sudo python FakeAPBuilder.py -a wlan0 -c 6 -f random___strings.lst
```

## Generating Random SSIDs

To generate random SSIDs for the fake access point, use the following command:
```python 
python random__string__generator.py
```

- Enter the length of the random strings to generate.
- Enter the number of random strings to generate.
- The random strings will be stored in the file `random___strings.lst`.

## Script Output

The script will log actions and information to both the terminal and a log file (fakeapbuilder.log). This includes:

- Checking if the script is run as root.
- Checking and installing mdk4.
- Checking if the wireless adapter supports packet injection.
- Validating the SSID list file.
- Creating the fake access point.

## Troubleshooting

If you cannot see the created SSIDs on your Wi-Fi devices, consider the following:

- Channel and Frequency Compatibility: Ensure the channel used is supported by your devices.
- Adapter Capability and Configuration: Ensure your adapter is in monitor mode and has sufficient power.
- Environment and Interference: Ensure minimal interference from other wireless networks and devices.
- Driver Issues: Ensure drivers for your wireless adapter are up to date.
- Device Scan Interval: Ensure your scanning devices are scanning continuously and not missing the broadcast.

## Logging and Debugging

The script provides detailed logging for troubleshooting. Check the fakeapbuilder.log file for information on script actions and any potential errors.

## Contributing

Contributions to the project are welcome. If you would like to suggest an improvement or report a bug, please open an issue or submit a pull request.

## Disclaimer

This script is intended for educational purposes only. The author is not responsible for any misuse of this script. Ensure you have permission before using this script on any network.

## Author

KARTHIK LAL (https://karthiklal.in)

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).