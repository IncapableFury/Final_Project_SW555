import unittest

from models.Individual import Individual
from models.Family import Family


class TestSprint2(unittest.TestCase):

    def test_order_siblings_by_age(self):
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
        p8 = Individual("p8")
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
        assert t2.order_siblings_by_age() == [p4, p2, p1, p3]


if __name__ == '__main__':
    unittest.main()
    pass
