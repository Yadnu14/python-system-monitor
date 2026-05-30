```python
import psutil
import time
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

LOG_FILE = "logs.txt"


def clear_screen():
    # Works on both Windows and Linux/Docker
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def log_warning(message):
    with open(LOG_FILE, "a") as file:
        file.write(f"{time.ctime()} - {message}\n")


while True:
    clear_screen()

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + "         SYSTEM MONITOR")
    print(Fore.CYAN + "=" * 40)

    print(Fore.GREEN + f"CPU Usage   : {cpu}%")
    print(Fore.GREEN + f"RAM Usage   : {ram}%")
    print(Fore.GREEN + f"Disk Usage  : {disk}%")

    print(Fore.CYAN + "=" * 40)

    # Warnings
    if cpu > 80:
        warning = "WARNING: High CPU Usage!"
        print(Fore.RED + warning)
        log_warning(warning)

    if ram > 85:
        warning = "WARNING: High RAM Usage!"
        print(Fore.RED + warning)
        log_warning(warning)

    if disk > 90:
        warning = "WARNING: Disk Almost Full!"
        print(Fore.RED + warning)
        log_warning(warning)

    print(Fore.MAGENTA + "\nRefreshing every 2 seconds...")

    time.sleep(2)
```
