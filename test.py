import unittest
from controller import*

class MyTestCase(unittest.TestCase):
    def search(self):
        with self.assertRaises(TypeError):
            search(a.isalpha(),False)

        with self.assertRaises(TypeError):
            search(b.isalpha(),False)


if __name__ == '__main__':
    unittest.main()
