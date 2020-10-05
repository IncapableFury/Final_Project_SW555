"""
Test cases go in here
Van comment for second time
"""

import unittest
from models import Individual
from models import Family
from models import Gedcom

class TestTriangles(unittest.TestCase):

    def setUp(self):
        self.ind_1 = Individual.Individual("01")
        self.ind_2 = Individual.Individual("02")
        self.ind_3 = Individual.Individual("03")

        self.fam_1 = Family.Family("01")
        self.fam_2 = Family.Family("02")

    def tearDown(self):
        self.ind_1 = Individual.Individual("01")
        self.ind_2 = Individual.Individual("02")
        self.ind_3 = Individual.Individual("03")

        self.fam_1 = Family.Family("01")
        self.fam_2 = Family.Family("02") 


    def test_marriage_after_14(self):
        with self.assertRaises(ValueError, msg = "No husband || wife || marry date"):
            self.fam_1.marriage_after_14()
        self.fam_1.set_husband(self.ind_1)
        with self.assertRaises(ValueError, msg = "No husband || wife || marry date"):
            self.fam_1.marriage_after_14()
        self.fam_1.set_wife(self.ind_2)
        with self.assertRaises(ValueError, msg = "No husband || wife || marry date"):
            self.fam_1.marriage_after_14()
        self.fam_1.set_marriedDate(["01", "JUN", "2017"])
        with self.assertRaises(ValueError, msg = "No birth Date for husband || wife"):
            self.fam_1.marriage_after_14()
        self.ind_1.set_birthDate(["09", "APR", "1997"])
        self.ind_2.set_birthDate(["19", "DEC", "1997"])
        self.assertTrue(self.fam_1.marriage_after_14())
        self.fam_1.set_marriedDate(["01", "JUN", "2007"])
        self.assertFalse(self.fam_1.marriage_after_14())

    def test_no_bigamy(self):
        self.ind_1.set_birthDate(["09", "APR", "1997"])
        self.ind_2.set_birthDate(["19", "DEC", "1997"])
        self.ind_1.add_to_family(self.fam_1)
        self.fam_1.set_marriedDate(["01", "JUN", "2017"])
        self.assertTrue(self.ind_1.no_bigamy())
        self.fam_2.set_marriedDate(["05", "JUN", "2016"])
        self.ind_1.add_to_family(self.fam_2)
        self.assertFalse(self.ind_1.no_bigamy())
        self.fam_2.set_divorcedDate(("01", "JAN", "2017"))
        self.assertTrue(self.ind_1.no_bigamy())
        self.fam_2.set_divorcedDate(("01", "AUG", "2017"))
        self.assertFalse(self.ind_1.no_bigamy())
        self.fam_1.set_divorcedDate(("01", "DEC", "2018"))
        self.assertFalse(self.ind_1.no_bigamy())
        self.fam_2.set_divorcedDate(("01", "JAN", "2017"))
        self.assertTrue(self.ind_1.no_bigamy())

    def testMarriageBeforeDivorce(self):
        self.ind_1.add_to_family(self.fam_1)
        self.ind_2.add_to_family(self.fam_1)
        self.fam_1.set_marriedDate(["08", "JUN", "2000"])
        self.fam_1.set_divorcedDate(['8', 'SEP', '2009'])
        self.assertTrue(self.fam_1.marriage_before_divorce())
        self.assertEqual(self.fam_1.marriage_before_divorce(), True)
        self.assertNotEqual(self.fam_1.marriage_before_divorce(), False)
        self.assertIsNot(self.fam_1.marriage_before_divorce(), " ")
        self.assertIsNotNone(self.fam_1.marriage_before_divorce())

    def testMarriageBeforeDeath(self):
        self.ind_1.add_to_family(self.fam_2)
        self.ind_2.add_to_family(self.fam_2)
        self.ind_1.set_deathDate(['8', 'SEP', '2010'])
        self.ind_2.set_deathDate(['8', 'SEP', '2011'])
        self.fam_2.set_husband(self.ind_1)
        self.fam_2.set_wife(self.ind_2)
        self.fam_2.set_marriedDate(["08", "JUN", "2000"])
        self.assertTrue(self.fam_2.marriage_before_death())
        self.assertEqual(self.fam_2.marriage_before_death(), True)
        self.assertNotEqual(self.fam_2.marriage_before_death(), False)

    def testInputValidation(self):
        pass


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
