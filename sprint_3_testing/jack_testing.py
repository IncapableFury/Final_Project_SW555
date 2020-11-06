import unittest

from models.Individual import Individual
from models.Family import Family
from models.Gedcom import Gedcom

SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
                    "DIV", "DATE", "HEAD", "TRLR", "NOTE"}

###
###Making the GEDCOM files
###
# right.ged with 5 recently deceased people in the past 30 days
# 7 recently deceased people's relatives. recently deceased in past 30 days
# 6 people with upcoming birthdays in 30 days
# 4 people with upcoming anniversaries in 30 days(2 couples)
# errors occur on line 20 and 25
# one or two date entries with missing information( missing day or missing month)

#wrong.ged with invalid dates, e.g(2/30/2020)
#error on line 15

G1 = Gedcom('../testing_files/mock-family.ged', SUPPORT_TAGS)
G1.parse()

# G2 = Gedcom('../testing_files/wrong.ged', SUPPORT_TAGS)

class sprint3Test(unittest.TestCase):

    #list all people in a GEDCOM file who died in the last 30 days
    # def test_ListRecentDeaths(self):
    #
    #     self.assertEqual(G1.listRecentDeaths().len(), 5)
    #     self.assertNotEqual(G1.listRecentDeaths().len(), 3)
    #
    #     #manually input deceased people and append to the array
    #     deceasedProple =[]
    #     for indi in deceasedProple:
    #         self.assertIn(indi, G1.listRecentDeaths())
    #
    # #list all living spouses and descendants of people in the GEDCOM who died in the last 30 days
    # def test_listRecentSurvivors(self):
    #     self.assertEqual(G1.listRecentSurviors().len(),7)
    #     self.assertNotEqual(G1.listRecentSurviors().len(), 8)
    #     # manually input deceased people's relatives and append to the array
    #     deceasedProple = []
    #     for indi in deceasedProple:
    #         self.assertIn(indi, G1.listRecentSurviors())
    #
    #
    # #list all living people in a GEDCOM file whose birthdays occur in the next 30 days
    # def test_listUpcomingBirthdays(self):
    #     self.assertEqual(G1.listUpcomingBirthdays().len(),6)
    #     #manually input people with birthdays
    #     birthdayPeople =[]
    #     for indi in birthdayPeople:
    #         self.assertIn(indi, G1.listUpcomingBirthdays())

    # list all living people in a GEDCOM file whose marriage anniversaries occur in the next 30 days
    def test_UpcomingAnniversaries(self):
        self.assertEqual(len(G1.list_upcoming_anniversaries()),4)
        # #manually input individuals who have anniversaries coming up
        # AnniversaryIndi = []
        # for indi in AnniversaryIndi:
        #     self.assertIn(indi, G1.list_upcoming_anniversaries())

    # # list line numbers from GEDCOM source file when reporting errors
    # def test_includeInputLineNumbers(self):
    #
    #     self.assertEqual(G1.include_InputLine_Numbers().len(), 2)
    #
    #     self.assertTrue(G1.include_InputLine_Numbers() == ['20','25'])
    #
    #     self.assertTrue(G2.include_InputLine_Numbers() == ['15'])
    #
    # # Accept and use dates without days or without days and months
    # def test_IncludePartialDates(self):
    #     self.assertTrue(G1.IncludePartialDates())
    #
    #
    # # All dates should be legitimate dates for the months specified(e.g. 2/30/2015 is not legitimate)
    # def test_RejectIllegitimateDates(self):
    #     self.assertTrue(G1.rejectIllegitimateDates())
    #     self.assertFalse(G2.rejectIllegitimateDates())

if __name__ == '__main__':
    unittest.main()
    pass