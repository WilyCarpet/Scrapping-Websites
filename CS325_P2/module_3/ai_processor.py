# The program contains the LLMConciser class. The class is initialized with an article text
# The class as the function generate_concise_description which will take in an article text
# and put it into a prompt variable where it will ask to make the article concise
#  and give it a title. Using the openai api it will use your api key to send it over
# to chat gpt and generate a response back. The response is saved inot concise_description
#  and is then returned. 

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    #Enter API Key here, useing the python-dotenv module I stored my key inside of a .env file and then pulled from there so 
    #it wouldn't be in the source code  
    
    api_key= os.getenv("OPENAI_API_KEY"),
)


class LLMConciser:
    def __init__(self,article_text):
        self.article_text = article_text

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
        concise_description = response.choices[0].text
        return concise_description