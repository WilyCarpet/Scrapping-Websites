#This python program will import in classes from module_1 and module_2 and combine thme into the ScrapeArticle class
#Which will take in a url and use the scrapper class to extrac a soup object which then the extract class will use to
#write the articles into their respective text files

from module_1 import scrapper as websiteScrap
from module_2 import file_handling as websiteExtract

class ScrapeArticle:
    def __init__(self,url):
        self.url = url

    def scrape_article(self):

        file = websiteScrap.BeautifulSoupScrapper()
        file.requestURL(self.url)
        soup = file.extract()
        
        extracter = websiteExtract.Extract(soup,self.url)
        extracter.extractArticle()

with open('raw/articles.text','r') as file:
    urls = file.readlines()

for url in urls:
    article = ScrapeArticle(url.strip())
    article.scrape_article()