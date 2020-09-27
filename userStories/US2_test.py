import datetime 
import unittest
import sys
sys.path.append("./userStories")
from US2 import dateCompare

class testDateCompare(unittest.TestCase):
    
    
    def testDate(self):
        presentDate = datetime.datetime.now()
        # print(presentDate)
        date1 = datetime.datetime(2020,9,1)
        date2 = datetime.datetime(2018,5,3)
        date3 = datetime.datetime(1999,1,1)
        self.assertEqual(dateCompare(presentDate, date1), False)
        self.assertEqual(dateCompare(date1, presentDate), True)
        self.assertEqual(dateCompare(presentDate, presentDate), False)
        self.assertEqual(dateCompare(date3, date2), True) 

    def test_values(self):
        date1 = datetime.datetime(2020,9,1)
        self.assertRaises(ValueError, dateCompare, 1,2)
        self.assertRaises(ValueError, dateCompare, date1, 2)
        self.assertRaises(ValueError, dateCompare,1,2 )

if __name__ == '__main__':
    t = testDateCompare()
    t.testDate()
    t.test_values()
