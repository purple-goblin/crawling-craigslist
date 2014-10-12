# Crawling Craigslist

To set up:

* git clone https://github.com/purple-goblin/crawling-craigslist
* cd crawling-craigslist

To customize the search:

* Perform a search on craigslist.org and note the URL. For example, if you search for part-time telecommuting web-related jobs in Portland, you'll see a URL like this:

```
https://portland.craigslist.org/search/web?&is_telecommuting=1&is_parttime=1
```

* Copy everything in the URL after "craigslist.org/"
* Open the script clsearch.py.
* Paste what you copied into the query variable.
* Run the script from the command line.

```
SYNTAX: python clsearch.py
```
