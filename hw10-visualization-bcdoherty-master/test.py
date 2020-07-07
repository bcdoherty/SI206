# Import statements
import unittest
import sqlite3
import twitter_info # still need this in the same directory, filled out
import matplotlib.pyplot as plt

## [PART 1]
# Finish writing the function getDayDict which takes a database cursor and returns a 
# dictionary that has the days of the weeks as the keys (using "Sun", "Mon", "Tue", 
# "Wed", "Thu", "Fri", "Sat") and the number of tweets on the named day as the values
#
# cur - the database cursor

conn = sqlite3.connect('tweets.sqlite')
cur = conn.cursor()

def getDayDict(cur):
	cur.execute('SELECT time_posted FROM tweets')
	sunNum = 0
	monNum = 0
	tueNum = 0
	wedNum = 0
	thuNum = 0
	friNum = 0
	satNum = 0
	for row in cur:
		lst = list(row)
		string = lst[0]
		timeLst = string.split(' ')
		
		day = timeLst[0]
		if day == 'Sun':
			sunNum = sunNum + 1
		elif day == 'Mon':
			monNum = monNum + 1
		elif day == 'Tue':
			tueNum = tueNum + 1
		elif day == 'Wed':
			wedNum = wedNum + 1
		elif day == 'Thu':
			thuNum = thuNum + 1
		elif day == 'Fri':
			friNum = friNum + 1
		else:
			satNum = satNum + 1
	tweetsByDay = {'Sunday':sunNum, 'Monday':monNum, 'Tuesday':tueNum, 'Wednesday':wedNum,'Thursday':thuNum, 'Friday':friNum, 'Saturday':satNum}
	return(tweetsByDay)

tweetsByDay = getDayDict(cur)
print(tweetsByDay)

def drawBarChart(dayDict):
	x = dayDict.keys()
	y = dayDict.values()
	plt.bar(x, y)
	plt.xlabel('Day of Week')
	plt.ylabel('Number of TWeets')
	plt.savefig('bar.png')

drawBarChart(tweetsByDay)





































