# The program contains the LLMConciser class. The class is initialized with an article text
# The class as the function generate_concise_description which will take in an article text
# and put it into a prompt variable where it will ask to make the article concise
#  and give it a title. Using the openai api it will use your api key to send it over
# to chat gpt and generate a response back. The response is saved inot concise_description
#  and is then returned. 

# Importing openai api to allow for text generation based on the data found in "processed"
from openai import OpenAI
# Implemnenting "dotenv" to allow for use of api key without making the key public
from dotenv import load_dotenv
# Implementing "os" to allow for use of operating system functionality
import os

# Loading the api key from "dotenv"
load_dotenv()


# Opening OpenAI client
client = OpenAI(
    #Enter API Key here, useing the python-dotenv module I stored my key inside of a .env file and then pulled from there so 
    #it wouldn't be in the source code  
    
    api_key= os.getenv("OPENAI_API_KEY"),
)


# Class for generation of new article based on data from the "processed" file in "Data"
class LLMConciser:
    def __init__(self,article_text):
        self.article_text = article_text

    # Generating a consise summary of the article in "processed" that is up to 50 words with a title
    def generate_concise_description(self):
        prompt = f"Generate a title along with the concise descripton up to 50 words of this article: \"{self.article_text}\""

        # This uses openai's completions api to send over the prompt
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=1,
            max_tokens=200,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Returns the summary generated using the OpenAI api to the "concised" folder in "Data"
        concise_description = response.choices[0].text
        return concise_description