#/usr/bin/python

import requests
from ast import literal_eval as d
from sys import exit

user_agent = { "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" }
url = "https://domains.yougetsignal.com/domains.php"
junk = "=" *70

print """%s
[+] Author	: Bayu Fedra	
[+] Facebook	: Bayu Fedra
[+] Instagram	: bayufedraa
[+] Github	: https://github.com/B3yeZ/
%s""" %(junk, junk)


try:
	target = raw_input("[+] Target	: ")
	try:
		try:
			form = { "remoteAddress" : "{0}".format(target), "key" : "" }
			req = requests.post(url, headers=user_agent, data=form, timeout=15)
			res = d(req.text)
		except:
			print "[-] Please Check  your internet connections..."
			exit(0)
	
		if res["status"] == "Success":
			print ""
			print "[+] Target		:", res["remoteAddress"]
			print "[+] IP			:", res["remoteIpAddress"]
			print "[+] Status		:", res["status"]
			print "[+] Date and Time	:", res["lastScrape"]
			print "[+] Results Method	:", res["resultsMethod"]
			print "[+] Domain Count	:", res["domainCount"]
			print ""
			
			for i in range(len(res["domainArray"])):
				print "[+] Domain Reversed %d	: %s" %(i+1, res["domainArray"][i][0])
		
		elif res["status"] == "Fail":
			if "Invalid remote address" in res["message"]:
				print "[+] Status		:", res["status"]
				print "[+] Message		:", res["message"]
				print ""
				print "[+] Try using www. or remove http:// or try other domain format"
			
			elif "check limit reached for" in res["message"]:
				print "[+] Status		:", res["status"]
				print "[+] Message		:", res["message"]
				print ""
				print "[+] Try to change your IP Address"
			else:
				print "[+] Status		:", res["status"]
				print "[+] Message		:", res["message"]
			
		else:
			print "[+] Status		:", res["status"]

	except KeyError:
		print "\n\n[-] Error, Domain/IP Address is incorrect! or can reversed or check your connections"
		print "[-] Try using www. or remove http:// or try other domain format"
		print "[-] If you check many time in one day, you will get limit"
		
except KeyboardInterrupt:
	print "\n[+] Closing the program..."
