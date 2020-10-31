import unittest
import sys
# sys.path.append('../')

from models.Individual import Individual
from models.Family import Family

class sprint2Test(unittest.TestCase):
    def testMLastNames(self):
        #family1
        fam1 = Family("1")
        #Husband
        ind1 = Individual("1")
        ind1.set_gender("M")
        ind1.set_name("Charles Glass")

        #Wife
        ind2 = Individual("2")
        ind2.set_gender("F")
        ind2.set_name("Betty Glass")

        #Child 1
        ind3 = Individual("3")
        ind3.set_gender("M")
        ind3.set_name("Nate Glass")

        # Child 2
        ind4 = Individual("4")
        ind4.set_gender("M")
        ind4.set_name("Bobby Glass")

        # Child 3
        ind5 = Individual("5")
        ind5.set_gender("M")
        ind5.set_name("Jack Glass")

        fam1.set_wife(ind2)
        fam1.set_husband(ind1)
        fam1.set_marriedDate((1989,7,25))
        fam1.set_children([ind3,ind4,ind5])

        self.assertTrue(fam1.male_last_names())

        #family2
        fam2 = Family("2")
        # Husband
        ind6 = Individual("6")
        ind6.set_gender("M")
        ind6.set_name("Charles Glass")

        # Wife
        ind7 = Individual("7")
        ind7.set_gender("F")
        ind7.set_name("Betty Glass")

        # Child 1
        ind8 = Individual("8")
        ind8.set_gender("F")
        ind8.set_name("Nancy Glass")

        # Child 2
        ind9 = Individual("9")
        ind9.set_gender("M")
        ind9.set_name("Bobby Tarantino")

        # Child 3
        ind10 = Individual("10")
        ind10.set_gender("M")
        ind10.set_name("Jack Glass")

        fam2.set_wife(ind7)
        fam2.set_husband(ind6)
        fam2.set_marriedDate((1992, 3, 17))
        fam2.set_children([ind8, ind9, ind10])

        self.assertFalse(fam2.male_last_names())

        #fam3
        fam3 = Family('3')
        #husband
        fam3.set_husband(ind3)
        ind3.add_to_family(fam3)
        #wife
        ind11 = Individual("11")
        ind11.set_gender("F")
        ind11.set_name("Sandy Glass")
        # Child 1
        ind12 = Individual("12")
        ind12.set_gender("F")
        ind12.set_name("Nancy T")

        # Child 2
        ind13 = Individual("13")
        ind13.set_gender("M")
        ind13.set_name("Bobby Glass")


        fam3.set_wife(ind11)
        fam3.set_children([ind12,ind13])

        self.assertTrue(fam1.male_last_names())

        # fam4
        fam4 = Family('4')
        # husband
        fam4.set_husband(ind4)
        ind4.add_to_family(fam4)
        # wife
        ind14 = Individual("14")
        ind14.set_gender("F")
        ind14.set_name("Sandy Glass")

        # Child 1
        ind15 = Individual("15")
        ind15.set_gender("F")
        ind15.set_name("Nancy T")

        # Child 2
        ind16 = Individual("16")
        ind16.set_gender("M")
        ind16.set_name("Bobby T")

        fam4.set_wife(ind14)
        fam4.set_children([ind15, ind16])

        self.assertFalse(fam1.male_last_names())


    def testNoMarriagesToDescendants(self):
        ## BASE CASE(husband and wife has no parent family)

        #fam1
        fam1 = Family("1")
        # Husband
        ind1 = Individual("1")
        ind1.set_gender("M")
        ind1.add_to_family(fam1)
        # Wife
        ind2 = Individual("2")
        ind2.set_gender("F")
        ind2.add_to_family(fam1)
        # Child 1
        ind3 = Individual("3")
        ind3.set_gender("M")
        # Child 2
        ind4 = Individual("4")
        ind4.set_gender("M")
        # Child 3
        ind5 = Individual("5")
        ind5.set_gender("F")

        fam1.set_husband(ind1)
        fam1.set_wife(ind2)
        fam1.set_marriedDate((1989, 7, 25))
        fam1.set_children([ind3, ind4, ind5])
        self.assertTrue(ind1.no_marriages_to_descendants())

        #fam2
        fam2 = Family("2")
        # Husband
        ind6 = Individual("6")
        ind6.set_gender("M")
        ind6.add_to_family(fam2)
        # Wife
        ind7 = Individual("7")
        ind7.set_gender("F")
        ind7.add_to_family(fam2)
        # Child 1
        ind8 = Individual("8")
        # Child 2
        ind9 = Individual("9")
        ind9.set_gender("M")
        # Child 3
        ind10 = Individual("10")
        ind10.set_gender("F")

        fam2.set_husband(ind6)
        fam2.set_wife(ind7)
        fam2.set_marriedDate((1989, 7, 25))
        fam2.set_children([ind6,ind9,ind10])

        self.assertFalse(ind6.no_marriages_to_descendants())

        #fam3
        fam3 = Family("3")
        # Husband
        fam3.set_husband(ind3)
        ind3.add_to_family(fam3)
        # Wife
        ind11 = Individual("11")
        ind11.set_gender("F")
        # Child 1
        ind12 = Individual("12")
        ind12.set_gender("M")
        # Child 2
        ind13 = Individual("13")
        ind13.set_gender("F")

        fam3.set_wife(ind11)
        fam3.set_children([ind12,ind13])

        self.assertTrue(ind1.no_marriages_to_descendants())

        #fam4
        fam4 = Family("4")
        # Husband
        fam4.set_husband(ind12)
        ind12.add_to_family(fam4)
        # Wife
        ind14 = Individual("14")
        ind14.set_gender("F")
        # Child 1
        ind15 = Individual("15")
        # Child 2
        ind16 = Individual("16")
        ind16.set_gender("M")

        fam4.set_wife(ind14)
        fam4.set_children([ind2,ind16])

        self.assertFalse(ind1.no_marriages_to_descendants())

if __name__ == '__main__':
    unittest.main()
    pass