import requests

API_KEY = "W2lsKCIZ613ogZrhdObafg==GDrSg3BXhnOk2y5e"


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