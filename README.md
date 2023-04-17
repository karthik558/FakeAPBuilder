# FakeAPBuilder - A User-Friendly Interface for MDK3 

![HEADER_IMAGE](src/mitm.png)

This tool, called FakeAPBuilder, builds upon the functionality of the MDK3 tool, which enables users to create fake access points (APs) and carry out Man-in-the-Middle (MITM) attacks. The FakeAPBuilder script acts as a user-friendly interface for the MDK3 tool by automating several steps in the process.

First, the script checks whether MDK3 is installed. If it is not, it installs the tool. Next, it verifies whether packet injection is working on the user's interface. If it is not, the script will terminate.

Assuming the packet injection is functioning, the user is prompted to select the desired interface for creating the fake AP. Once selected, the script leverages the information in the file.lst file to create the fake AP, which includes both the SSID and the password of the fake AP.

If the user desires to modify the SSID or password, they can simply edit the file.lst file prior to running the script. Once the fake AP has been created, the MITM attack can commence. Overall, the FakeAPBuilder tool provides an accessible means for users to create fake APs and carry out MITM attacks using the MDK3 tool.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
- Run the script with root privileges only (sudo).
- Install the following dependencies:
  - MDK3
  - Aircrack-ng
  - Python 3
- Make sure that your wireless card supports packet injection and monitor mode.

## Usage
- `git clone https://github.com/karthik558/FakeAPBuilder && cd FakeAPBuilder`
- `sudo python3 FakeAPBuilder.py`
- Follow the on-screen instructions.
- Update Run `random__strings__generator.py` to generate random SSIDs and copy the output to random__strings.lst file.

## Contributing

Contributions to the project are welcome. If you would like to suggest an improvement or report a bug, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).