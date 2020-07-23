import re
import socket
import requests
import urllib2
import urllib
import os
import sys
import time
import cookielib
from bs4 import BeautifulSoup
from platform import system

banner =""" 
    _    _      Coded By : W0rmC0der
   (o)--(o)     Tools By : W0rmC0der 
  /.______.\    Mass Bing - Mass Dorker - Converter IP to Sites
  \________/    Github.com/fstreitzia/
 ./        \.   
( .        , )  
 \ \_\/\//_/ /
  ~~  ~~  ~~                                                                   
"""
print (banner)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
print ("""
1. Bing Dorker 
2. Web List From IP
3. IP From Weblist
4. HTTP Weblist
5. Scanner Clear
""")

nels = raw_input("root@Jancok:~# ")


class males():
	#def alldomains(self):
		#iya = raw_input("List@Dork:~#  ")
		#iya = open(iya, 'r')
		#dom = ['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao',
				#'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb',
				#'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo',
				#'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd',
				#'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr',
				#'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do',
				#'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi',
				#'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf',
				#'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs',
				#'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu',
				#'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'is', 'it',
				#'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn',
				#'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk',
				#'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me',
				#'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr',
				#'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc',
				#'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz',
				#'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn',
				#'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru',
				#'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj',
				#'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy',
				#'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm',
				#'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug',
				#'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi',
				#'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'za', 'zm', 'zw', 'com',
				#'net', 'org', 'biz', 'gov', 'mil', 'edu', 'info', 'int', 'tel',
				#'name', 'aero', 'asia', 'cat', 'coop', 'jobs', 'mobi', 'museum',
				#'pro', 'travel']
		#for udah in iya:
			#tam = []
			#page = 1
			#while page < 159:
				#bing = "http://www.bing.com/search?q="+udah+' site:.'+dom+"+&count=50&first="+str(page)
				#rek = requests.get(bing,verify=False,headers=headers)
				#eee = rek.content
				#nemu = re.findall('<h2><a href="(.*?)"', eee)
				#for o in nemu:
					#i = o.split('/')
					#if (i[0]+'//'+i[2]) in tam:
						#pass
					#else:
						#tam.append(i[0]+'//'+i[2])
						#print '[>>]',(i[0]+'//'+i[2])
						#with open('AllDomains.txt', 'a') as s:
							#s.writelines((i[0]+'//'+i[2])+'\n')
				#pages = pages+50

	def randomdomen(self):
		bo = raw_input("List@Dork:~# ")
		bo = open(bo, 'r')
		for oaja in bo:
			sa = []
			tu = 1
			while tu < 159:
				bing0 = "http://www.bing.com/search?q="+oaja+"+&count=50&first="+str(tu)
				iyoo = requests.get(bing0,verify=False,headers=headers)
				rrr = iyoo.content
				sip = re.findall('<h2><a href="(.*?)"', rrr)
				for i in sip:
					o = i.split('/')
					if (o[0]+'//'+o[2]) in sa:
						pass
					else:
						sa.append(o[0]+'//'+o[2])
						print '[>>]',(o[0]+'//'+o[2])
						with open('Random.txt', 'a') as s:
							s.writelines((o[0]+'//'+o[2])+'\n')
				tu = tu+50


	def grabip(self):
		ooke = raw_input("List@IP:~# ")
		ooke = open(ooke, 'r')
		for zzz in ooke:
			bo = []
			lonk = 1
			while lonk < 299:
				bingung = "http://www.bing.com/search?q=IP%3A"+zzz+"+&count=50&first="+str(lonk)
				iyagw = requests.get(bingung,verify=False,headers=headers)
				gans = iyagw.content
				ya = re.findall('<h2><a href="(.*?)"', gans)
				for z in ya:
					o = z.split('/')
					if (o[0]+'//'+o[2]) in bo:
						pass
					else:
						bo.append(o[0]+'//'+o[2])
						print '[>>]',(o[0]+'//'+o[2])
						with open('Grab.txt','a') as s:
							s.writelines((o[0]+'//'+o[2])+'\n')
				lonk = lonk+50

	def http(self):
		kep = raw_input("List@Sites:~# ")
		kep = open(kep, 'r')
		for i in kep:
			i = i.rstrip()
			print("http://"+i)
			with open('HTTP.txt', 'a') as o:
				o.write("http://" + i + '\n')
		print("[>>] D0N3! Check HTTP.txt")

	def clean(self):
		print ("URL LIST WITHOUT HTTP://")
		oh = raw_input("List@Sites:~#")
		oh = open(oh, 'r')
		for i in oh:
			i = i.rstrip()
			with open("Cleaner.txt", 'a') as f:
				f.write(i.split('/')[0] + '\n')
		print('[>>] D0N3! Check Cleaner.txt')

	def getip(self):
		hooh = raw_input("List@IP:~# ")
		hooh = open(hooh, 'r')
		for i in hooh.readlines():
			done = i.rstrip()
			try:
				done = done.rstrip()
				bine = requests.get('http://api.hackertarget.com/reverseiplookup/?q='+done)
				if '.' in bine.content:
					print ("[>>]" + (bine.content))
					with open('site.txt', 'a') as o:
						o.writelines(bine.content + '\n')
				else:
					pass

			except:
				pass


dahah = males()
if nels == '1':
	dahah.randomdomen()
elif nels == '2':
	dahah.grabip()
elif nels == '4':
	dahah.http()
elif nels == '5':
	dahah.clean()
elif nels == '3':
	dahah.getip()
else:
	print("?")
	