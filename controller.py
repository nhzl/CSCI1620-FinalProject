from bs4 import BeautifulSoup
from view import Ui_MainWindow

import requests
from PyQt5.QtWidgets import *
import time



class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.search())
        self.resetButton.clicked.connect(lambda: self.reset())

    def search(self):
        if self.siteIndeed.isChecked():
            self.indeed()
        if self.siteLinkedin.isChecked():
            self.linkedin()
        #if self.siteZiprecruiter.isChecked():
            #self.ziprecruiter()
        if self.siteGoogle.isChecked():
            self.simply()






    def indeed(self):
        i= 0
        search_term = self.searchBox.toPlainText()
        location_term = self.searchBox_2.toPlainText()
        url = 'https://www.indeed.com/jobs?as_and=' + search_term + '&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l=' + location_term + '%2C%20NE&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=ae9008d2f6729286'
        result = requests.get(url)

        soup = BeautifulSoup(result.content, 'html.parser')

        #jobCard = soup.find_all('div', class_='slider_item')
        for i in range(0,3):
            jobName = soup.find_all('h2')[i].get_text()
            companyName = soup.find_all('span',class_= 'companyName')[i].get_text()
            companyLocation = soup.find_all('div',class_= 'companyLocation')[i].get_text()
            salary = soup.find_all('div',class_= 'metadata salary-snippet-container')[i].get_text()
            if 'new' in jobName:
                jobName = jobName.lstrip('new')
                self.listWidget.addItem(jobName)
            elif '*' in jobName:
                jobName = jobName.rstrip()
                self.listWidget.addItem(jobName)
            else:
                self.listWidget.addItem(jobName)
            self.listWidget.addItem(companyName)
            self.listWidget.addItem(companyLocation)
            self.listWidget.addItem(salary)
            i+=1

        #print(jobCard[1].prettify())

    def linkedin(self):
        i = 0
        search_term = self.searchBox.toPlainText()
        location_term = self.searchBox_2.toPlainText()
        url = 'https://www.linkedin.com/jobs/search?keywords=' + search_term + '&location=' + location_term + '&geoId=102457028&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
        result = requests.get(url)

        soup = BeautifulSoup(result.content, 'html.parser')

        #linkjobCard = soup.find_all('div', class_='base-search-card__info')
        for i in range(0,3):
            linkjobName = soup.find_all('h3',class_='base-search-card__title')[i].text.rstrip().lstrip()
            linkcompanyName = soup.find_all('h4', class_='base-search-card__subtitle')[i].text.rstrip().lstrip()
            linkcompanyLocation = soup.find_all('span', class_='job-search-card__location')[i].get_text().rstrip().lstrip()
            #linksalary = soup.find_all('span', class_='job-search-card__salary-info')[i].get_text()
            if 'new' in linkjobName:
                linkjobName = linkjobName.lstrip('new')
                self.listWidget.addItem(linkjobName)
            elif '*' in linkjobName:
                linkjobName = linkjobName.rstrip()
                self.listWidget.addItem(linkjobName)
            else:
                self.listWidget.addItem(linkjobName)
            self.listWidget.addItem(linkcompanyName)
            self.listWidget.addItem(linkcompanyLocation)
            #if linksalary.isalpha():
                #self.listWidget.addItem(linksalary)
            #else:
                #continue
            i += 1
        #print(linkjobCard[1].prettify())

    def simply(self):
        i = 0
        search_term = self.searchBox.toPlainText()
        location_term = self.searchBox_2.toPlainText()
        url = 'https://www.simplyhired.com/search?q='+search_term+'&l='+location_term+'%2C+NE'
        result = requests.get(url)
        soup = BeautifulSoup(result.content, 'html.parser')
        #simplyjobCard = soup.find_all('div', class_='tl-item-selected')
        for i in range(0, 3):
            simplyjobName = soup.find_all('h3', class_='jobposting-title')[i].text
            simplycompanyName = soup.find_all('span', class_='JobPosting-labelWithIcon jobposting-company')[i].get_text()
            simplycompanyLocation = soup.find_all('span', class_='jobposting-location')[i].get_text()
            simplysalary = soup.find_all('div', class_='jobposting-salary SerpJob-salary')[i].get_text()
            if 'new' in simplyjobName:
                simplyjobName = simplyjobName.lstrip('new')
                self.listWidget.addItem(simplyjobName)
            elif '*' in simplyjobName:
                simplyjobName = simplyjobName.rstrip()
                self.listWidget.addItem(simplyjobName)
            else:
                self.listWidget.addItem(simplyjobName)
            self.listWidget.addItem(simplycompanyName)
            self.listWidget.addItem(simplycompanyLocation)
            self.listWidget.addItem(simplysalary)
            i += 1
        #print(googjobCard[1].prettify())

    """def ziprecruiter(self):
        i = 0
        search_term = self.searchBox.toPlainText()
        location_term = self.searchBox_2.toPlainText()
        url = 'https://www.ziprecruiter.com/candidate/search?form=jobs-landing&search=' + search_term + '&location=' + location_term
        result = requests.get(url)

        soup = BeautifulSoup(result.content, 'html.parser')

        #zipjobCard = soup.find_all('div', class_='job_content')
        for i in range(0, 3):
            zipjobName = soup.find_all('h2')[i].get_text()
            #linkcompanyName = soup.find_all('h4', class_='base-search-card__subtitle')[i].text.rstrip().lstrip()
            #linkcompanyLocation = soup.find_all('span', class_='job-search-card__location')[i].get_text().rstrip().lstrip()
            #linksalary = soup.find_all('span', class_='job-search-card__salary-info')[i].get_text()
            self.listWidget.addItem(zipjobName)
            #self.listWidget.addItem(linkcompanyName)
            #self.listWidget.addItem(linkcompanyLocation)
            #if linksalary.isalpha():
            #self.listWidget.addItem(linksalary)
            #else:
            #continue
            i += 1
        #print(zipjobCard[1].prettify())"""



    def reset(self):
        x = '6'
        self.listWidget.addItem(x)
