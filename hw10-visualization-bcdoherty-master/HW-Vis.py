# Import statements
import unittest
import sqlite3
import matplotlib.pyplot as plt

## [PART 1]
# Finish writing the function getDayDict which takes a database cursor and returns a 
# dictionary that has the days of the weeks as the keys (using "Sun", "Mon", "Tue", 
# "Wed", "Thu", "Fri", "Sat") and the number of tweets on the named day as the values
#
# cur - the database cursor
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
## [Part 2]
# Finish writing the function drawBarChart which takes the dictionary and draws a bar 
# chart with the days of the week on the x axis and the number of tweets on the named day on 
# the y axis.  The chart must have an x label, y label, and title.  Save the chart to 
# "bar.png" and submit it on canvas.  
#
# dayDict - a dictionary with the days of the week and the number of tweets per day
#comment
def drawBarChart(dayDict):
	x = dayDict.keys()
	y = dayDict.values()
	plt.bar(x, y)
	plt.xlabel('Day of the Week')
	plt.ylabel('Number of TWeets')
	plt.savefig('bar.png')

## [Part 3]
## Create unittests to test the function
# Finish writing the unittests.  Write the setUp function which will create the database connection 
# to 'tweets.sqlite' and the cursor.  Write the tearDown function which closes the database connection.  
# Write the test_getDayDict function to test getDayDict by comparing the returned dictionary to the 
# expected value.  Also call drawBarChart in test_getDayDict.comment
class TestHW10(unittest.TestCase):
	def setUp(self):
		self.conn = sqlite3.connect('tweets.sqlite')
		self.cur = self.conn.cursor()
	def test_getDayDict(self):
		dayDict = getDayDict(self.cur)
		self.assertEqual(dayDict['Sunday'], 0)
		self.assertEqual(dayDict['Monday'], 69)
		self.assertEqual(dayDict['Tuesday'], 77)
		self.assertEqual(dayDict['Wednesday'], 90)
		self.assertEqual(dayDict['Thursday'], 0)
		self.assertEqual(dayDict['Friday'], 0)
		self.assertEqual(dayDict['Saturday'], 0)
		drawBarChart(dayDict)
	def tearDown(self):
		self.conn.close()
# run the main method
if __name__ == "__main__":
    unittest.main(verbosity=2)
