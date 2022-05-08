from bs4 import BeautifulSoup
from view import Ui_MainWindow
import lxml
import requests
from PyQt5.QtWidgets import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.indeed())
        self.resetButton.clicked.connect(lambda: self.reset())

    def indeed(self):
        search_term = 'software'  # self.searchBox.toPlainText()
        location_term = 'omaha'  # self.searchBox_2.toPlainText()
        url = 'https://www.indeed.com/jobs?as_and=' + search_term + '&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l=' + location_term + '%2C%20NE&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=ae9008d2f6729286'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        job = soup.find('div', class_='slider_item')

        #company_name = job.find('span', class_='companyName').text.replace(' ', '')

        self.listWidget.addItem(job)

    def reset(self):
        self.listWidget.addItem("hello world")
