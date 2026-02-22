import os
import time
import sys

def setup():
    # Dependency Check
    print("\033[95m[+] UI Upgrade Start Ho Raha Hai...\033[0m")
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install figlet ncurses-utils -y")
    os.system("clear")

    # Interactive Customization
    print("\033[38;5;13m" + "═"*40)
    print("      TERMUX CUSTOMIZER BY PARI")
    print("═"*40 + "\033[0m")
    
    header_input = input("\033[38;5;250m[?] Header Name (Default: HACKER): \033[0m") or "HACKER"
    shell_input = input("\033[38;5;250m[?] Shell Name (Default: PARI): \033[0m") or "PARI"

    bashrc_path = os.path.expanduser("~/.bashrc")
    
    # Exact Midnight Purple-Gray from Image (\033[48;5;234m)
    # Welome Message with Sleek Borders
    content = f"""
# Midnight Purple Background Setup
echo -e "\\e[48;5;234m\\e[2J"
clear

# Professional Pink Header
echo -e "\\e[38;5;198m"
figlet -f standard "{header_input}"
echo -e "\\e[0m"

# Welcome Banner (Gray on Deep Purple)
echo -e "\\e[38;5;234m" # Hidden text for spacing
echo -e "\\e[48;5;55m\\e[38;5;255m  CONNECTED AS: BOSS  \\e[0m"
echo -e "\\e[38;5;245mWelcome Back, Access Granted.\\e[0m"
echo ""

# Modern Shell Prompt (Green User @ Blue Path)
export PS1="\\033[38;5;82m{shell_input}\\033[38;5;255m@\\033[38;5;45mtermux\\033[38;5;255m:[\\033[38;5;226m\\w\\033[38;5;255m]\\033[38;5;198m#\\033[0m "
"""

    with open(bashrc_path, "w") as f:
        f.write(content)

    # UI Loading Animation
    os.system("clear")
    print("\033[38;5;13mFinalizing UI...")
    for i in range(21):
        sys.stdout.write(f"\r\033[38;5;55m[{'#' * i}{'.' * (20-i)}] {i*5}%")
        sys.stdout.flush()
        time.sleep(0.05)
    
    print(f"\n\n\033[32m[+] UI Set Successfully!")
    time.sleep(1)

    # SHOW LIVE PREVIEW
    os.system("clear && echo -e '\\e[48;5;234m\\e[2J' && clear")
    os.system(f"echo -e '\\e[38;5;198m' && figlet -f standard '{header_input}' && echo -e '\\e[0m'")
    os.system("echo -e '\\e[48;5;55m\\e[38;5;255m  CONNECTED AS: BOSS  \\e[0m'")
    print(f"\n\033[38;5;82m{shell_input}\033[38;5;255m@\033[38;5;45mtermux\033[38;5;255m:[\033[38;5;226m~\033[38;5;255m]\033[38;5;198m#\033[0m ")

if __name__ == "__main__":
    setup()
