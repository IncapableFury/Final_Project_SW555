"""
Author: Dongming Ma
I grab some of the codes(unstable, and will be refactored soon) in my team project.
I reckon it would be okay since they are written by me.
"""

import unittest

from models.Individual import Individual
from models.Family import Family


# from datetime import date


class TestSprint1(unittest.TestCase):

    def test_siblings_spacing(self):
        t1 = Family("t1")
        t2 = Family("t2")
        t3 = Family("t3")
        t4 = Family("t4")
        t5 = Family("t5")
        t6 = Family("t6")
        p1 = Individual("p1")
        p1.set_birthDate((1990, 1, 1))
        p2 = Individual("p2")
        p2.set_birthDate((1990, 1, 1))
        p3 = Individual("p3")
        p3.set_birthDate((1990, 9, 1))
        p4 = Individual("p4")
        p4.set_birthDate((1990, 1, 2))
        p5 = Individual("p5")
        p5.set_birthDate((1990, 1, 3))
        p6 = Individual("p6")
        p6.set_birthDate((1990, 5, 30))
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

    def test_multiple_births_lessOrEqual_than_5(self):
        t1 = Family("t1")
        t2 = Family("t2")
        t3 = Family("t3")
        p1 = Individual("p1")
        p1.set_birthDate((1990, 1, 1))
        p2 = Individual("p2")
        p2.set_birthDate((1990, 1, 1))
        p3 = Individual("p3")
        p3.set_birthDate((1990, 1, 1))
        p4 = Individual("p4")
        p4.set_birthDate((1990, 1, 3))
        p5 = Individual("p5")
        p5.set_birthDate((1990, 1, 2))
        p6 = Individual("p6")
        p6.set_birthDate((1990, 5, 30))
        p7 = Individual("p7")
        p7.set_birthDate((1990, 1, 2))
        p8 = Individual("p8")
        p8.set_birthDate((1990, 1, 2))
        p9 = Individual("p9")
        p9.set_birthDate((1990, 9, 2))
        p10 = Individual("p10")
        p10.set_birthDate((1990, 9, 2))
        p11 = Individual("p11")
        p11.set_birthDate((1990, 9, 3))
        p12 = Individual("p12")
        p12.set_birthDate((1990, 9, 3))
        p13 = Individual("p13")
        p13.set_birthDate((1990, 9, 3))
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


if __name__ == '__main__':
    unittest.main()
    pass
