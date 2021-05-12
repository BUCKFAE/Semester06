from main import DyadicRepresentation, Number, GoLeft, GoRight, main

import unittest

class TestMain(unittest.TestCase):
 
    def test_dya(self):
        # Ensuring dya from number is correct
        self.assertEqual(DyadicRepresentation(3), [1, 1])
        self.assertEqual(DyadicRepresentation(109), [2, 1, 2, 2, 2, 1])
        self.assertEqual(DyadicRepresentation(20), [1, 2, 1, 2])

        self.assertEqual(DyadicRepresentation(0), [])


    def test_number(self):
        # Ensuring number from dya is corret
        self.assertEqual(Number([1, 2, 1, 2]), 20)
        self.assertEqual(Number([0, 0, 1, 2, 1, 2]), 20)
        self.assertEqual(Number([1, 2, 1, 2, 0, 0]), 20)
        self.assertEqual(Number([0, 0, 1, 2, 1, 2, 0, 0]), 20)
        self.assertEqual(Number([2, 1, 2, 2, 2, 1]), 109)
        self.assertEqual(Number([0, 2, 1, 2, 2, 2, 1]), 109)
        self.assertEqual(Number([0, 0, 2, 1, 2, 2, 2, 1, 0]), 109)

        self.assertEqual(Number([]), 0)
        # Tests GoRight

    def test_go_right(self):
        self.assertEqual(GoRight([1, 2], 1), ([1, 2, 0], 2))
        self.assertEqual(GoRight([1, 2], 0), ([1, 2], 1))

    # Tests GoLeft
    def test_go_left(self):
        self.assertEqual(GoLeft([1, 2], 0), ([0, 1, 2], 0))
        self.assertEqual(GoLeft([1, 2], 1), ([1, 2], 0))

    # Tests of main
    def test_main(self):
        self.assertEqual(main(0), 0)
        self.assertEqual(main(1), 3)
        self.assertEqual(main(2), 6)
        self.assertEqual(main(3), 15)
        self.assertEqual(main(4), 21)
        self.assertEqual(main(6), 14)
        self.assertEqual(main(10), 0)
        self.assertEqual(main(19), 321)
        self.assertEqual(main(20), 0)
        self.assertEqual(main(23), 384)

if __name__ == '__main__':
    unittest.main()
