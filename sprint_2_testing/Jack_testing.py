import unittest
import sys
sys.path.append('../')

from models.Individual import Individual
from models.Family import Family

class sprint2Test(unittest.TestCase):
    def testMaleLastNames(self):
        fam1 = Family("1")

        #Husband
        ind1 = Individual("1")
        ind1.set_gender("male")
        ind1.set_name(["Charles", "Glass"])

        #Wife
        ind2 = Individual("2")
        ind2.set_gender("female")
        ind2.set_name(["Betty", "Glass"])

        #Child 1
        ind3 = Individual("3")
        ind3.set_gender("female")
        ind3.set_name(["Nancy", "Glass"])

        # Child 2
        ind4 = Individual("4")
        ind4.set_gender("male")
        ind4.set_name(["Bobby", "Glass"])

        # Child 3
        ind5 = Individual("5")
        ind5.set_gender("male")
        ind5.set_name(["Jack", "Glass"])

        fam1.set_wife(ind2)
        fam1.set_husband(ind1)
        fam1.set_children([ind3,ind4,ind5])

        self.assertTrue(fam1.male_last_names())

if __name__ == '__main__':
    unittest.main()
    pass