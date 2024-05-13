# wificrack
crack wifi password

# WiFi Cracker Script

This Python script automates the process of cracking WiFi passwords using a combination of tools like `airmon-ng`, `airodump-ng`, `aireplay-ng`, and `aircrack-ng`. It simplifies the process by guiding the user through the necessary steps and providing instructions along the way.

## Features

- Automated WiFi password cracking process.
- User-friendly prompts and instructions.


## Prerequisites

- This script requires Python 3.x.
- Connect The External WIFI adapter
- Ensure that the necessary WiFi hacking tools (`airmon-ng`, `airodump-ng`, `aireplay-ng`, `aircrack-ng`) are installed on your system.
- Download a wordlist file. In kali or parrot there is a wordlist file already present in this location `/usr/share/wordlists/rockyou.txt` 
- **Note:** Make sure to run the script as root for full functionality.

## Usage

1. Clone this repository to your local machine:


`git clone https://github.com/Ankit1927/wificrack.git`

`python3 wificrack.py` (run this command in sudo mode)

`airodump-ng wlan0`  (Run this command in new terminal with sudo, to see all available wifi Network when you locate your prefered one press `ctrl+c` to exit)

now back to your terminal

copy and paste BSSID of the wifi router of your choice.

then enter CH (channel number)

again open new tab in termianl and paste this

`airodump-ng --bssid 4C:93:A6:88:0D:B3 -c 6 wlan0 -w hand_shake`

if any device is conneted through this wifi network it appers below....(dont close this tab) and back to script....

`hit enter...`

back to other opened tab and see if WPA HANDSHAKE is being captured or not if yes then back to script and enter full path of your wordlist...

it can take some time to found the correct Passsowrd.

After exit from Script run command...

`sudo airmon-ng check kill`

`sudo service NetworkManager restart`


Tested in only Parrot/Kali linux systems till now. 



