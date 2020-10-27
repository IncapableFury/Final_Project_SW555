import unittest

from models.Individual import Individual
from models.Family import Family
from models.Gedcom import Gedcom

class TestSprint2(unittest.TestCase):
    def test_unique_name_and_birth_date(self):
        SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
                                       "DIV", "DATE", "HEAD", "TRLR", "NOTE"}
        G1 = Gedcom('../testing_files/Jiashu_Wang.ged',SUPPORT_TAGS)
        G2 = Gedcom('../testing_files/MichealFahimGEDCOM.ged',SUPPORT_TAGS)
        G3 = Gedcom('../testing_files/mock-family.ged', SUPPORT_TAGS)
        # --------------------------------------------------
        assert G1.unique_name_and_birth_date() == True
        assert G2.unique_name_and_birth_date() == True
        assert G3.unique_name_and_birth_date() == True



if __name__ == '__main__':
    unittest.main()
    pass