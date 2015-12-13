#!/usr/bin/python

import webbrowser, os, sys, requests
from bs4 import BeautifulSoup

# Replace the value of query with the URL string as described in the 
# README file. For example:
#
# query = 'search/web?is_telecommuting=1&is_parttime=1'


query = 'search/wri?employment_type=2&query=technical+writer'


# create initial HTML tags and write them to output file
beginning = """
<html><title>Craigslist Search</title>
 <body>
   <h1>Custom Craigslist Search</h1>"""

with open('out.htm','a') as out:
	out.write(beginning)

# open list of all subdomains
with open('subdomains.txt','r') as f:
	subdomains = f.readlines()

# query each subdomain and build list of jobs
for sub in subdomains:
	sub = sub.strip()
	sys.stdout.write('Searching ' + sub + '.craigslist.org ...')

	# build the search url, send request, and parse results
	url     = 'http://' + sub + '.craigslist.org/' + query
	headers = {'User-agent': 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'}
	req     = requests.get(url,headers=headers)
	soup    = BeautifulSoup(req.text)

	if soup('p',class_="row"):
		para = soup('p',class_="row")
	else:
	# if there are no matches at all, break out of the current loop
		sys.stdout.write("  no matches found\n")
		continue

	# if the previous sibling of the first item is h4, this is the NEARBY
	# section (which we don't want), so break out of the current loop
	if para[0].previous_sibling.previous_sibling:
		if para[0].previous_sibling.previous_sibling.name == "h4":
			sys.stdout.write("  no matches found\n")
			continue
	
	# otherwise, we've found matches
	sys.stdout.write("  found matches!\n")
	matches = []
	a = '<a href="' + url + '">' + sub + '</a>'
	city = '<br><h3>Matches found in ' + a + ':</h3>'
	matches.append(city)

	for p in para:
		job = p.a['href']
		p('a')[1]['href'] = 'https://' + sub + '.craigslist.org' + job
		matches.append(p)

	with open('out.htm','a') as out:
		for match in matches:
			line = str(match)
			out.write(line)

ending = '</body></html>'
with open('out.htm','a') as out:
	out.write(ending)

results = 'file://localhost' + os.getcwd() + '/out.htm'
webbrowser.open(results, new=2)
