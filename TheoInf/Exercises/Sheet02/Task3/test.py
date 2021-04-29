import unittest

import task3

class TestMain(unittest.TestCase):

    def test_powZ(self):
        self.assertTrue(all([i ** j == task3.powZ(i, j) for i in range(0, 5) for j in range(0, 5)]))

    def test_binLength(self):
        self.assertTrue(all([len(str(bin(i))[2:]) == task3.binLength(i)for i in range(0, 20)]))


    def test_binTestBit(self):
        for j in range(0, 10):
            for i in range(0, len(str(bin(j)[2:]))):
                self.assertEqual(str(bin(j))[::-1][i], str(task3.binTestBit(j, i)))

    def test_ListCreate(self):
        self.assertEqual(task3.ListCreate(), 2)

    def test_ListGetLength(self):
        self.assertTrue(True)

    def test_single_element(self):
        # Empty list
        l = task3.ListCreate()
        self.assertEqual(0, task3.ListGetLength(l))
        self.assertEqual(l, 2)

        # List contianing only 0
        l = task3.ListCreate()
        l = task3.ListAppendElement(l, 0)
        self.assertEqual(1, task3.ListGetLength(l))
        self.assertEqual(l, 34)

        # List contianing only 1
        l = task3.ListCreate()
        l = task3.ListAppendElement(l, 1)
        self.assertEqual(1, task3.ListGetLength(l))
        self.assertEqual(l, 46)

        # List contianing only 5
        l = task3.ListCreate()
        l = task3.ListAppendElement(l, 5)
        self.assertEqual(1, task3.ListGetLength(l))
        self.assertEqual(l, 718)

    def test_sequence(self):
        # Empty list
        l = task3.ListCreate()
        self.assertEqual(0, task3.ListGetLength(l))
        self.assertEqual(l, 2)

        for i in range(0, 1):
            l = task3.ListAppendElement(l,  i)

        self.assertEqual(l, 2288830)


if __name__ == '__main__':
    unittest.main()