from bs4 import BeautifulSoup
from view import Ui_MainWindow

import requests
from PyQt5.QtWidgets import *
import time



class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.indeed())
        self.resetButton.clicked.connect(lambda: self.reset())

    def indeed(self):
        search_term = self.searchBox.toPlainText()
        location_term = self.searchBox_2.toPlainText()
        url = 'https://www.indeed.com/jobs?as_and=' + search_term + '&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l=' + location_term + '%2C%20NE&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=ae9008d2f6729286'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')


        #company_name = job.find('span', class_='companyName').text.replace(' ', '')
        self.listWidget.addItem(soup.find('div', class_='slider_item').text)

    def reset(self):
        x = '6'
        self.listWidget.addItem(x)
