#!/usr/bin/python

import webbrowser, os, sys, urllib2
from bs4 import BeautifulSoup

# Replace the value of query with the URL string as described in the 
# README.txt file.                                  
# 
# For example:
#
# query = 'search/web?query=+&is_telecommuting=1&is_parttime=1'
#


query = ''


beginning = """
<html><title>Craigslist Search</title>
 <body>
   <h1>Custom Craigslist Search</h1>"""

with open('out.htm','a') as out:
	out.write(beginning)

with open('subdomains.txt','r') as f:
	subdomains = f.readlines()

for sub in subdomains:
	sub = sub.strip()
	print 'Searching ' + sub + '.craigslist.org ...'
	url = 'http://' + sub + '.craigslist.org/' + query
	headers = {'User-agent': 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'}
	req = urllib2.Request(url, None, headers)
	reply = urllib2.urlopen(req).read()

	soup = BeautifulSoup(reply)
	if soup('div')[10].p:
		para = soup('div')[10].p
	else:
	# break out of loop if we don't find a match for soup('div')[10].p
		continue

	# if para has a previous sibling, there are no local matches	
	if para.previous_sibling.previous_sibling:
		continue

	matches = []
	a = '<a href="' + url + '">' + sub + '</a>'
	city = '<br><h3>Matches found in ' + a + ':</h3>'
	matches.append(city)

	while True:
		path = para.span.a['href']
		para.span.a['href'] = 'http://' + sub + '.craigslist.org' + path
		matches.append(str(para))

		try:
			para = para.next_sibling.next_sibling
		except:
			break
		if not para:
			break
		if not para.next_sibling.next_sibling:
			break
		if para.next_sibling.next_sibling == ' ':
			break
		if para.next_sibling.next_sibling.name != 'p':
			break
			
	with open('out.htm','a') as out:
		out.writelines(matches)

ending = '</body></html>'
with open('out.htm','a') as out:
	out.write(ending)

results = 'file://localhost' + os.getcwd() + '/out.htm'
webbrowser.open(results, new=2)
