from __future__ import print_function
from apiclient import discovery
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from oauth2client import tools
import gmail_info
import json
import sqlite3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np 

# this link helps http://wescpy.blogspot.com/2015/08/accessing-gmail-from-python-plus-bonus.html
# video to watch https://www.youtube.com/watch?v=L6hQCgxgzLI&feature=youtu.be&list=PLOU2XLYxmsILOIxBRPPhgYbuSslr50KVq&index=11&linkId=16190771
# api reference: https://developers.google.com/gmail/api/v1/reference/users/messages

api_key = gmail_info.api_key
service = discovery.build('gmail', 'v1', developerKey=api_key)
scope = 'https://www.googleapis.com/auth/gmail.readonly'
client_secret = 'client_secret.json'
store = file.Storage('storage.json')
credz = store.get()
if not credz or credz.invalid:
	flow = client.flow_from_clientsecrets(client_secret, scope)
	credz = tools.run_flow(flow, store)
gmail = build('gmail', 'v1', http=credz.authorize(Http()))

#create table
conn = sqlite3.connect('gmail.sqlite')
cur = conn.cursor()
cur.execute('''
			CREATE TABLE IF NOT EXISTS Gmail
			(class TEXT, sender TEXT, subject TEXT NOT NULL UNIQUE, recieved TIMESTAMP)''')

#searching inbox and pulling data
def gmailDB(search, cur, conn):
	threads = gmail.users().messages().list(userId='me', maxResults=50, q=search).execute().get('messages',[])
	for thread in threads:
		tdata = gmail.users().messages().get(userId='me', id=thread['id']).execute()
		tdataHeaders = tdata['payload']['headers']
		for dic in tdataHeaders:
			if dic['name'] == 'Subject':
				subject = dic['value']
			if dic['name'] == 'From':
				sender = dic['value']
			if dic['name'] == 'Date':
				date = dic['value']
		cur.execute('INSERT or IGNORE INTO Gmail (class, sender, subject, recieved) VALUES (?,?,?,?)',
			(search, sender, subject, date))
	conn.commit()
#gmailDB('301', cur, conn)
#gmailDB('310', cur, conn)
#gmailDB('206', cur, conn)
#gmailDB('300', cur, conn)

#getting date and class from database; storing data as a list of dictionaries [{class:date}]
def dataProcess(cur, SIclass):
	cur.execute("SELECT class, recieved, subject FROM Gmail WHERE class =="+ SIclass)
	dic = {}
	lst = []
	for row in cur:
		recieved = str(row[1])
		subject = str(row[2])
		dic[subject] = recieved
		lst.append(dic)
	return(lst)	
		
lst310 = dataProcess(cur, '310')
lst206 = dataProcess(cur, '206')
lst301 = dataProcess(cur, '301')
lst300 = dataProcess(cur, '300')
conn.close()
#this  will calculate the data the amount of emails from each class and write it to a text file

def writeData(classLst, clss):
	try:
		file = open('data.txt', 'r')
		text = file.read()
		file.close()
		
		file = open('data.txt', 'w')
		file.write(text)
		file.write('SI '+ clss + '\n')
		file.write('Number of mentions: ' +str(len(classLst)) +'\n \n')
		file.close()

	except: 
		file = open("data.txt","w+")
		file.write('SI '+ clss + '\n')
		file.write('Number of mentions: ' +str(len(classLst)) +'\n \n')
		file.close()
writeData(lst310)
writeData(lst301)
writeData(lst300)
writeData(lst206)
#returns a dictionary of months
def messagesByMonth(classLst):
	timestamps = list(classLst[0].values())
	monthNames = {}
	for time in timestamps:
		stampLst = time.split()
		month = stampLst[2]
		if month in monthNames:
			count = monthNames[month]
		else:
			count = 0
		monthNames[month] = count + 1
	return(monthNames)

months310 = messagesByMonth(lst310)
months301 = messagesByMonth(lst301)
months206 = messagesByMonth(lst206)
months300 = messagesByMonth(lst300)

#create bar graph
def barGraph(lst310, lst301, lst300, lst206):
	y = (len(lst310), len(lst301), len(lst300), len(lst206))
	x = ('SI310', 'SI301', 'SI300', 'SI206')
	barlst = plt.bar(x, y)
	barlst[0].set_color('#ff9900')
	barlst[1].set_color('#ff3366')
	barlst[2].set_color('#33cc99')
	barlst[3].set_color('#66ccff')
	plt.xlabel('class')
	plt.ylabel('mentions')
	plt.savefig('barGraph.png')
	plt.show()

def lineGraph(months310, months301, months206, months300):
	x1 = list(months310.keys())
	x2 = list(months301.keys())
	x3 = list(months300.keys())
	x4 = list(months206.keys())
	x5 = x1 + x2 + x3 + x4
	x = []
	for month in x5:
		if month in x:
			count = 0
		else:
			x.append(month)
	allMonths = {}
	for month in x:
		allMonths[month] = 0

	for x in list(allMonths.keys()):
		if x in list(months310.keys()):
			months310 = months310
		else:
			months310[x] = 0

		if x in list(months301.keys()):
			months301 = months301
		else:
			months301[x] = 0

		if x in list(months300.keys()):
			months300 = months300
		else:
			months300[x] = 0

		if x in list(months206.keys()):
			months206 = months206
		else:
			months206[x] = 0

	x = list(allMonths.keys())
	y1 = list(months310.values())
	y2 = list(months301.values())
	y3 = list(months300.values())
	y4 = list(months206.values())

	plt.plot(x, y1, label = 'SI310')
	plt.plot(x, y2, label = 'SI301')
	plt.plot(x, y3, label = 'SI300')
	plt.plot(x, y4, label = 'SI206')
	plt.xlabel('month')
	plt.ylabel('mentions')
	plt.grid()
	plt.legend()
	plt.savefig('lineGraph.png')
	plt.show()
lineGraph(months310, months301, months206, months300)
barGraph(lst310, lst301, lst300, lst206)
"""def newMonthDics(months310, months301, months206, months300):
	x1 = list(months310.keys())
	x2 = list(months301.keys())
	x3 = list(months300.keys())
	x4 = list(months206.keys())
	x5 = x1 + x2 + x3 + x4
	x = []
	for month in x5:
		if month in x:
			count = 0
		else:
			x.append(month)
	allMonths = {}
	for month in x:
		allMonths[month] = 0

	for x in list(allMonths.keys()):
		if x in list(months310.keys()):
			months310 = months310
		else:
			months310[x] = 0

		if x in list(months301.keys()):
			months301 = months301
		else:
			months301[x] = 0

		if x in list(months300.keys()):
			months300 = months300
		else:
			months300[x] = 0

		if x in list(months206.keys()):
			months206 = months206
		else:
			months206[x] = 0"""
lineGraph(months310, months301, months206, months300)

#this code finds the the headers. this is where you access the content like date, sender, recipient, maybe text...
"""tdata = gmail.users().messages().get(userId='me', id=threads[0]['id']).execute()

tdataHeaders = tdata['payload']['headers']

for stuff in range(len(tdataHeaders)):
	print(stuff)
	print(tdataHeaders[stuff])
	print("------------------------------")
	print('\n')"""




"""for thread in threads:
	nmsgs = len(tdata['messages'])
	if nmsgs > 2:
		msg = tdata['messages'][0]['payload']
		subject = ''
		for header in msg['headers']:
			if header['name'] == 'Subject':
				subject = header['value']
				break
		if subject:
			print ('%s (%d msgs)' % (subject, nmsgs))"""

# timestamp example: {'300': 'Tue, 4 Sep 2018 13:22:16 +0000'}
















