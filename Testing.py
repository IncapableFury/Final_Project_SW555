"""
Test cases go in here
Van comment for second time
"""

import unittest
from models.Individual import Individual
from models.Family import Family
from models import Gedcom


class TestTriangles(unittest.TestCase):
    def test_no_marriages_to_descendants(self):
        i1 = Individual("i1")
        i1.set_gender("M")
        i2 = Individual("i2")
        i3 = Individual("i3")
        i4 = Individual("i4")
        i5 = Individual("i5")
        i6 = Individual("i6")
        i7 = Individual("i7")
        # ----------------------------------
        f1 = Family("f1")
        f2 = Family("f2")
        f3 = Family("f3")
        f1.set_husband(i1)
        i1.add_to_family(f1)
        f1.set_wife(i2)
        i2.add_to_family(f2)
        f1.add_child(i3)
        f1.add_child(i4)
        # ---------------
        # f2.set_husband(i1)
        # f2.set_wife(i4)
        # i1.add_to_family(f2)
        # i4.add_to_family(f2)
        # ------------
        f3.set_husband(i5)
        f3.set_wife(i3)
        i3.add_to_family(f3)
        i5.add_to_family(f3)
        f3.add_child(i6)
        f3.add_child(i7)
        assert i1.no_marriages_to_descendants() == True


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
