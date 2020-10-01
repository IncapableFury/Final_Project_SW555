"""
Test cases go in here
Van comment for second time
"""

import unittest

from models.Individual import Individual
from models.Family import Family
from models import Gedcom


class TestDivorseBeforeDeath(unittest.TestCase):
    def test1(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorced("1 JAN 1999")
        self.assertTrue(family1.divorce_before_death())

    def test2(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorced("1 JAN 2001")
        self.assertFalse(family1.divorce_before_death())
    
    def test3(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorced("1 JAN 2003")
        self.assertFalse(family1.divorce_before_death())
    
    def test4(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorced("1 JAN 2000")
        self.assertTrue(family1.divorce_before_death())
    
    def test5(self):
        male1=Individual("P01")
        female1=Individual("P02")
        family1=Family("F01")
        male1.set_deathDate("5 MAR 2000")
        female1.set_deathDate("9 APR 2002")
        family1.set_husband(male1)
        family1.set_wife(female1)
        family1.set_divorced("1 JAN 2002")
        self.assertFalse(family1.divorce_before_death())

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
