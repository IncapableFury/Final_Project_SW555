import unittest
import sys
# sys.path.append('../')

from models.Individual import Individual
from models.Family import Family

class sprint2Test(unittest.TestCase):
    def testMaleLastNames(self):
        #family1
        fam1 = Family("1")
        #Husband
        ind1 = Individual("1")
        ind1.set_gender("male")
        ind1.set_name("Charles Glass")

        #Wife
        ind2 = Individual("2")
        ind2.set_gender("female")
        ind2.set_name("Betty Glass")

        #Child 1
        ind3 = Individual("3")
        ind3.set_gender("female")
        ind3.set_name("Nancy Glass")

        # Child 2
        ind4 = Individual("4")
        ind4.set_gender("male")
        ind4.set_name("Bobby Glass")

        # Child 3
        ind5 = Individual("5")
        ind5.set_gender("male")
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
        ind6.set_gender("male")
        ind6.set_name("Charles Glass")

        # Wife
        ind7 = Individual("7")
        ind7.set_gender("female")
        ind7.set_name("Betty Glass")

        # Child 1
        ind8 = Individual("8")
        ind8.set_gender("female")
        ind8.set_name("Nancy Glass")

        # Child 2
        ind9 = Individual("9")
        ind9.set_gender("male")
        ind9.set_name("Bobby Tarantino")

        # Child 3
        ind10 = Individual("10")
        ind10.set_gender("male")
        ind10.set_name("Jack Glass")

        fam2.set_wife(ind7)
        fam2.set_husband(ind6)
        fam2.set_marriedDate((1992, 3, 17))
        fam2.set_children([ind8, ind9, ind10])

        self.assertFalse(fam2.male_last_names())

        #fam3
        fam3 = Family('3')
        #husband
        ind11 = Individual("11")
        ind11.set_gender("male")
        ind11.set_name("Chad Glass")
        #wife
        ind12 = Individual("12")
        ind12.set_gender("female")
        ind12.set_name("Sandy Glass")
        # Child 1
        ind13 = Individual("13")
        ind13.set_gender("female")
        ind13.set_name("Nancy Glass")

        # Child 2
        ind14 = Individual("9")
        ind14.set_gender("male")
        ind14.set_name("Bobby Tarantino")

        fam3.set_husband(ind8)
        fam3.set_wife(ind12)
        fam3.set_children([ind13,ind14])
        #husband of fam1's parent family is fam3
        ind1.set_parentFamily(fam3)
        # print(ind8._family)
        # print(ind8._family[0].get_children())
        self.assertFalse(fam1.male_last_names())

    def testNoMarriagesToDescendants(self):
        ## BASE CASE(husband and wife has no parent family)

        #fam1
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

        #fam2
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

        # ind8.set_families(fam2)
        # ind9.set_families(fam2)
        # ind10.set_families(fam2)

        fam2.set_wife(ind7)
        fam2.set_husband(ind8)
        fam2.set_marriedDate((1989, 7, 25))
        fam2.set_children([ind8,ind9,ind10])
        self.assertFalse(fam2.no_marriages_to_descendants())

        # #husband with parent family
        # #fam3
        # fam3 = Family("3")
        # # Husband
        # ind11 = Individual("11")
        # # Wife
        # ind12 = Individual("12")
        # # Child 1
        # ind13 = Individual("13")
        # # Child 2
        # ind14 = Individual("14")
        #
        # ind13.set_families(fam3)
        # ind14.set_families(fam3)
        #
        # fam3.set_wife(ind12)
        # fam3.set_husband(ind11)
        # fam3.set_children([ind13,ind14])
        #
        # #husband of family1's parent family is fam3
        # ind1.set_parentFamily(fam3)
        # self.assertTrue(fam1.no_marriages_to_descendants())
        #
        # #2 generations of parent family, husband side
        # # fam3
        # fam4 = Family("4")
        # # Husband
        # ind15 = Individual("15")
        # # Wife
        # ind16 = Individual("16")
        # # Child 1
        # ind17 = Individual("17")
        # # Child 2
        # ind18 = Individual("18")
        # fam4.set_wife(ind16)
        # fam4.set_husband(ind15)
        # fam4.set_children([ind17, ind18])
        # # husband of family3's parent family is fam4
        # ind11.set_parentFamily(fam4)
        # self.assertTrue(fam1.no_marriages_to_descendants())
        #
        # # Adding parent family to fam1 wife's side
        #
        # fam5 = Family("5")
        # # Husband
        # ind19 = Individual("19")
        # # Wife
        # ind20 = Individual("20")
        # # Child 1
        # ind21 = Individual("21")
        # # Child 2
        # ind22 = Individual("22")
        # fam5.set_wife(ind20)
        # fam5.set_husband(ind19)
        # fam5.set_children([ind19, ind22])
        # # wife of family1's parent family is fam5
        # ind2.set_parentFamily(fam5)
        # print(ind2._parentFamily)
        # self.assertFalse(fam1.no_marriages_to_descendants())

if __name__ == '__main__':
    unittest.main()
    pass