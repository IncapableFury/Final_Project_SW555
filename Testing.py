import unittest
import sys
#sys.path.append('../')

from models.Individual import Individual
from models.Family import Family
from models.Gedcom import Gedcom


class TestSprint1(unittest.TestCase):

    def setUp(self):
        SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
                        "DIV", "DATE", "HEAD", "TRLR", "NOTE"}
        self.G1 = Gedcom('../testing_files/right.ged', SUPPORT_TAGS)
        self.G2 = Gedcom('../testing_files/wrong.ged', SUPPORT_TAGS)

        self.ind_1 = Individual("01")
        self.ind_2 = Individual("02")
        self.ind_3 = Individual("03")

        self.fam_1 = Family("01")
        self.fam_2 = Family("02")

    def tearDown(self):
        self.ind_1 = Individual("01")
        self.ind_2 = Individual("02")
        self.ind_3 = Individual("03")

        self.fam_1 = Family("01")
        self.fam_2 = Family("02")


    def test_US11_no_bigamy(self):
        self.ind_1.set_birthDate(["09", "APR", "1997"])
        self.ind_2.set_birthDate(["19", "DEC", "1997"])
        self.ind_1.add_to_family(self.fam_1)
        self.fam_1.set_marriedDate(["01", "JUN", "2017"])
        self.assertTrue(self.ind_1.no_bigamy())
        self.fam_2.set_marriedDate(["05", "JUN", "2016"])
        self.ind_1.add_to_family(self.fam_2)
        self.assertFalse(self.ind_1.no_bigamy())
        self.fam_2.set_divorcedDate(("01", "JAN", "2017"))
        self.assertTrue(self.ind_1.no_bigamy())
        self.fam_2.set_divorcedDate(("01", "AUG", "2017"))
        self.assertFalse(self.ind_1.no_bigamy())
        self.fam_1.set_divorcedDate(("01", "DEC", "2018"))
        self.assertFalse(self.ind_1.no_bigamy())
        self.fam_2.set_divorcedDate(("01", "JAN", "2017"))
        self.assertTrue(self.ind_1.no_bigamy())

    def test_US02_birth_before_marriage(self):
        self.ind_1.set_birthDate(["09", "APR", "1997"])
        self.ind_1.add_to_family(self.fam_1)
        self.fam_1.set_marriedDate(["01", "JUN", "2018"])
        self.assertTrue(self.ind_1.birth_before_marriage())

    def test_US03_birth_before_death(self):
        self.ind_1.set_birthDate(["09", "APR", "1997"])
        self.ind_1.set_deathDate(["01", "JUN", "2018"])
        self.assertTrue(self.ind_1.birth_before_death())


    def  test_US07_less_then_150_years_old(self):
        self.ind_1.set_birthDate(["09", "APR", "1997"])

        self.assertTrue(self.ind_1.less_then_150_years_old())
        self.ind_2.set_birthDate(["09", "APR", "997"])
        self.assertFalse(self.ind_2.less_then_150_years_old())

    def test_US04_marriage_before_divorce(self):
            t1 = Family("F01")
            male1 = Individual("P01")
            female1 = Individual("P02")
            male1.set_deathDate(['8', 'SEP', '2010'])
            female1.set_deathDate(['8', 'SEP', '2011'])
            t1.set_husband(male1)
            t1.set_wife(female1)
            t1.set_marriedDate(['8', 'SEP', '2000'])
            t1.set_divorcedDate(['8', 'SEP', '2009'])
            # ---------------------------------
            t2 = Family("F02")
            male2 = Individual("P03")
            female2 = Individual("P04")
            male2.set_deathDate(['8', 'SEP', '2012'])
            female2.set_deathDate(['8', 'SEP', '2013'])
            t2.set_husband(male2)
            t2.set_wife(female2)
            t2.set_marriedDate(['8', 'SEP', '2005'])
            t2.set_divorcedDate(['8', 'SEP', '2004'])
            # ---------------------------------
            assert t1.marriage_before_divorce() == True
            assert t2.marriage_before_divorce() == False

    def test_US05_marriage_before_death(self):
            t1 = Family("F01")
            male1 = Individual("P01")
            female1 = Individual("P02")
            male1.set_deathDate(['8', 'SEP', '2010'])
            female1.set_deathDate(['8', 'SEP', '2011'])
            t1.set_husband(male1)
            t1.set_wife(female1)
            t1.set_marriedDate(['8', 'SEP', '2000'])
            # ---------------------------------
            t2 = Family("F02")
            male2 = Individual("P03")
            female2 = Individual("P04")
            male2.set_deathDate(['8', 'SEP', '1999'])
            female2.set_deathDate(['9', 'SEP', '2011'])
            t2.set_husband(male2)
            t2.set_wife(female2)
            t2.set_marriedDate(['8', 'SEP', '2000'])
            # ---------------------------------
            t3 = Family("F03")
            male3 = Individual("P05")
            female3 = Individual("P06")
            male3.set_deathDate(['8', 'SEP', '2003'])
            female3.set_deathDate(['9', 'SEP', '1998'])
            t3.set_husband(male3)
            t3.set_wife(female3)
            t3.set_marriedDate(['8', 'SEP', '2000'])
            # ---------------------------------
            t4 = Family("F04")
            male4 = Individual("P07")
            female4 = Individual("P08")
            male4.set_deathDate(['8', 'SEP', '1998'])
            female4.set_deathDate(['9', 'SEP', '1999'])
            t4.set_husband(male4)
            t4.set_wife(female4)
            t4.set_marriedDate(['8', 'SEP', '2000'])
            # ---------------------------------
            t5 = Family("F05")
            male5 = Individual("P09")
            female5 = Individual("P10")
            male5.set_deathDate(['8', 'SEP', '2009'])
            female5.set_deathDate(['8', 'SEP', '2009'])
            t5.set_husband(male5)
            t5.set_wife(female5)
            t5.set_marriedDate(['8', 'SEP', '2009'])
            # ---------------------------------
            assert t1.marriage_before_death() == True
            assert t2.marriage_before_death() == False
            assert t3.marriage_before_death() == False
            assert t4.marriage_before_death() == False
            assert t5.marriage_before_death() == True

    def test_US06_divorse_before_death(self):
            t1 = Family("F01")
            male1 = Individual("P01")
            female1 = Individual("P02")
            male1.set_deathDate(["5", "MAR", "2000"])
            female1.set_deathDate(["9", "APR", "2002"])
            t1.set_husband(male1)
            t1.set_wife(female1)
            t1.set_divorcedDate(["1", "JAN", "1999"])
            # ---------------------------------
            t2 = Family("F02")
            male2 = Individual("P03")
            female2 = Individual("P04")
            male2.set_deathDate(["5", "MAR", "2000"])
            female2.set_deathDate(["9", "APR", "2002"])
            t2.set_husband(male2)
            t2.set_wife(female2)
            t2.set_divorcedDate(["1", "JAN", "2003"])

            # ---------------------------------
            assert t1.divorce_before_death() == True
            assert t2.divorce_before_death() == False


    def test_US08_birth_before_marriage_of_parents(self):
            t1 = Family("F01")
            male1 = Individual("P01")
            female1 = Individual("P02")
            child1 = Individual("P03")
            t1.add_child(child1)
            t1.set_marriedDate(['8', 'SEP', '2000'])
            child1.set_birthDate(["6", "JAN", "1998"])
            t1.set_husband(male1)
            t1.set_wife(female1)
            # ---------------------------------
            t2 = Family("F02")
            male2 = Individual("P04")
            female2 = Individual("P05")
            child2 = Individual("P06")
            t2.add_child(child2)
            t2.set_marriedDate(['8', 'SEP', '2000'])
            child2.set_birthDate(["6", "JAN", "2001"])
            t2.set_husband(male2)
            t2.set_wife(female2)
            # ---------------------------------
            t3 = Family("F03")
            male3 = Individual("P07")
            female3 = Individual("P08")
            child3 = Individual("P09")
            t3.add_child(child3)
            t3.set_marriedDate(['6', 'MAR', '2000'])
            child3.set_birthDate(["6", "MAR", "2000"])
            t3.set_husband(male3)
            t3.set_wife(female3)
            # ---------------------------------
            assert t1.birth_before_marriage_of_parents() == False
            assert t2.birth_before_marriage_of_parents() == True
            assert t3.birth_before_marriage_of_parents() == False

    def test_US09_birth_before_death_of_parent(self):
            t1 = Family("F01")
            male1 = Individual("P01")
            female1 = Individual("P02")
            child1 = Individual("P03")
            t1.add_child(child1)
            male1.set_deathDate(["5", "MAR", "2000"])
            female1.set_deathDate(["9", "APR", "2002"])
            child1.set_birthDate(["6", "JAN", "1998"])
            t1.set_husband(male1)
            t1.set_wife(female1)
            # ---------------------------------
            t2 = Family("F02")
            male2 = Individual("P04")
            female2 = Individual("P05")
            child2 = Individual("P06")
            t2.add_child(child2)
            male2.set_deathDate(["5", "MAR", "2000"])
            female2.set_deathDate(["9", "APR", "2002"])
            child2.set_birthDate(["6", "JAN", "2001"])
            t2.set_husband(male2)
            t2.set_wife(female2)
            # ---------------------------------
            t3 = Family("F03")
            male3 = Individual("P07")
            female3 = Individual("P08")
            child3 = Individual("P09")
            t3.add_child(child3)
            male3.set_deathDate(["5", "MAR", "2000"])
            female3.set_deathDate(["9", "APR", "2002"])
            child3.set_birthDate(["6", "MAR", "2000"])
            t3.set_husband(male3)
            t3.set_wife(female3)
            # ---------------------------------
            assert t1.birth_before_death_of_parents() == True
            assert t2.birth_before_death_of_parents() == False
            assert t3.birth_before_death_of_parents() == True

    def test_US10_marriage_after_14(self):
            t1 = Family("F01")
            male1 = Individual("P01")
            female1 = Individual("P02")
            male1.set_birthDate(['8', 'SEP', '2000'])
            female1.set_birthDate(['8', 'SEP', '2000'])
            t1.set_husband(male1)
            t1.set_wife(female1)
            t1.set_marriedDate(['8', 'SEP', '2014'])
            # --------------------------------------------------
            t2 = Family("F02")
            male2 = Individual("P03")
            female2 = Individual("P04")
            male2.set_birthDate(['7', 'SEP', '2000'])
            female2.set_birthDate(['8', 'SEP', '2000'])
            t2.set_husband(male2)
            t2.set_wife(female2)
            t2.set_marriedDate(['8', 'SEP', '2014'])
            # --------------------------------------------------
            t3 = Family("F03")
            male3 = Individual("P05")
            female3 = Individual("P06")
            male3.set_birthDate(['8', 'SEP', '2000'])
            female3.set_birthDate(['7', 'SEP', '2000'])
            t3.set_husband(male3)
            t3.set_wife(female3)
            t3.set_marriedDate(['8', 'SEP', '2014'])
            # --------------------------------------------------
            t4 = Family("F04")
            male4 = Individual("P07")
            female4 = Individual("P08")
            male4.set_birthDate(['1', 'SEP', '1990'])
            female4.set_birthDate(['2', 'SEP', '1990'])
            t4.set_husband(male4)
            t4.set_wife(female4)
            t4.set_marriedDate(['8', 'SEP', '2014'])
            # --------------------------------------------------
            t5 = Family("F05")
            male5 = Individual("P09")
            female5 = Individual("P10")
            male5.set_birthDate(['09', 'APR', '1997'])
            female5.set_birthDate(['19', 'DEC', '1997'])
            t5.set_husband(male5)
            t5.set_wife(female5)
            t5.set_marriedDate(['1', 'JUN', '2007'])
            # --------------------------------------------------
            assert t1.marriage_after_14() == False
            assert t2.marriage_after_14() == False
            assert t3.marriage_after_14() == False
            assert t4.marriage_after_14() == True
            assert t5.marriage_after_14() == False

    def test_US13_siblings_spacing(self):
            t1 = Family("t1")
            t2 = Family("t2")
            t3 = Family("t3")
            t4 = Family("t4")
            t5 = Family("t5")
            t6 = Family("t6")
            p1 = Individual("p1")
            p1.set_birthDate(("1", "JAN", "1990"))
            p2 = Individual("p2")
            p2.set_birthDate(("1", "JAN", "1990"))
            p3 = Individual("p3")
            p3.set_birthDate(("1", "SEP", "1990"))
            p4 = Individual("p4")
            p4.set_birthDate(("2", "JAN", "1990"))
            p5 = Individual("p5")
            p5.set_birthDate(("3", "JAN", "1990"))
            p6 = Individual("p6")
            p6.set_birthDate(("30", "MAY", "1990"))
            # --------------------------------------------------
            t1.add_child(p1)
            t1.add_child(p2)
            t2.add_child(p1)
            t2.add_child(p3)
            t3.add_child(p1)
            t3.add_child(p4)
            t4.add_child(p1)
            t4.add_child(p5)
            t5.add_child(p1)
            t5.add_child(p6)
            t6.add_child(p1)
            t6.add_child(p3)
            t6.add_child(p6)
            # --------------------------------------------------
            assert t1.siblings_spacing() == True
            assert t2.siblings_spacing() == True
            assert t3.siblings_spacing() == True
            assert t4.siblings_spacing() == False
            assert t5.siblings_spacing() == False
            assert t6.siblings_spacing() == False

    def test_US14_multiple_births_lessOrEqual_than_5(self):
            t1 = Family("t1")
            t2 = Family("t2")
            t3 = Family("t3")
            p1 = Individual("p1")
            p1.set_birthDate(("1", "JAN", "1990"))
            p2 = Individual("p2")
            p2.set_birthDate(("1", "JAN", "1990"))
            p3 = Individual("p3")
            p3.set_birthDate(("1", "JAN", "1990"))
            p4 = Individual("p4")
            p4.set_birthDate(("3", "JAN", "1990"))
            p5 = Individual("p5")
            p5.set_birthDate(("2", "JAN", "1990"))
            p6 = Individual("p6")
            p6.set_birthDate(("30", "MAY", "1990"))
            p7 = Individual("p7")
            p7.set_birthDate(("2", "JAN", "1990"))
            p8 = Individual("p8")
            p8.set_birthDate(("2", "JAN", "1990"))
            p9 = Individual("p9")
            p9.set_birthDate(("2", "SEP", "1990"))
            p10 = Individual("p10")
            p10.set_birthDate(("2", "SEP", "1990"))
            p11 = Individual("p11")
            p11.set_birthDate(("3", "SEP", "1990"))
            p12 = Individual("p12")
            p12.set_birthDate(("3", "SEP", "1990"))
            p13 = Individual("p13")
            p13.set_birthDate(("3", "SEP", "1990"))
            # -------------------------------
            t1.add_child(p1)
            t1.add_child(p2)
            t1.add_child(p3)
            t1.add_child(p4)
            t1.add_child(p5)
            t1.add_child(p6)
            t1.add_child(p7)
            t1.add_child(p8)
            t2.add_child(p1)
            t2.add_child(p2)
            t2.add_child(p3)
            t2.add_child(p4)
            t2.add_child(p5)
            t2.add_child(p6)
            t3.add_child(p3)
            t3.add_child(p4)
            t3.add_child(p5)
            t3.add_child(p6)
            t3.add_child(p7)
            t3.add_child(p8)
            t3.add_child(p9)
            t3.add_child(p10)
            t3.add_child(p11)
            t3.add_child(p12)
            t3.add_child(p13)
            # ---------------------------------
            assert t1.multiple_births_lessOrEqual_than_5() == False
            assert t2.multiple_births_lessOrEqual_than_5() == True
            assert t3.multiple_births_lessOrEqual_than_5() == False

    def test_US12_parents_not_too_old(self):
        t1 = Family("t1")
        t2 = Family("t2")
        p1 = Individual("p1")
        p2 = Individual("p2")
        p3 = Individual("p3")
        p4 = Individual("p4")
        p5 = Individual("p5")
        p6 = Individual("p6")
        t1.set_wife(p1)
        t1.set_husband(p2)
        t1.add_child(p3)
        t2.set_wife(p4)
        t2.set_husband(p5)
        t2.add_child(p6)
        p1.set_birthDate(["1", "JAN", "1990"])
        p2.set_birthDate(["1", "JAN", "1990"])
        p4.set_birthDate(["1", "JAN", "1790"])
        p5.set_birthDate(["1", "JAN", "1790"])

        p3.set_birthDate(["1", "JAN", "2010"])
        p6.set_birthDate(["1", "JAN", "2000"])
        # ---------------------------------
        assert t1.parents_not_too_old() == True
        assert t2.parents_not_too_old() == False

    def test_US15_Fewer_than_15_siblings(self):
        t1 = Family("t1")
        t2 = Family("t2")
        p1 = Individual("p1")
        p2 = Individual("p2")
        p3 = Individual("p3")
        p4 = Individual("p4")
        p5 = Individual("p5")
        p6 = Individual("p6")
        p7 = Individual("p7")
        p8 = Individual("p8")
        p9 = Individual("p9")
        p10 = Individual("p10")
        p11 = Individual("p11")
        p12 = Individual("p12")
        p13 = Individual("p13")
        p14 = Individual("p14")
        p15= Individual("p15")
        p16= Individual("p16")
        p17= Individual("p17")
        p18= Individual("p18")
        p19= Individual("p19")
        p20= Individual("p20")
        p21= Individual("p21")
        p22 = Individual("p22")
        p23 = Individual("p23")
        p24 = Individual("p24")
        p25= Individual("p25")
        p26 = Individual("p26")
        p27 = Individual("p27")
        p28 = Individual("p28")

    # ---------------------------------
        t1.add_child(p1)
        t1.add_child(p2)
        t1.add_child(p3)
        t1.add_child(p4)
        t1.add_child(p5)
        t1.add_child(p6)
        t1.add_child(p7)
        t1.add_child(p8)
        t1.add_child(p9)
        t1.add_child(p10)
        t1.add_child(p11)
        t1.add_child(p12)
        t2.add_child(p13)
        t2.add_child(p14)
        t2.add_child(p15)
        t2.add_child(p16)
        t2.add_child(p17)
        t2.add_child(p18)
        t2.add_child(p19)
        t2.add_child(p20)
        t2.add_child(p21)
        t2.add_child(p22)
        t2.add_child(p23)
        t2.add_child(p24)
        t2.add_child(p25)
        t2.add_child(p26)
        t2.add_child(p27)
        t2.add_child(p28)
        # ---------------------------------
        assert t1.fewer_than_15_siblings() == True
        assert t2.fewer_than_15_siblings() == False

    def test_US21_Correct_Gender_For_Role(self):
        t1 = Family("t1")
        t2 = Family("t2")
        p1 = Individual("p1")
        p2 = Individual("p2")
        p3 = Individual("p3")
        p4 = Individual("p4")

    # ---------------------------------
        t1.set_wife(p1)
        t1.set_husband(p2)
        t2.set_wife(p3)
        t2.set_husband(p4)
        p1.set_gender('F')
        p2.set_gender('M')
        p4.set_gender('F')
        p3.set_gender('M')
    # ---------------------------------
        assert t1.correct_gender_for_role() == True
        assert t2.correct_gender_for_role() == False

    def test_US24_Unique_families_by_spouses(self):
        SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
                        "DIV", "DATE", "HEAD", "TRLR", "NOTE"}
        self.G1 = Gedcom('testing_files/Jiashu_Wang.ged', SUPPORT_TAGS)
        G2 = Gedcom('testing_files/MichealFahimGEDCOM.ged', SUPPORT_TAGS)
        G3 = Gedcom('testing_files/mock-family.ged', SUPPORT_TAGS)
        # ---------------------------------
        assert self.G1.unique_families_by_spouses() == True
        assert G2.unique_families_by_spouses() == True
        assert G3.unique_families_by_spouses() == True


    def test_US25_Unique_first_names_in_families(self):
        SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
                        "DIV", "DATE", "HEAD", "TRLR", "NOTE"}
        self.G1 = Gedcom('testing_files/Jiashu_Wang.ged', SUPPORT_TAGS)
        G2 = Gedcom('testing_files/MichealFahimGEDCOM.ged', SUPPORT_TAGS)
        G3 = Gedcom('testing_files/mock-family.ged', SUPPORT_TAGS)
        # ---------------------------------
        assert self.G1.unique_first_names_in_families() == True
        assert G2.unique_first_names_in_families() == True
        assert G3.unique_first_names_in_families() == True


    def test_US22_UniqueId(self):
        pass

    # finished in main funciton

    def test_US23_unique_name_and_birth_date(self):
        SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
                        "DIV", "DATE", "HEAD", "TRLR", "NOTE"}
        self.G1 = Gedcom('testing_files/Jiashu_Wang.ged', SUPPORT_TAGS)
        G2 = Gedcom('testing_files/MichealFahimGEDCOM.ged', SUPPORT_TAGS)
        G3 = Gedcom('testing_files/mock-family.ged', SUPPORT_TAGS)
        # --------------------------------------------------
        assert self.G1.unique_name_and_birth_date() == True
        assert G2.unique_name_and_birth_date() == True
        assert G3.unique_name_and_birth_date() == True

    def test_US18_Siblings_should_not_marry(self):
        t1 = Family("t1")
        t2 = Family("t2")
        t3 = Family("t3")
        t4 = Family("t4")
        t5 = Family("t5")
        t6 = Family("t6")
        p1 = Individual("p1")
        p2 = Individual("p2")
        p3 = Individual("p3")
        p4 = Individual("p4")
        # --------------------------------------------------
        
        t1.set_husband(p1)
        t1.set_wife(p2)
        t4.set_husband(p3)
        t4.set_wife(p4)
        '''
        t2.add_child(p1)
        t3.add_child(p2)
        t4.set_husband(p3)
        t4.set_wife(p4)
        t5.add_child(p3)
        t5.add_child(p4)
        '''
        # --------------------------------------------------
        p1.set_parentFamily(t2)
        p2.set_parentFamily(t3)
        p3.set_parentFamily(t5)
        p4.set_parentFamily(t5)
        # --------------------------------------------------
        assert t1.siblings_should_not_marry() == True
        #assert t2.siblings_should_not_marry() == True
        assert t4.siblings_should_not_marry() == False
        #assert t5.siblings_should_not_marry() == False

    def test_US19_First_cousins_should_not_marry(self):
        t1 = Family("t1")
        t2 = Family("t2")
        t3 = Family("t3")
        t4 = Family("t4")
        t5 = Family("t5")
        t6 = Family("t6")
        t7 = Family("t7")
        t8 = Family("t8")
        t9 = Family("t9")
        p1 = Individual("p1")
        p2 = Individual("p2")
        p3 = Individual("p3")
        p4 = Individual("p4")
        p5 = Individual("p5")
        p6 = Individual("p6")
        p7 = Individual("p7")
        p8 = Individual("p8")
        # --------------------------------------------------
        '''
        t1.add_child(p1)
        t1.add_child(p2)
        t2.set_wife(p1)
        t2.add_child(p3)
        t3.set_wife(p2)
        t3.add_child(p4)
        t4.set_husband(p3)
        t5.set_wife(p4)
        
        t6.add_child(p5)
        t6.add_child(p6)
        t7.set_wife(p5)
        t8.set_wife(p6)
        t7.add_child(p7)
        t8.add_child(p8)
        t9.set_wife(p7)
        t9.set_husband(p8)
        '''
        # --------------------------------------------------
        p3.set_parentFamily(t1)
        t1.set_husband(p8)
        t1.set_wife(p7)
        p8.set_parentFamily(t2)
        p7.set_parentFamily(t3)
        t2.add_child(p8)
        t3.add_child(p7)



        assert p3.first_cousins_should_not_marry()==True
        #assert p4.first_cousins_should_not_marry()==True

    def test_US16_Male_last_names(self):
        t1 = Family("t1")
        t2 = Family("t2")
        t3 = Family("t3")
        t4 = Family("t4")
        t5 = Family("t5")
        t6 = Family("t6")
        t7 = Family("t7")
        t8 = Family("t8")
        t9 = Family("t9")
        t10 = Family("t10")
        p1 = Individual("p1")
        p2 = Individual("p2")
        p3 = Individual("p3")
        p4 = Individual("p4")
        p5 = Individual("p5")
        p6 = Individual("p6")
        p7 = Individual("p7")
        p8 = Individual("p8")
        p9 = Individual("p9")
        p10 = Individual("p10")
        # --------------------------------------------------
        t1.set_husband(p1)
        t1.add_child(p2)
        t1.add_child(p3)
        t2.set_husband(p2)
        t3.set_husband(p3)
        t2.add_child(p4)
        t3.add_child(p5)
        t4.set_husband(p4)
        t5.set_husband(p5)

        t6.set_husband(p6)
        t6.add_child(p7)
        t6.add_child(p8)
        t7.set_husband(p7)
        t8.set_husband(p8)
        t7.add_child(p9)
        t8.add_child(p10)
        t9.set_husband(p9)
        t10.set_husband(p10)

        p1.set_gender("M")
        p1.set_name("Charles Glass")
        p2.set_gender("M")
        p2.set_name("Charles Glass")
        p3.set_gender("M")
        p3.set_name("Charles Glass")
        p4.set_gender("M")
        p4.set_name("Charles Glass")
        p5.set_gender("M")
        p5.set_name("Charles Glass")


        p6.set_gender("M")
        p6.set_name("Charles Glass")
        p7.set_gender("M")
        p7.set_name("Charles Glass")
        p8.set_gender("M")
        p8.set_name("Charles WDNMD")
        p9.set_gender("M")
        p9.set_name("Charles Glass")
        p10.set_gender("M")
        p10.set_name("Charles Glass")

        # --------------------------------------------------
        
        assert t3.male_last_names()==True 
        assert t8.male_last_names()==False
        


    def test_US17_No_marriages_to_descendants(self):
        t1 = Family("t1")
        t2 = Family("t2")
        t3 = Family("t3")
        t4 = Family("t4")
        p1 = Individual("p1")
        p2 = Individual("p2")
        p3 = Individual("p3")
        p4 = Individual("p4")
        p5 = Individual("p5")
        p6 = Individual("p6")
        p7 = Individual("p7")
        p8 = Individual("p8")
        p9 = Individual("p9")
        t1.set_husband(p1)
        t1.set_wife(p2)
        t1.add_child(p3)
        t2.set_wife(p3)
        t2.set_husband(p4)
        t2.add_child(p5)
        t3.set_husband(p6)
        t3.set_wife(p7)
        t3.add_child(p8)
        t4.set_husband(p6)
        t4.set_wife(p8)
        t4.add_child(p9)
     # --------------------------------------------------

        #assert p3.no_marriages_to_descendants()==True
        #assert p6.no_marriages_to_descendants()==False
        #assert p8.no_marriages_to_descendants()==True

    def test_US27_eInclude_individual_ags(self):
        SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
                        "DIV", "DATE", "HEAD", "TRLR", "NOTE"}
        self.G1 = Gedcom('testing_files/Jiashu_Wang.ged', SUPPORT_TAGS)
        G2 = Gedcom('testing_files/MichealFahimGEDCOM.ged', SUPPORT_TAGS)
        G3 = Gedcom('testing_files/mock-family.ged', SUPPORT_TAGS)
        # --------------------------------------------------
        '''
        assert self.G1.include_individual_ages() == True
        assert G2.include_individual_ages() == True
        assert G3.include_individual_ages() == True
        '''


    def test_US28_Order_siblings_by_age(self):
        t1 = Family("t1")
        t2 = Family("t2")
        p1 = Individual("p1")
        p1.set_birthDate((1990, 4, 1))
        p2 = Individual("p2")
        p2.set_birthDate((1990, 1, 1))
        p3 = Individual("p3")
        p3.set_birthDate((1990, 9, 1))
        p4 = Individual("p4")
        p4.set_birthDate((1987, 1, 1))
        p5 = Individual("p5")
        p5.set_birthDate((2019, 1, 1))
        p6 = Individual("p6")
        p6.set_birthDate((2017, 5, 30))
        p7 = Individual("p7")
        p7.set_birthDate((2018, 3, 30))
        p8 = Individual("p8")
        p8.set_birthDate((2019, 8, 30))
        # --------------------------------------------------
        t1.add_child(p1)
        t1.add_child(p2)
        t1.add_child(p3)
        t1.add_child(p4)
        t1.add_child(p5)
        t1.add_child(p6)
        t2.add_child(p1)
        t2.add_child(p2)
        t2.add_child(p3)
        t2.add_child(p4)
        t2.add_child(p7)
        t2.add_child(p8)
        # --------------------------------------------------
        assert t1.order_siblings_by_age() == [p4, p2, p1, p3, p6, p5]
        assert t2.order_siblings_by_age() == [p4, p2, p1, p3,p7,p8]



    def test_US20_Aunts_and_uncles(self):
        t1 = Family("t1")
        t2 = Family("t2")
        t3 = Family("t3")
        t4 = Family("t4")
        t5 = Family("t5")
        t6 = Family("t6")
        t7 = Family("t7")
        t8 = Family("t8")
        t9 = Family("t9")
        t10 = Family("t10")
        t11 = Family("t11")
        t12 = Family("t12")
        p1 = Individual("p1")
        p2 = Individual("p2")
        p3 = Individual("p3")
        p4 = Individual("p4")
        p5 = Individual("p5")
        p6 = Individual("p6")
        p7 = Individual("p7")
        p8 = Individual("p8")
        p9 = Individual("p9")
        p10 = Individual("p10")
        p11 = Individual("p11")
        # --------------------------------------------------
        p11.set_parentFamily(t1)
        t1.set_husband(p1)
        t1.set_wife(p2)
        p1.set_parentFamily(t2)
        p2.set_parentFamily(t3)
        #t2.set_husband(p3)
        #t2.set_wife(p4)
        #t3.set_husband(p5)
        #t3.set_wife(p6)
        t2.set_children([p1, p7, p8])
        t3.set_children([p2, p9, p10])
        

        '''
        t1.add_child(p3)
        t1.add_child(p4)
        t2.set_husband(p3)
        t3.set_wife(p4)
        t2.add_child(p5)
        t3.add_child(p6)

        t4.set_husband(p7)
        t4.set_wife(p8)
        t4.add_child(p9)
        t4.add_child(p10)
        t5.set_husband(p9)
        t5.add_child(p11)
        t6.set_husband(p10)
        t6.set_wife(p11)
        '''
        # --------------------------------------------------
        assert p11.aunts_and_uncles()==True
        #assert p10.aunts_and_uncles()==False

    def test_US26_Corresponding_entries(self):
        SUPPORT_TAGS = {"INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
                        "DIV", "DATE", "HEAD", "TRLR", "NOTE"}
        self.G1 = Gedcom('testing_files/Jiashu_Wang.ged', SUPPORT_TAGS)
        G2 = Gedcom('testing_files/MichealFahimGEDCOM.ged', SUPPORT_TAGS)
        G3 = Gedcom('testing_files/mock-family.ged', SUPPORT_TAGS)
        # --------------------------------------------------
        assert self.G1.corresponding_entries() == True
        assert G2.corresponding_entries() == True
        assert G3.corresponding_entries() == True

    def test_US29_list_deceased(self):

        self.assertEqual(self.G1.listDeceased().len(),5 )
        self.assertNotEqual(self.G1.listDeceased().len(),3 )
        deceasedPeople = []
        for indi in deceasedPeople:
            self.assertIn(indi, self.G1.listDeceased())

    #List all living married people in a GEDCOM file
    def test_US30_list_living_married(self):
        self.assertEqual(self.G1.listLivingMarried().len(),5 )
        self.assertNotEqual(self.G1.listLivingMarried().len(),3 )
        marriedPeople = []
        for indi in marriedPeople:
            self.assertIn(indi, self.G1.listLivingmarried())

    #List all living people over 30 who have never been married in a GEDCOM file
    def test_US31_list_living_single(self):
        self.assertEqual(self.G1.listLivingSingle().len(),5 )
        self.assertNotEqual(self.G1.listLivingSingle().len(),3 )
        singlePeople = []
        for indi in singlePeople:
            self.assertIn(indi, self.G1.listLivingSingle())

    #List all multiple births in a GEDCOM file
    def test_US32_list_multiple_births(self):
        self.assertEqual(self.G1.listMultipleBirths().len(),4 )
        MultipleBirths = []
        for birt in MultipleBirths:
            self.assertIn(birt, self.G1.listMultipleBirths())

    #List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
    def test_US33_list_orphans(self):

        self.assertEqual(self.G1.listOrphans().len(),4)
        OrphansPeople = []
        for indi in OrphansPeople:
            self.assertIn(indi, self.G1.listOrphans())

    #List all couples who were married when the older spouse was more than twice as old as the younger spouse
    def test_US34_list_large_age_differences(self):
        self.assertEqual(self.G1.listLargeAgeDifferences().len(),4 )
        ageDifferences = []
        for birt in ageDifferences:
            self.assertIn(birt, self.G1.listLargeAgeDifferences())

    #List all people in a GEDCOM file who were born in the last 30 days
    def test_US35_list_recent_births(self):

        self.assertEqual(self.G1.listRecentBirths().len(),5 )
        self.assertNotEqual(self.G1.listRecentBirths().len(),3 )
        bornPeople =[]
        for indi in bornPeople:
            self.assertIn(indi, self.G1.listRecentBirths())


    #list all people in a GEDCOM file who died in the last 30 days
    def test_US36_ListRecentDeaths(self):

        self.assertEqual(self.G1.listRecentDeaths().len(), 5)
        self.assertNotEqual(self.G1.listRecentDeaths().len(), 3)

        #manually input deceased people and append to the array
        deceasedProple =[]
        for indi in deceasedProple:
            self.assertIn(indi, self.G1.listRecentDeaths())

    #list all living spouses and descendants of people in the GEDCOM who died in the last 30 days
    def test_US37_listRecentSurvivors(self):
        self.assertEqual(self.G1.listRecentSurviors().len(),7)
        self.assertNotEqual(self.G1.listRecentSurviors().len(), 8)
        # manually input deceased people's relatives and append to the array
        deceasedProple = []
        for indi in deceasedProple:
            self.assertIn(indi, self.G1.listRecentSurviors())


    #list all living people in a GEDCOM file whose birthdays occur in the next 30 days
    def test_US38_listUpcomingBirthdays(self):
        self.assertEqual(self.G1.listUpcomingBirthdays().len(),6)
        #manually input people with birthdays
        birthdayPeople =[]
        for indi in birthdayPeople:
            self.assertIn(indi, self.G1.listUpcomingBirthdays())

    # list all living people in a GEDCOM file whose marriage anniversaries occur in the next 30 days
    def test_US39_UpcomingAnniversaries(self):
        self.assertEqual(self.G1.upcomingAnniversaries().len(),4)
        #manually input individuals who have anniversaries coming up
        AnniversaryIndi = []
        for indi in AnniversaryIndi:
            self.assertIn(indi, self.G1.upcomingAnniversaries())

    # list line numbers from GEDCOM source file when reporting errors
    def test_US40_includeInputLineNumbers(self):

        self.assertEqual(self.G1.includeInputLineNumbers().len(), 2)

        self.assertTrue(self.G1.includeInputLineNumbers() == ['20','25'])

        self.assertTrue(self.G2.includeInputLineNumbers() == ['15'])

    # Accept and use dates without days or without days and months
    def test_US41_IncludePartialDates(self):
        self.assertTrue(self.G1.IncludePartialDates())


    # All dates should be legitimate dates for the months specified(e.g. 2/30/2015 is not legitimate)
    def test_US42_RejectIllegitimateDates(self):
        self.assertTrue(self.G1.rejectIllegitimateDates())
        self.assertFalse(self.G2.rejectIllegitimateDates())





    def testInputValidation(self):
        pass


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
