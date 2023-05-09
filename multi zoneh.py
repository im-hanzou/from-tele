#Coded By HYPER
try:

    import requests,sys,time
    import re
    user = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}

    url_1 = "http://www.zone-h.org/archive/notifier="
    url_2 = "http://zone-h.org/archive/page=1"
    my_cook = {
        "ZHE" : "",
        "PHPSESSID" : ""
    }

    def clearscreen():
        print("\033[2J\033[1;1H")

    def get_urls_for_user(user_name):
        urls = []
        for i in range(1, 51):
            response = requests.get(url_1 + user_name +"/page=" + str(i), cookies=my_cook, headers=user)
            content = response.content
            print("\033[92m" + url_1 + user_name +"/page=" + str(i))
            if '<html><body>-<script type="text/javascript"' in content:
                print("Change Your Cookie Addresses")
                break
            elif '<input type="text" name="captcha" value=""><input type="submit">' in content:
                print("Please open zone-h in browser and enter captcha.")
                break
            else:
                urls_found = re.findall('<td>(.*)\n							</td>', content)
                if '/mirror/id/' in content:
                    for url in urls_found:
                        url_cleaned = url.replace('...','')
                        print ('    ['  + '*' + '] ') + url_cleaned.split('/')[0]
                        urls.append("http://" + url_cleaned.split('/')[0])
                else:
                    print("Grabber process finished.")
                    break
        return urls

    def get_all_urls():
        all_urls = []
        for i in range(1, 51):
            response = requests.get(url_2 + "/page=" + str(i), cookies=my_cook, headers=user)
            content = response.content

            if '<html><body>-<script type="text/javascript"' in content:
                print("Please Update Your Cookie Addresses ZHE & PHPSESSID")
                break
                    
            elif "captcha" in content:
                print("Please open [zone-h.org] in any browser and enter the captcha")
                break
            else:
                urls_found = re.findall('<td>(.*)\n							</td>', content)
                for url in urls_found:
                    url_cleaned = url.replace('...','')
                    print ('    ['  + '*' + '] ') + url_cleaned.split('/')[0]
                    all_urls.append("http://" + url_cleaned.split('/')[0])
        return all_urls
    
    def main():
        clearscreen()

        msg0 ="Coded By Hyper Multi Zone H Notifier Grabber\n"

        for i in msg0:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.02)
        print("""
        [1] \033[92mMulti Notifier
        [2] \033[92mOnhold
        """)
        choice = int(raw_input("\033[91m[-] \033[90m\033[92m Please enter number\033[95m : \033[90m"))
        if choice == 1:
            user_names = []
            num_of_users = int(raw_input("\033[94mHow many usernames do you want to add?: "))
            for i in range(num_of_users):
                user_name = raw_input("\033[94muser name " + str(i+1) + ": ")
                user_names.append(user_name)
            for user_name in user_names:
                print("\033[92mGrabbing URLs for user " + user_name + "...")
                urls = get_urls_for_user(user_name)
                print("\033[92mNumber of URLs found: " + str(len(urls)))
                with open(user_name + ".txt", "w") as f:
                    for url in urls:
                        f.write(url + "\n")
            print("\033[94mAll URLs grabbed successfully.")

        elif choice == 2:
            all_urls = get_all_urls()
            print("\033[94mNumber of URLs found: " + str(len(all_urls)))
            with open("all_urls.txt", "w") as f:
                for url in all_urls:
                    f.write(url + "\n")
            print("\033[94mAll URLs grabbed successfully.")

        else:
            print("\033[91mInvalid choice. Exiting...")
            return

    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print("CTRL + C Detected.")