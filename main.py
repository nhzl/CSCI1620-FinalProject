from controller import *
#import unittest

"""class test_search_input(unittest.TestCase):
    def test_string(self):
        from self.search() import
        x = self.searchBox.toPlainText()
        self.assertEqual(x.isalpha(),True)"""


def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()