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
        i= 0
        search_term = self.searchBox.toPlainText()
        location_term = self.searchBox_2.toPlainText()
        url = 'https://www.indeed.com/jobs?as_and=' + search_term + '&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l=' + location_term + '%2C%20NE&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=ae9008d2f6729286'
        result = requests.get(url)

        soup = BeautifulSoup(result.text, 'html.parser')

        job = soup.find_all('div', class_='slider_item')

        #job_title = job.find('span', attrs={'title'})

        #employer_name = job.find(text ='companyName')

        #location = job.find(text ='companyLocation')

        print(job[1].prettify())

        #self.listWidget.addItem()

    #def linkedin(self):
        #url = 'https://www.linkedin.com/jobs/search/?geoId=100739428&keywords=' + search_term + '&location=' + location_term
    #def google(self):
        #url = 'https://www.google.com/search?q=' + search_term + '&rlz=1C1CHBF_en&oq=google+job+s&aqs=chrome.1.69i57j0i433i512j0i512l5j0i10i512j0i512l2&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&sqi=2&ved=2ahUKEwjs1ZLLptH3AhWchP0HHcjsCNgQutcGKAF6BAggEAY&sxsrf=ALiCzsYk8LG6xYJPn7SALKDVStz4i5QVQg:1652060938618#fpstate=tldetail&htivrt=jobs&htichips=city:8WYPEnHkrIl-8kaKidp64Q%3D%3D&htischips=city;8WYPEnHkrIl-8kaKidp64Q%3D%3D:' + location_term +'&htidocid=LQQoNIk0r3cAAAAAAAAAAA%3D%3D'
    #def ziprecruiter(self):
        #url = 'https://www.ziprecruiter.com/jobs-search?search=' search_term + '&location=' + location_term



    def reset(self):
        x = '6'
        self.listWidget.addItem(x)
