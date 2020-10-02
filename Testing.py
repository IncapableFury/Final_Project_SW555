"""
Test cases go in here
Van comment for second time
"""

import unittest
from datetime import date 

from models.Individual import Individual
from models.Family import Family
from models.Gedcom import Gedcom

class TestTriangles(unittest.TestCase):
  
    def testMarriageBeforeDivorce1(self):
        self.assertTrue(marriage_before_divorce(fam1))

    def testMarriageBeforeDivorce2(self):
        self.assertEqual(marriage_before_divorce(fam1), True)

    def testMarriageBeforeDivorce3(self):
        self.assertNotEqual(marriage_before_divorce(fam1), False)

    def testMarriageBeforeDivorce4(self):
        self.assertIsNot(marriage_before_divorce(fam1), " ")

    def testMarriageBeforeDivorce5(self):
        self.assertIsNotNone(marriage_before_divorce(fam1))

    def testMarriageBeforeDeath1(self):
        self.assertTrue(fam2.marriage_before_death())

    def testMarriageBeforeDeath2(self):
        self.assertEqual(fam2.marriage_before_death(), True)

    def testMarriageBeforeDeath3(self):
        self.assertNotEqual(fam2.marriage_before_death(), False)

        
def marriage_before_divorce(Family):
    from datetime import date
    marriage= Family.get_marriedDate()
    divorce= Family.get_divorcedDate()
    timediff = date(*marriage)-date(*divorce)
    if timediff.days <0:
        return True
    print("Error marriage before divorce: Marriage date of "+Family.get_id+" happened after the divorce date.")
    return False

class TestDivorseBeforeDeath(unittest.TestCase):
    def test1(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorcedDate("1 JAN 1999")
        self.assertTrue(family1.divorce_before_death())

    def test2(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorcedDate("1 JAN 2001")
        self.assertFalse(family1.divorce_before_death())
    
    def test3(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorcedDate("1 JAN 2003")
        self.assertFalse(family1.divorce_before_death())
    
    def test4(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorcedDate("1 JAN 2000")
        self.assertTrue(family1.divorce_before_death())
    
    def test5(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorcedDate("1 JAN 2002")
        self.assertFalse(family1.divorce_before_death())
class TestBirthBeforeDeathofParent(unittest.TestCase):
    def test1(self):
        male1=Individual("P01")
        female1=Individual("P02")
        child1=Individual("P03")
        family1=Family("F01")
        family1.add_child(child1)
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        child1.set_birthDate("6 JAN 1998")
        family1.set_husband(male1)
        family1.set_wife(female1)
        self.assertTrue(family1.birth_before_death_of_parents())
    def test2(self):
        male1=Individual("P01")
        female1=Individual("P02")
        child1=Individual("P03")
        family1=Family("F01")
        family1.add_child(child1)
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        child1.set_birthDate("6 JAN 2001")
        family1.set_husband(male1)
        family1.set_wife(female1)
        self.assertRaises(ValueError,family1.birth_before_death_of_parents())
    def test2(self):
        male1=Individual("P01")
        female1=Individual("P02")
        child1=Individual("P03")
        family1=Family("F01")
        family1.add_child(child1)
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        child1.set_birthDate("6 MAR 2000")
        family1.set_husband(male1)
        family1.set_wife(female1)
        self.assertTrue(family1.birth_before_death_of_parents())

if __name__ == '__main__':
    # -----------------------------------------------
    fam1=Family("F01")
    fam1.set_divorcedDate(['8', 'SEP', '2009'])
    fam1.set_marriedDate(['8', 'SEP', '2000'])
    fam2=Family("F02")
    male1=Individual("P01")
    per1=Individual("P01")
    per2=Individual("P02")
    per1.set_deathDate(['8', 'SEP', '2010'])
    per2.set_deathDate(['8', 'SEP', '2011'])
    fam2.set_husband(per1)
    fam2.set_wife(per2)
    fam2.set_marriedDate(['8', 'SEP', '2001'])
    #-------------------------------------------------
    print('Running unit tests')
    unittest.main()
