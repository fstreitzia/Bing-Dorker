import  requests
from colorama import Fore,init
import getpass
import os
import socket
from bs4 import BeautifulSoup
import random
import ctypes
from multiprocessing.dummy import Pool
from multiprocessing import Lock

"""
created for research :))))
"""

#
init()
lock = Lock()
#

joomla = 0
wordpress = 0
drupal = 0
checked = 0

class cms_checker(object):
    def __init__(self,location_site):
        self.sites_location = location_site
        self.sites_list = []


    def site_load(self):
        location = open(self.sites_location).readlines()
        coco = [items.rstrip()for items in location]
        for data in coco:
            self.sites_list.append({'site':data})

    def checker(self,url):
        global joomla,wordpress,drupal,checked
        head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)'
        }
        info_string_box = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTBLUE_EX + 'URL' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
        check_one = requests.get(url+'/templates/system/css/system.css',headers=head).text # joomla
        check_two = requests.get(url,headers=head).text # wordpress
        check_three = requests.get(url,headers=head).text

        if 'joomla' in check_one:
            checked += 1
            joomla += 1
            lock.acquire()
            print(info_string_box+f": {url} -> "+Fore.LIGHTGREEN_EX+"joomla")
            print(url,file=open('cms_check/joomla/joomla.txt', 'a'))
            lock.release()
        elif '/wp-content/' in check_two:
            checked += 1
            wordpress += 1
            lock.acquire()
            print(info_string_box+f": {url} -> "+Fore.LIGHTGREEN_EX+"WORDPRESS")
            print(url, file=open('cms_check/wordpress/wordpress.txt', 'a'))
            lock.release()
        elif '/sites/default/' in check_three or 'content="Drupal' in  check_three:
            checked += 1
            drupal += 1
            lock.acquire()
            print(info_string_box+f": {url} -> "+Fore.LIGHTGREEN_EX+"DRUPAL")
            print(url, file=open('cms_check/drupal/drupal.txt', 'a'))
            lock.release()
        else:
            checked += 1
            lock.acquire()
            print(info_string_box+f": {url} -> "+Fore.LIGHTRED_EX+"UNKNOWN")
            print(url, file=open('cms_check/other/other.txt', 'a'))
            lock.release()


        ctypes.windll.kernel32.SetConsoleTitleW(f"[SITES IDENTIFIER] - > Sites {len(self.sites_list)} -> Checked {checked} -> Jom {joomla} -> WP {wordpress} -> DRUP {drupal} ")

    def sender(self,list_sites):
        website = list_sites['site']
        while True:
            try:
                self.checker(website)
                break
            except Exception:
                continue

    def thread(self):
        self.site_load()
        pool = Pool(40)

        try:
            for _ in pool.imap_unordered(self.sender,self.sites_list):
                pass
        except KeyboardInterrupt:
            import os
            os._exit(0)

class dorker(object):

    def __init__(self,dork,pages,proxy):
        self.dork = dork
        self.page_ammount = pages
        self.domains_bing = []
        self.proxy_required = proxy
        self.first_page_links = []


    def filter_and_adding(self,domains_list):
        alert_string = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTRED_EX + 'ALERT' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
        print(alert_string+"-> Removing Blacklisted sites And Fixing Syntax.")
        print()
        data = open('blacklist/sites.txt').readlines()
        new_data = [items.rstrip() for items in data]
        for domains in domains_list:
            domain_data = domains.split('/')
            new_domain = domain_data[0]+"//"+domain_data[2]+'/'
            if new_domain not in new_data:
                self.domains_bing.append(new_domain)
                print(new_domain,file=open('results/sites/sites.txt', 'a'))
        ctypes.windll.kernel32.SetConsoleTitleW(f"[PROXYLESS DORKER] - > Dork {self.dork} -> Sites Added {len(self.domains_bing)}")



    def first_page(self):
        try:
            url = "https://www.bing.com/search?q=" + self.dork + "&first=" + '1' + "&FORM=PERE"
            header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
            }
            source_code = requests.get(url, headers=header).text
            keyword = '<li class="b_algo"><h2><a href="'
            split_data = source_code.split(keyword)
            for x in range(10):
                links_ = split_data[x + 1].split('"')[0]
                self.first_page_links.append(links_)
        except IndexError:
            pass

    def searcher(self):
        for i in range(self.page_ammount):
            url = "https://www.bing.com/search?q=" + self.dork +"&first=" + str(i)+'1' + "&FORM=PERE"
            info_string_box = Fore.LIGHTCYAN_EX+'['+Fore.LIGHTBLUE_EX+'-'+Fore.LIGHTCYAN_EX+']'+Fore.WHITE
            added_sting = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTGREEN_EX + '+' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE

            print(info_string_box+f" Printing Page  {i}")
            print()
            header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
            }
            try:
                source_code = requests.get(url,headers=header).text
                keyword = '<li class="b_algo"><h2><a href="'
                split_data = source_code.split(keyword)
                temporary_domain_list = []
                try:
                    for x in range(10):
                        links_ = split_data[x+1].split('"')[0]
                        temporary_domain_list.append(links_)
                        print(added_sting+" - "+links_)

                except IndexError:
                    pass

                print()
                print('--------')
                self.filter_and_adding(temporary_domain_list)


            except requests.exceptions.HTTPError:
                print("Http error retrying")
                continue
            except requests.exceptions.ConnectTimeout:
                print("Connection timed out error retrying")
                continue
            except requests.exceptions.Timeout:
                print("Timeout error retrying")
                continue

            if i != 0:
                if self.first_page_links == temporary_domain_list:
                    print("Same Urls Found Again. Last Resulsts Reached | Removing Dublicates.")
                    break

    def start(self):

        self.first_page()
        self.searcher()

        print(f"Done Totat sites scrapped {len(self.domains_bing)}")


proxy_error = 0
sites_list = []

class sites_from_ip(object):
    def __init__(self,site,total,current):
        self.site = site
        self.site_list = []
        self.proxy_list = []
        self.total_ip = total
        self.current = current

    def ip(self):
        ip = socket.gethostbyname(self.site)
        info_string_box = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTBLUE_EX + '-' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
        print(info_string_box+f" IP: {ip}")
        print()
        self.get_sites(ip)

    def proxy(self):
        proxy_list = open('proxy/http/https.txt')
        removed_space = [items.rstrip()for items in proxy_list]
        for proxies in removed_space:
            self.proxy_list.append(proxies)


    def get_sites(self,ip):
        global proxy_error,sites_list
        try:
            while True:
                proxy = random.choice(self.proxy_list)

                try:
                    url = f"https://viewdns.info/reverseip/?host={ip}&t=1"
                    headerx = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.150',
                    }
                    source = requests.get(url, headers=headerx, proxies={
                        'http':proxy,
                        'https':proxy,
                    },timeout=3).text
                    if "<b>403 Forbidden - Naughty!</b>" in source:
                        loc = self.proxy_list.index(proxy)
                        self.proxy_list.pop(loc)
                        alert_string = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTRED_EX + 'ALERT' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
                        print(alert_string+f" The Proxy: {proxy} has been banned.")
                        proxy_error += 1
                        raise Exception
                    elif "Why do I have to complete a CAPTCHA?</h2>" in source:
                        loc = self.proxy_list.index(proxy)
                        self.proxy_list.pop(loc)
                        proxy_error += 1
                        raise Exception
                    else:
                        soup = BeautifulSoup(source, 'lxml')
                        data = soup.find('table', {'border': '1'})
                        try:
                            td_data = data.find_all('td')
                            td_data.pop(0)
                            i = 1
                            for item in td_data:
                                try:
                                    added_sting = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTGREEN_EX + '+' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
                                    print(added_sting+f" - {td_data[i].text}")
                                    print('http://'+td_data[i].text+'/',file=open('results/ipscan/result_sites.txt', 'a'))
                                    sites_list.append(td_data[i].text)
                                    i += 2

                                except IndexError:
                                    pass

                             

                        except AttributeError:
                            alert_string = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTRED_EX + 'ALERT' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
                            print(alert_string+": No results/The ip is protected.")
                    break
                except:
                    continue
        except KeyboardInterrupt:
            os._exit(0)

    def start(self):
        ctypes.windll.kernel32.SetConsoleTitleW(f"[SITES GRABBER BULK] - > IP Loaded {self.total_ip} -> Searched {self.current} -> Proxy Error/Ban/Captcha {proxy_error} -> Found {len(sites_list)}")
        self.proxy()
        self.ip()



def ip_grabber(site,sites_length,current):
    ctypes.windll.kernel32.SetConsoleTitleW(f"[IP GRABBER BULK] - > Sites Loaded {sites_length} -> Converted {current}")
    try:
        ip = socket.gethostbyname(site)
        info_string_box = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTBLUE_EX + 'SITE' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
        added_sting = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTGREEN_EX + 'IP' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
        print(info_string_box + f': {site} - ' + added_sting + f': {ip}')
        print(ip, file=open('results/ip/ip.txt', 'a'))
    except socket.gaierror:
        pass



ctypes.windll.kernel32.SetConsoleTitleW("[BINGDORKER] V2 JEMBUT EDITION - By Fstreitzia | Contact: icq.im/@jarot")
ammount = len(open('blacklist/sites.txt').readlines())
ammount_proxy = len(open('proxy/http/https.txt').readlines())
print("""
    _    _      Coded By : W0rmC0der
   (o)--(o)     Tools By : W0rmC0der 
  /.______.\    Mass Bing - Mass Dorker - Converter IP to Sites
  \________/    Github.com/fstreitzia/
 ./        \.   
( .        , )  
 \ \_\/\//_/ /
  ~~  ~~  ~~                                                                          
""")

print(" Root@Jancok -> "+Fore.LIGHTYELLOW_EX+f"{getpass.getuser()}"+Fore.WHITE+"  -> Karalist Urls "+Fore.LIGHTYELLOW_EX+f"{ammount}"+Fore.WHITE+" -> Https Proxies "+Fore.LIGHTYELLOW_EX+f"{ammount_proxy}"+Fore.WHITE)
print()
print("-----------------------------------------["+Fore.LIGHTBLUE_EX+"USERMENU"+Fore.WHITE+"]-----------------------------------------------")
print(Fore.LIGHTYELLOW_EX+'['+Fore.LIGHTBLUE_EX+'1'+Fore.LIGHTYELLOW_EX+']'+Fore.LIGHTWHITE_EX+" - Bing Dork Scanner.")
print(Fore.LIGHTYELLOW_EX+'['+Fore.LIGHTBLUE_EX+'2'+Fore.LIGHTYELLOW_EX+']'+Fore.LIGHTWHITE_EX+" - URL Reverse .")
print(Fore.LIGHTYELLOW_EX+'['+Fore.LIGHTBLUE_EX+'3'+Fore.LIGHTYELLOW_EX+']'+Fore.LIGHTWHITE_EX+" - Web List To IP.")
print(Fore.LIGHTYELLOW_EX+'['+Fore.LIGHTBLUE_EX+'4'+Fore.LIGHTYELLOW_EX+']'+Fore.LIGHTWHITE_EX+" - IP To Weblist.")
print(Fore.LIGHTYELLOW_EX+'['+Fore.LIGHTBLUE_EX+'5'+Fore.LIGHTYELLOW_EX+']'+Fore.LIGHTWHITE_EX+" - Taranacak Verı .")
print()
try:
    while True:
        choice = input("[Root@Jancok]: ")
        if choice == '1':
            print("[MODULE] - ProxyLess Dorker.")
            print()
            dork = input("Dork: ")
            print()
            print("""
                select your site, all for global | for country search in,de,fr type directly without .
                putting bogus shit will waste your time.
            """)
            print()
            country = input("Country: ")
            if country == 'all':
                dork_new = dork
            else:
                dork_new = dork+' site:'+country
            # Perform anti public actions here
            pages_ = input("Pages [Note: Bing may have limited results]: ")
            os.system('cls')

            dorker(dork_new,int(pages_),False).start()
            break

        elif choice == '2':
            print("[MODULE] - IP Url Grabber.")
            print()
            print('EXAMPLE - [www.facebook.com, facebook.com] exclude protocols ie, https/http')
            print()
            url = input("Url: ")
            if 'http' in url:
                fixing_url = url.split('/')[2]
                new_url = fixing_url
            else:
                new_url = url

            sites_from_ip(new_url,1,1).start()


        elif choice == '3':
            print("[MODULE] - IP Url Grabber Bulk.")
            print()
            print('Enter File Name & Extension of Proxies.')
            print()
            file_location = input("File: ")
            opened_file = open(file_location,).readlines()
            fresh_lines_proxies = [items.rstrip()for items in opened_file]
            proxies_len = len(fresh_lines_proxies)
            rotation = 0
            for lines in fresh_lines_proxies:
                rotation += 1
                sites_from_ip(lines,proxies_len,rotation).start()

        elif choice == '4':
            print("[MODULE] - Sites to Ip [CONVERTOR].")
            print()
            print('Enter site list.')
            print()
            file_location = input("File: ")
            opened_file = open(file_location, ).readlines()
            fresh_lines_sites = [items.rstrip() for items in opened_file]
            sites_len = len(fresh_lines_sites)
            rotation = 0
            for lines in fresh_lines_sites:
                rotation += 1
                simplified_ = lines.split('/')[2]
                ip_grabber(simplified_,sites_len,rotation)

        elif choice == '5':
            print("[MODULE] - Sites Identifier [THREADED].")
            print()
            print('Enter site list.')
            print()
            file_location = input("File: ")
            cms_checker(file_location).thread()



        else:
            continue
except KeyboardInterrupt:
    print("\n")
    print("[Keyboard Interrupt detected] ****** Exiting.")
    print(" ~ Bye.")

# Author: facebook.com/bakbakblabla