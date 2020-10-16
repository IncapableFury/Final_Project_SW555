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
        fam1.set_marriedDate((1989,7,25))
        fam1.set_children([ind3,ind4,ind5])

        self.assertTrue(fam1.male_last_names())

        fam2 = Family("2")

        # Husband
        ind6 = Individual("6")
        ind6.set_gender("male")
        ind6.set_name(["Charles", "Glass"])

        # Wife
        ind7 = Individual("7")
        ind7.set_gender("female")
        ind7.set_name(["Betty", "Glass"])

        # Child 1
        ind8 = Individual("8")
        ind8.set_gender("female")
        ind8.set_name(["Nancy", "Glass"])

        # Child 2
        ind9 = Individual("9")
        ind9.set_gender("male")
        ind9.set_name(["Bobby", "Tarantino"])

        # Child 3
        ind10 = Individual("10")
        ind10.set_gender("male")
        ind10.set_name(["Jack", "Glass"])

        fam2.set_wife(ind7)
        fam2.set_husband(ind6)
        fam2.set_marriedDate((1992, 3, 17))
        fam2.set_children([ind8, ind9, ind10])

        self.assertFalse(fam2.male_last_names())

    def testNoMarriagesToDescendants(self):
        fam1 = Family("1")

        # Husband
        ind1 = Individual("1")

        # Wife
        ind2 = Individual("2")

        # Child 1
        ind3 = Individual("3")

        # Child 2
        ind4 = Individual("4")

        # Child 3
        ind5 = Individual("5")

        fam1.set_wife(ind2)
        fam1.set_husband(ind1)
        fam1.set_marriedDate((1989, 7, 25))
        fam1.set_children([ind3, ind4, ind5])

        self.assertTrue(fam1.no_marriages_to_descendants())
        fam2 = Family("2")

        # Husband
        ind6 = Individual("6")

        # Wife
        ind7 = Individual("7")

        # Child 1
        ind8 = Individual("8")

        # Child 2
        ind9 = Individual("9")

        # Child 3
        ind10 = Individual("10")

        fam2.set_wife(ind7)
        fam2.set_husband(ind8)
        fam2.set_marriedDate((1989, 7, 25))
        fam2.set_children([ind8,ind9,ind10])

        self.assertFalse(fam2.no_marriages_to_descendants())

if __name__ == '__main__':
    unittest.main()
    pass