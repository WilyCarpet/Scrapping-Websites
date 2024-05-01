# This python program contains the class FileHandling which will take the information from the given article text
# it will then write to a text file named after its url, and in it just the one string of article information
# It will let the user know that the article was stored succesfully

# Class for file handling 
class FileHandling:
    # Initializing the class artical_text and url to the respected article_text and url
    def __init__(self,article_text,url):
        self.article_text = article_text
        self.url = url

    # Function to fetch the artical text from the file
    def getArticle(self, article_text):
        self.article_text = article_text

    # used for writing files within the processed folder
    def writeToProcessed(self):
            # with statement automatically handles file closing
            with open(f'processed/article_{self.url.strip().split("/")[-1]}.txt','w',encoding='utf-8') as file:
                file.write(self.article_text)
        
            print(f"Article scraped from {self.url} and stored successfully!")

    # used for writing files to the "concised" subfolder in "Data" folder
    def writeToConcised(self):
        # Writing the file to the "concised folder" located in the "Data" folder
        with open(f'concised/article_{self.url.strip().split("/")[-1]}.txt','w',encoding='utf-8') as file:
              file.write(self.article_text)

        print(f"Article concised from {self.url} and stored successfully!")