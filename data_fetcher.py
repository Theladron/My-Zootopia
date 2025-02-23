import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def fetch_data(user_input):
    """
    Gets json data from the api-ninjas animals api, searches
    for the term specified in the user input
    :param user_input: word to search for as str
    :return: json file as list of dicts
    """
    response = requests.get("https://api.api-ninjas.com/v1/animals?name=" + user_input, headers={"X-Api-Key": API_KEY})
    data = response.json()
    return data