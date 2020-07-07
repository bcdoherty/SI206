from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import unittest

def getSumSpans(url):
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")

	count = 0
	spans = soup.find_all('span')
	for x in range(len(spans)):
		span = spans[x]
		num = int(span.get_text())
		count = count + num
	print(count)

def followLinks(url, numAnchor, numTimes):
	""" Repeat for numTimes. Find the url at numAnchor position (the first link is at position 1) at
	the current url and use that as the new url
	return the text in the a tag from the last url that you process

	url -- a uniform resource locator - address for a web page
	numAnchor -- the position of the anchor (a tag) you are looking at on the page - the first link is position 1
	numTimes -- the number of times to repeat the process of finding the new url
	"""
	numAnchor = numAnchor - 1
	for x in range(numTimes):
		ctx = ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE
		html = urlopen(url, context=ctx).read()
		soup = BeautifulSoup(html, "html.parser")

		a = soup.find_all('a')
		link = a[numAnchor]
		text = link.get_text()
		href = link.get('href')
		url = href
	print(text)
