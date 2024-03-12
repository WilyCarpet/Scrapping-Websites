#This python program contains the class Extract which will take the information in the article element and turn it into one string
#it will then write to a text file named after its url, and in it just the one string of article information
#It will let the user know if the article is extraced successfully or not


from bs4 import BeautifulSoup


class Extract:
    def __init__(self,soup,url):
        self.soup = soup
        self.url = url

    def extractArticle(self):
        #Find the main content of the article
        article_content = self.soup.find('article')
        if article_content:
        #It extracts all the text from the HTML element and its children
        #stripping away any HTML tags and stores it int a single string
        #Then it is stored into variable article_text
            article_text = article_content.get_text()

            #with statement automatically handles file closing
            with open(f'processed/article_{self.url.strip().split("/")[-1]}.txt','w',encoding='utf-8') as file:
                file.write(article_text)
        
            print(f"Article scraped form {self.url} and stored successfully!")

        else: 
            print(f"No article content found on {self.url}.")