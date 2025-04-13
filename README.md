# My Zootopia 
is designed for showcasing how to let a user
search an online api like
[api-ninjas animals api](https://api-ninjas.com/api/animals)
and create an HTML file from specific entries of the found data

## Key Features
* Search for an animal name to get the following data:
  * for all animals that contain your search word, get
    * name
    * diet
    * location data if present
    * prey data if present

## Installation

To install this project, simply clone the repository and install the dependencies.
If you want to use the data fetcher, you need to register at https://api-ninjas.com for free
and create a .env file containing your personal api key. The .env just needs the following line:
API_KEY="your key"

## Usage

To use this project, run the following command - "python animals_web_generator.py"
remember to first create your own .env file or update the API_KEY variable on the data_fetcher site
with your own api key.

## Contributing

I allways welcome contributions and suggestions. Remember however that this is an exercise
from the masterschool SE learning course, and therefor I might not find the time to revisit the project
once it's finished and graded.
