from socket import timeout
import requests
import re
from multiprocessing.dummy import Pool
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
from colorama import Fore
from colorama import Style
from colorama import init
from time import sleep
init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT


def finder(i):
    try :
        list_users = ['leafmailer2.8.php','leaf.php','lf.php','leafmailer.php','wp-conetnt/leaf.php','wp-admin/leaf.php','wp-content/leafmailer2.8.php','wp-admin/leafmailer2.8.php','mailer.php','leaf-mailer.php']
        for ma in list_users :
            url = i+'/'+ma
            check = requests.get(url, timeout=10, headers=head).text
            if 'Leaf PHPMailer</title>' in check :
                print(fg+'Found one :     '+i)
                open('mailers.txt','a').write(url+'\n')
            elif 'method=post>Password:' in check :
                print(fy+'password ===  '+i)
                open('password_mailer.txt','a').write(url+'\n')
            else:
                print(fr+'Not found :::::    '+i)
    except :
        pass
def main() :
    ad =  input('Enter list sites : ')
    oppp = open(ad, 'r',errors='ignore').read().splitlines()
    utchiha = Pool(int(100))
    utchiha.map(finder, oppp)
main()