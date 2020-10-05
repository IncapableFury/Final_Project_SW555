import unittest
import sys

sys.path.append("../")

from models.Individual import Individual
from models.Family import Family


class TestSprint1(unittest.TestCase):
    def test_date_compare(self):
        fam_1 = Family("01")
        ind_1 = Individual("01")
        ind_1.set_birthDate((2019, 9, 1))
        ind_1.set_parentFamily(fam_1)
        fam_1.set_marriedDate((2019, 9, 2))
        ind_1.set_deathDate((2020,9,1))

        fam_2 = Family("02")
        ind_2 = Individual("02")
        ind_2.set_birthDate((2019,8,1))
        ind_2.set_parentFamily((fam_2))
        fam_2.set_marriedDate((2019,7,1))
        ind_2.set_deathDate((2018,8,1))
        assert ind_1.birth_before_marriage() == True
        assert ind_2.birth_before_marriage() == False

        assert ind_1.birth_before_death() == True
        assert ind_2.birth_before_death() == False



if __name__ == '__main__':
    unittest.main()
    pass

