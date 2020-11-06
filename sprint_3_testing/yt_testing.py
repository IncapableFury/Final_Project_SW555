import unittest

from models.Individual import Individual
from models.Family import Family
from models.Gedcom import Gedcom

SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
                    "DIV", "DATE", "HEAD", "TRLR", "NOTE"}


G1 = Gedcom('../testing_files/right.ged', SUPPORT_TAGS)
G2 = Gedcom('../testing_files/wrong.ged', SUPPORT_TAGS)

class sprint3Test(unittest.TestCase):

    #List all deceased individuals in a GEDCOM file
    def test_US29_list_deceased(self):
        self.assertEqual(G1.listDeceased().len(),5 )
        self.assertNotEqual(G1.listDeceased().len(),3 )
        deceasedPeople = []
        for indi in deceasedPeople:
            self.assertIn(indi, G1.listDeceased())

    #List all living married people in a GEDCOM file
    def test_US30_list_living_married(self):
        self.assertEqual(G1.listLivingMarried().len(),5 )
        self.assertNotEqual(G1.listLivingMarried().len(),3 )
        marriedProple = []
        for indi in marriedProple:
            self.assertIn(indi, G1.listLivingmarried())

    #List all living people over 30 who have never been married in a GEDCOM file
    def test_US31_list_living_single(self):
        self.assertEqual(G1.listLivingSingle().len(),5 )
        self.assertNotEqual(G1.listLivingSingle().len(),3 )
        singlePeople = []
        for indi in singlePeople:
            self.assertIn(indi, G1.listLivingSingle())

    #List all multiple births in a GEDCOM file
    def test_US32_list_multiple_births(self):
        self.assertEqual(G1.listMultipleBirths().len(),4 )
        MultipleBirths = []
        for birt in MultipleBirths:
            self.assertIn(birt, G1.listMultipleBirths())

    #List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
    def test_US33_list_orphans(self):

        self.assertEqual(G1.listOrphans().len(),4)
        OrphansPeople = []
        for indi in OrphansPeople:
            self.assertIn(indi, G1.listOrphans())

    #List all couples who were married when the older spouse was more than twice as old as the younger spouse
    def test_US34_list_large_age_differences(self):
        self.assertEqual(G1.listLargeAgeDifferences().len(),4 )
        ageDifferences = []
        for birt in ageDifferences:
            self.assertIn(birt, G1.listLargeAgeDifferences())

    #List all people in a GEDCOM file who were born in the last 30 days
    def test_US35_list_recent_births(self):

        self.assertEqual(G1.listRecentBirths().len(),5 )
        self.assertNotEqual(G1.listRecentBirths().len(),3 )
        bornPeople =[]
        for indi in bornPeople:
            self.assertIn(indi, G1.listRecentBirths())

if __name__ == '__main__':
    unittest.main()
    pass
