Crawling Craigslist

To set up:

	1. git clone https://github.com/purple-goblin/crawling-craigslist
	2. cd crawling-craigslist
	3. python clsearch.py

To customize the search:

	1. Perform a search on craigslist.org and note the URL. For example, if
	   you search for part-time telecommuting web-related jobs in Portland, 
	   you'll see a URL like this:

	   https://portland.craigslist.org/search/web?query=+&is_telecommuting=1
	   &is_parttime=1

	2. Copy everything in the URL after "craigslist.org/"
	   E.g.: search/web?query=+&is_telecommuting=1&is_parttime=1

	3. Open the script clsearch.py.

	4. Paste what you copied into the query variable.

	5. Run the script from the command line.

	SYNTAX: python clsearch.py
