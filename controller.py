from bs4 import BeautifulSoup
from view import Ui_MainWindow

import requests
from PyQt5.QtWidgets import *
import time



class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.linkedin())
        self.resetButton.clicked.connect(lambda: self.reset())

    def indeed(self):
        """i= 0
        search_term = self.searchBox.toPlainText()
        location_term = self.searchBox_2.toPlainText()
        url = 'https://www.indeed.com/jobs?as_and=' + search_term + '&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l=' + location_term + '%2C%20NE&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=ae9008d2f6729286'
        result = requests.get(url)

        soup = BeautifulSoup(result.content, 'html.parser')

        jobCard = soup.find_all('div', class_='slider_item')
        for i in range(0,10):
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



        #job_title = job.find('span', attrs={'title'})

        #employer_name = job.find(text ='companyName')

        #location = job.find(text ='companyLocation')

        print(jobCard[1].prettify())





        #self.listWidget.addItem()"""

    def linkedin(self):
        i = 0
        search_term = self.searchBox.toPlainText()
        location_term = self.searchBox_2.toPlainText()
        url = 'https://www.linkedin.com/jobs/search?keywords=' + search_term + '&location=' + location_term + '&geoId=102457028&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
        result = requests.get(url)

        soup = BeautifulSoup(result.content, 'html.parser')

        linkjobCard = soup.find_all('div', class_='base-search-card__info')
        for i in range(0,10):
            linkjobName = soup.find_all('h3',class_='base-search-card__title')[i].text.rstrip().lstrip()
            linkcompanyName = soup.find_all('h4', class_='base-search-card__subtitle')[i].text.rstrip().lstrip()
            linkcompanyLocation = soup.find_all('span', class_='job-search-card__location')[i].get_text().rstrip().lstrip()
            linksalary = soup.find_all('span', class_='job-search-card__salary-info')[i].get_text()
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
            if linksalary.isalpha():
                self.listWidget.addItem(linksalary)
            else:
                continue
            i += 1
        print(linkjobCard[1].prettify())

    #def google(self):
        #url = 'https://www.google.com/search?q=' + search_term + '&rlz=1C1CHBF_en&oq=google+job+s&aqs=chrome.1.69i57j0i433i512j0i512l5j0i10i512j0i512l2&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&sqi=2&ved=2ahUKEwjs1ZLLptH3AhWchP0HHcjsCNgQutcGKAF6BAggEAY&sxsrf=ALiCzsYk8LG6xYJPn7SALKDVStz4i5QVQg:1652060938618#fpstate=tldetail&htivrt=jobs&htichips=city:8WYPEnHkrIl-8kaKidp64Q%3D%3D&htischips=city;8WYPEnHkrIl-8kaKidp64Q%3D%3D:' + location_term +'&htidocid=LQQoNIk0r3cAAAAAAAAAAA%3D%3D'
    #def ziprecruiter(self):
        #url = 'https://www.ziprecruiter.com/jobs-search?search=' search_term + '&location=' + location_term



    def reset(self):
        x = '6'
        self.listWidget.addItem(x)
