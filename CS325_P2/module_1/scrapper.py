#This is a python program containg the Scrapper class which will use a function to take in a given url
#With the url it will send a http request and retrive the contents of the url
#The html elements will then be parsed into a beautifulSoup object where the function extractSoup will
#return a soup object with the uneccessary elements extracted so only the article remains

#I choice the SOLID principle Open-Closed Principle (OCP) to open the possibilities to different web drivers to scrap other than beautiful soup

#Requests is an HTTP library for python that allows to send 
# HTTP requests 
import requests

#This is a Python library for pulling data out of HTML 
# and XML files.
from bs4 import BeautifulSoup

from abc import ABC, abstractmethod

class Scrapper:
    @abstractmethod
    def requestURL(self,url):
        pass
    def extract(self):
        pass

class BeautifulSoupScrapper(Scrapper):
    def __init__(self):
        self.response = None
        self.soup = None

    # Sends an HTTP GET request to the specified URL, the response
    # variable will contain the server's reponse to the HTTP request
    def requestURL(self,url):
        self.response = requests.get(url)
    
    #Return a BeautifulSoup object that has removed all uneccessary elems from the parse tree
    def extract(self):
        # When you parse HTML content using BeautifulSoup, it creats
        # a parse tree, which is a hierachical representation of the
        # HTML structure of the webpage. The line is parsing the HTML
        # content of the 'reponse' object and creates a BeautifulSoup
        # object 'soup' that represents the parsed HTML content of the
        # webpage
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

        # This line utilizes BeautifulSoup's find_all() method to locate
        # all HTML elements listed
        for elem in self.soup.find_all(['script','style','iframe','a','header','footer']):
            #Once these elements are located, the extract() method is
            #called on each of them. The extract() method removes the
            #the element from the parse tree 
            elem.extract()
        for elem in self.soup.find_all(['p','div']):
            if elem.name == 'div' and 'info' in elem.get('class', []):
                elem.extract()
            if elem.name == 'div' and 'user-input' in elem.get('class',[]):
                elem.extract()
        

        return self.soup