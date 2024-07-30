#IMPORTING
import sys
import dns.resolver

resolver = dns.resolver.Resolver()

#ARGS
try:
	target = sys.argv[1]
	wordlist = sys.argv[2]
except:
	print("Usage: python dnsbrute.py domain wordlist.txt")
	sys.exit()

#WORDLIST FILE
try:
	with open(wordlist, "r") as arq:
		subdomains = arq.read().splitlines()
except:
	print("Error, can't open the file")
	sys.exit()

#SUBDOMAIN
for subdomain in subdomains:
	try:
		sub_target = "{}.{}".format(subdomain, target)
		results = resolver.resolve(sub_target, "A")
		for result in results:
			print("{} -> {}".format(sub_target, result))
	except:
		pass
