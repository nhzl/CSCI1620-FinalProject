from bs4 import BeautifulSoup
from view import Ui_JobSearch

import requests
from PyQt5.QtWidgets import *
import time


class Controller(QMainWindow, Ui_JobSearch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.search(self.searchBox.toPlainText(), self.searchBox_2.toPlainText()))
        self.resetButton.clicked.connect(lambda: self.reset())

    def search(self, a, b):
        if self.siteIndeed.isChecked():
            self.indeed(a, b)
        if self.siteLinkedin.isChecked():
            self.linkedin(a, b)
        if self.siteGoogle.isChecked():
            self.simply(a, b)

    def indeed(self, a, b):
        i = 0
        url = 'https://www.indeed.com/jobs?as_and=' + a + '&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l=' + b + '%2C%20NE&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=ae9008d2f6729286'
        result = requests.get(url)

        soup = BeautifulSoup(result.content, 'html.parser')

        # jobCard = soup.find_all('div', class_='slider_item')
        self.listWidget.addItem("Indeed: Title /// Company /// Location")
        for i in range(0, 3):
            jobName = soup.find_all('h2')[i].get_text()
            companyName = soup.find_all('span', class_='companyName')[i].get_text()
            companyLocation = soup.find_all('div', class_='companyLocation')[i].get_text()
            salary = soup.find_all('div', class_='metadata salary-snippet-container')[i].get_text()
            if 'new' in jobName:
                jobName = jobName.lstrip('new')
            elif '*' in jobName:
                jobName = jobName.rstrip()
            self.listWidget.addItem(f"{jobName} /// {companyName} /// {companyLocation}")
            i += 1

        # print(jobCard[1].prettify())

    def linkedin(self, a, b):
        i = 0
        url = 'https://www.linkedin.com/jobs/search?keywords=' + a + '&location=' + b + '&geoId=102457028&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
        result = requests.get(url)

        soup = BeautifulSoup(result.content, 'html.parser')
        self.listWidget.addItem("Linkedin: Title /// Company /// Location")

        # linkjobCard = soup.find_all('div', class_='base-search-card__info')
        for i in range(0, 3):
            linkjobName = soup.find_all('h3', class_='base-search-card__title')[i].text.rstrip().lstrip()
            linkcompanyName = soup.find_all('h4', class_='base-search-card__subtitle')[i].text.rstrip().lstrip()
            linkcompanyLocation = soup.find_all('span', class_='job-search-card__location')[
                i].get_text().rstrip().lstrip()
            # linksalary = soup.find_all('span', class_='job-search-card__salary-info')[i].get_text()
            if 'new' in linkjobName:
                linkjobName = linkjobName.lstrip('new')
            elif '*' in linkjobName:
                linkjobName = linkjobName.rstrip()
            self.listWidget.addItem(f"{linkjobName} /// {linkcompanyName} /// {linkcompanyLocation}")
            i += 1

    def simply(self, a, b):
        i = 0
        url = 'https://www.simplyhired.com/search?q=' + a + '&l=' + b + '%2C+NE'
        result = requests.get(url)
        soup = BeautifulSoup(result.content, 'html.parser')
        # simplyjobCard = soup.find_all('div', class_='tl-item-selected')
        self.listWidget.addItem("SimplyHired: Title /// Company /// Location")
        for i in range(0, 3):
            simplyjobName = soup.find_all('h3', class_='jobposting-title')[i].text
            simplycompanyName = soup.find_all('span', class_='JobPosting-labelWithIcon jobposting-company')[
                i].get_text()
            simplycompanyLocation = soup.find_all('span', class_='jobposting-location')[i].get_text()
            simplysalary = soup.find_all('div', class_='jobposting-salary SerpJob-salary')[i].get_text()
            if 'new' in simplyjobName:
                simplyjobName = simplyjobName.lstrip('new')
            elif '*' in simplyjobName:
                simplyjobName = simplyjobName.rstrip()
            self.listWidget.addItem(f"{simplyjobName} /// {simplycompanyName} /// {simplycompanyLocation}")
            i += 1
        # print(googjobCard[1].prettify())


    def reset(self):
        x = '6'
        self.searchBox.
