from bs4 import BeautifulSoup
from gui import Ui_Dialog
import requests
from PyQt5.QtWidgets import *


class Controller(QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.indeed(self))

    def indeed(self):
        search_term = self.searchBox.text()
        location_term = self.searchBox_2.text()

        url = 'https://www.indeed.com/jobs?as_and=' + search_term + '&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st' \
                                                                    '&salary&radius=25&l=' + location_term + \
              '%2C%20NE&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=ae9008d2f6729286 '

        page = requests.get(url).text

        soup = BeautifulSoup(page, 'lxml')
        job = soup.find('div', class_='slider_item')

        company_name = job.find('span', class_='companyName').text.replace(' ', '')
        location = job.find('div', class_='companyLocation').text
        title = job.find('h2', class_='jobTitle').text
        urgent = job.find('div', class_='urgentlyHiring')

        if urgent == 'None':
            urgent = 'No'
        else:
            urgent = 'Yes.'
        i = 0

        self.listWidget.addItem(f"{company_name} {location} {title} {urgent}")

        print(f'''
        Company Name: {company_name}
        Location: {location}
        Job Title: {title}
        Urgently Hiring: {urgent}
        ''')

