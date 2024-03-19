# Website Scrapper
This program uses the requests and the BeautifulSoup modules to grab a websites hTML and scrape it for the text inside the article tag

## How to install the environment
1. Download the requirements.yaml
2. Then you want to inport the environment using conda
    > - conda env create -f requirements.yaml


## How to run the program
1. Open up the environment
2. Replace the 'raw/articles.text' with your articles text file
3. Run the program inside the environment
    > - python websiteScrapper.py
4. The new scrapped web articles will be inside the processed file
