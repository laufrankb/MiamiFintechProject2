""" SHAZAM CORE API REQUEST """
""" WORLD CHART BY GENRE ENDPOINT """


""" This function acquires the top songs for a particular genre """
""" It requires a genre_code """

# GENRE CODES
# POP,HIP_HOP_RAP,DANCE,ELECTRONIC,SOUL_RNB,ALTERNATIVE,ROCK,LATIN,FILM_TV,COUNTRY,
# AFRO_BEATS,WORLDWIDE,REGGAE_DANCE_HALL,HOUSE,K_POP,FRENCH_POP,SINGER_SONGWRITER,REG_MEXICO


# Imports
import requests
import os
import json
from dotenv import load_dotenv

# Load .env environment variables
load_dotenv()

# Set RAPID API key
my_rapid_api_key = os.getenv("RAPID_API_KEY")



# Define function to use Shazam Core API

def get_chart_genre(querystring):

    url = "https://shazam-core.p.rapidapi.com/v1/charts/genre-world"

    headers = {
    'x-rapidapi-host': "shazam-core.p.rapidapi.com",
    'x-rapidapi-key': my_rapid_api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()