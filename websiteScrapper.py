#Requests is an HTTP library for python that allows to send 
# HTTP requests 
import requests

#This is a Python library for pulling data out of HTML 
# and XML files.
from bs4 import BeautifulSoup

def scrape_article(url):

    # Sends an HTTP GET request to the specified URL, the response
    # variable will contain the server's reponse to the HTTP request
    response = requests.get(url)

    # When you parse HTML content using BeautifulSoup, it creats
    # a parse tree, which is a hierachical representation of the
    # HTML structure of the webpage. The line is parsing the HTML
    # content of the 'reponse' object and creates a BeautifulSoup
    # object 'soup' that represents the parsed HTML content of the
    # webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # This line utilizes BeautifulSoup's find_all() method to locate
    # all HTML elements listed
    for elem in soup.find_all(['script','style','iframe','a','header','footer']):
        #Once these elements are located, the extract() method is
        #called on each of them. The extract() method removes the
        #the element from the parse tree
        elem.extract()
    
    #Find the main content of the article
    article_content = soup.find('article')
    if article_content:
        #It extracts all the text from the HTML element and its children
        #stripping away any HTML tags and stores it int a single string
        #Then it is stored into variable article_text
        article_text = article_content.get_text()

        with open(f'article_{url.strip().split("/")[-1]}.txt','w',encoding='utf-8') as file:
            file.write(article_text)
        
        print(f"Article scraped form {url} and stored successfully!")
    
    else: 
        print(f"No article content found on {url}.")

with open('articles.text','r') as file:
    urls = file.readlines()

for url in urls:
    scrape_article(url.strip())