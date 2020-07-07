## SI 206 F18 - Project 2

## COMMENT HERE WITH:
## Your name: Bridget Doherty
## Anyone you worked with on this project and how you worked together
## You can not share code, but can share ideas
###########

## Import statements
import unittest
import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import codecs

## PART 1  - Complete grab_headlines
## INPUT: soup - the soup object to process
## Grab the headlines from the "Most Read" section
## and return them in a list
def grab_headlines(soup):
    
    # get the most read div
    mostReadDiv = soup.find('div', 'view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266')
    
    # get the ordered list from that div
    ol = mostReadDiv.find('ol')

    # get the links from the ordered list div
    links = ol.find_all('a')
    headlines = []
    for link in links:
	    headline = link.get_text()
	    headlines.append(headline)
   
    # return the headlines
    return(headlines)
    
## PART 2 Complete a function called get_headline_dict. It will take a soup object and return a dictionary
## with each story headline as a key and each story url as the value
## INPUT: soup - the soup object
## OUTPUT: Return - a dictionary with each story headline as the key and the story url as the value
def get_headline_dict(soup):
    
    # create the empty dictionary
    dic = {}
    
    # get the story wrap divs
    div = soup.find_all('div', 'storywrap')

    # get the short headline
    for x in range(len(div)):
    	divItem = div[x]
    	shortHeadline = divItem.find('div', 'views-field views-field-field-short-headline')
    	link = shortHeadline.find('a')
    	url = link.get('href')
    	text = link.get_text()
    	dic[text] = url
    return(dic)
    
## PART 3 Define a function called get_page_info. It will take a soup object for a story
## and return a tuple with the title, author, date, and the number of paragraphs
## in the body of the story
## INPUT: soup - the soup object
## OUTPUT: Return - a tuple with the title, author, date, and number of paragraphs
def get_page_info(soup):
    
    # get the title
    titleDiv = soup.find('div', 'panel-pane pane-node-title')
    titleH2 = titleDiv.find('h2')
    title = titleH2.get_text()
    
    # get the date
    dateDiv = soup.find('div', 'panel-pane pane-node-created')
    dateDiv = dateDiv.find('div', 'pane-content')
    date = dateDiv.get_text()#.strip()
    
    # get the author
    authorDiv = soup.find('div', 'view view-byline-for-storypage view-id-byline_for_storypage view-display-id-panel_pane_1 view-dom-id-98a269661184a82fd2a2480bc9d2a425')
    a = authorDiv.find('a')
    author = a.get_text()#.strip()
    
    # get the number of paragraphs
    soupDiv = soup.find('div', 'panel-pane pane-entity-field pane-node-body p402_premium')
    pLst = soupDiv.find_all('p')
    p = len(pLst)

    # return the tuple
    t = (title, date, author, p)
    return(t)




















"""ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urlopen('xfile:///Users/bridgetdoherty/projects/SI206/project-2-bcdoherty/news1.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")"""
text = codecs.open("newsStory1.html", 'r', 'utf-8')
soup = BeautifulSoup(text, 'html.parser')


#print(grab_headlines(soup))
print(get_page_info(soup))









