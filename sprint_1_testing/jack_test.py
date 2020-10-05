
import unittest
import sys

sys.path.append("../")

from models.Individual import Individual
from models.Family import Family 




class TestSprint1(unittest.TestCase):
    def test_date_compare(self):
        
        fam_1 = Family("01")
        ind_1 = Individual("01")
        ind_1.set_birthDate((2019,9,1))
        ind_1.set_parentFamily(fam_1)
        fam_1.set_marriedDate((2019,9,2))
        
        assert ind_1.birth_before_marriage() == True


if __name__ == '__main__':
    unittest.main()
    pass

