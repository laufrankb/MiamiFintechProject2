""" SHAZAM CORE API REQUEST """
""" TRACK DETAILS ENDPOINT """


""" This function acquires lyrics for a particular song """
""" It requires a track_id as an input """

# TRACK IDS --> number


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

def get_lyrics(querystring):

    url = "https://shazam-core.p.rapidapi.com/v1/tracks/details"

    headers = {
    'x-rapidapi-host': "shazam-core.p.rapidapi.com",
    'x-rapidapi-key': my_rapid_api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()