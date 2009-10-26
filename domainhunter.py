#!/usr/bin/env python
# Domain Hunter									 -- Abhishek Mishra
# 	usage -
#		$ python domainhunter.py < wordlist.txt

from sys import stdin

def domainSearch(domain):
	import httplib
	  
	baseurl = "ajaxwhois.com"
	conn = httplib.HTTPConnection(baseurl)
    
	try:
		conn.request("GET", "/lookup/?d=" + domain)
		response = conn.getresponse()
		data = response.read()
	
		if (data.find("\"a\":true") != -1):
			return True
		else:
			return False
	except:
		print " connection error ... ",

tlds = ['.net', '.com', '.org'];
# you can modify tlds to suit your needs,
# complete list of Google Apps supported tlds -
# tlds = ['.com', '.net', '.org', '.net', '.biz', '.info'];
# more injection of .coms for quality

if __name__ == '__main__':
	search = stdin.readline()

	while (search):
		for word in search.split():
			print (word + ":").ljust(30,' '),

			for tld in tlds:
				if ( domainSearch(word + tld) ):
					print "[+]" + tld + "\t",
				else:
					print "[X]" + tld + "\t",
			print
		search = stdin.readline()
