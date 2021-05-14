from main import prodZ

import unittest

class TestMain(unittest.TestCase):

    def test_prodZ(self):
        self.assertEqual(prodZ(7, 43), 30)

if __name__ == '__main__':
    unittest.main()
