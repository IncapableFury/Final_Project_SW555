import unittest
import sys
sys.path.append('../')

from models.Individual import Individual
from models.Family import Family
from models import Gedcom


class testSprint1(unittest.TestCase):

    def setUp(self):
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
            t1.set_divorced(["1", "JAN", "1999"])
            # ---------------------------------
            t2 = Family("F02")
            male2 = Individual("P03")
            female2 = Individual("P04")
            male2.set_deathDate(["5", "MAR", "2000"])
            female2.set_deathDate(["9", "APR", "2002"])
            t2.set_husband(male2)
            t2.set_wife(female2)
            t2.set_divorced(["1", "JAN", "2001"])
            # ---------------------------------
            t3 = Family("F03")
            male3 = Individual("P05")
            female3 = Individual("P06")
            male3.set_deathDate(["5", "MAR", "2000"])
            female3.set_deathDate(["9", "APR", "2002"])
            t3.set_husband(male3)
            t3.set_wife(female3)
            t3.set_divorced(["1", "JAN", "2003"])
            # ---------------------------------
            t4 = Family("F04")
            male4 = Individual("P07")
            female4 = Individual("P08")
            male4.set_deathDate(["5", "MAR", "2000"])
            t4.set_deathDate(["9", "APR", "2002"])
            t4.set_husband(male4)
            t4.set_wife(female4)
            t4.set_divorced(["1", "JAN", "2000"])
            # ---------------------------------
            t5 = Family("F05")
            male5 = Individual("P09")
            female5 = Individual("P10")
            male5.set_deathDate(["5", "MAR", "2000"])
            t5.set_deathDate(["9", "APR", "2002"])
            t5.set_husband(male5)
            t5.set_wife(female5)
            t5.set_divorced(["1", "JAN", "2002"])
            # ---------------------------------
            assert t1.divorce_before_death() == True
            assert t2.divorce_before_death() == False
            assert t3.divorce_before_death() == False
            assert t4.divorce_before_death() == True
            assert t5.divorce_before_death() == False

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

    def Test_US12_parents_not_too_old(self):
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
        t1.set_children(p3)
        t2.set_wife(p4)
        t2.set_husband(p5)
        t2.set_children(p6)
        p1.set_birthDate("1", "JAN", "1990")
        p2.set_birthDate("1", "JAN", "1990")
        p4.set_birthDate("1", "JAN", "1790")
        p5.set_birthDate("1", "JAN", "1790")
        # ---------------------------------
        assert t1.parents_not_too_old() == True
        assert t2.parents_not_too_old() == False

    def testInputValidation(self):
        pass


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

