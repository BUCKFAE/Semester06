import unittest

import task3

class TestMain(unittest.TestCase):

    def test_powZ(self):
        self.assertTrue(all([i ** j == task3.powZ(i, j) for i in range(0, 5) for j in range(0, 5)]))

    def test_binLength(self):
        self.assertTrue(all([len(str(bin(i))[2:]) == task3.binLength(i)for i in range(0, 20)]))

    def test_binTestBit(self):
        # Testing numbers from 0 to 10
        for j in range(0, 10):
            # Testing bit, str(bin(x)) starts with 0x hence we need to start at index 2
            for i in range(0, len(str(bin(j)[2:]))):
                self.assertEqual(str(bin(j))[::-1][i], str(task3.binTestBit(j, i)))

    def test_single_elements(self):
        # Empty list
        l = task3.ListCreate()
        self.assertEqual(0, task3.ListGetLength(l))
        self.assertEqual(l, 2)

        # List contianing only 0
        l = task3.ListCreate()
        l = task3.ListAppendElement(l, 0)
        self.assertEqual(1, task3.ListGetLength(l))
        self.assertEqual(0, task3.ListGetElement(l, 0))

        self.assertEqual(l, 34)

        # List contianing only 1
        l = task3.ListCreate()
        l = task3.ListAppendElement(l, 1)
        self.assertEqual(1, task3.ListGetLength(l))
        self.assertEqual(1, task3.ListGetElement(l, 0))
        self.assertEqual(l, 46)

        # List contianing only 5
        l = task3.ListCreate()
        l = task3.ListAppendElement(l, 5)
        self.assertEqual(1, task3.ListGetLength(l))
        self.assertEqual(5, task3.ListGetElement(l, 0))
        self.assertEqual(l, 718)

    def test_sequence(self):
        # Empty list
        l = task3.ListCreate()

        # Appending numbers from 0 to 3 to the list
        for i in range(0, 4):
            l = task3.ListAppendElement(l,  i)
            self.assertEqual(i + 1, task3.ListGetLength(l))
            self.assertEqual(i, task3.ListGetElement(l, i))

        self.assertEqual(l, 2288830)


if __name__ == '__main__':
    unittest.main()