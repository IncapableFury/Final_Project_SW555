import unittest
import sys  
sys.path.append('../')

from models.Individual import Individual
from models.Family import Family

class TestDivorseBeforeDeath(unittest.TestCase):
    def test1(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate(["5", "MAR", "2000"])
        female1.set_deathDate(["9", "APR", "2002"])
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorced(["1", "JAN", "1999"])
        self.assertTrue(family1.divorce_before_death())

    def test2(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate(["5", "MAR", "2000"])
        female1.set_deathDate(["9", "APR", "2002"])
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorced(["1", "JAN", "2001"])
        self.assertFalse(family1.divorce_before_death())

    def test3(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate(["5", "MAR", "2000"])
        female1.set_deathDate(["9", "APR", "2002"])
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorced(["1", "JAN", "2003"])
        self.assertFalse(family1.divorce_before_death())

    def test4(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate(["5", "MAR", "2000"])
        female1.set_deathDate(["9", "APR", "2002"])
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorced(["1", "JAN", "2000"])
        self.assertTrue(family1.divorce_before_death())

    def test5(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate(["5", "MAR", "2000"])
        female1.set_deathDate(["9", "APR", "2002"])
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorced(["1", "JAN", "2002"])
        self.assertFalse(family1.divorce_before_death())

class TestBirthBeforeDeathofParent(unittest.TestCase):
    def test1(self):
        male1=Individual("P01")
        female1=Individual("P02")
        child1=Individual("P03")
        family1=Family("F01")
        family1.add_child(child1)
        male1.set_deathDate(["5", "MAR", "2000"])
        female1.set_deathDate(["9", "APR", "2002"])
        child1.set_birthDate(["6", "JAN", "1998"])
        family1.set_husband(male1)
        family1.set_wife(female1)
        self.assertTrue(family1.birth_before_death_of_parents())
    def test2(self):
        male1=Individual("P01")
        female1=Individual("P02")
        child1=Individual("P03")
        family1=Family("F01")
        family1.add_child(child1)
        male1.set_deathDate(["5", "MAR", "2000"])
        female1.set_deathDate(["9", "APR", "2002"])
        child1.set_birthDate(["6", "JAN", "2001"])
        family1.set_husband(male1)
        family1.set_wife(female1)
        self.assertRaises(ValueError,family1.birth_before_death_of_parents())
    def test3(self):
        male1=Individual("P01")
        female1=Individual("P02")
        child1=Individual("P03")
        family1=Family("F01")
        family1.add_child(child1)
        male1.set_deathDate(["5", "MAR", "2000"])
        female1.set_deathDate(["9", "APR", "2002"])
        child1.set_birthDate(["6", "MAR", "2000"])
        family1.set_husband(male1)
        family1.set_wife(female1)
        self.assertTrue(family1.birth_before_death_of_parents())

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()