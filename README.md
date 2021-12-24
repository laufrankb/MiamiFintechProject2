# Project Title

(project image)

(summary of project bla bla)


# Notebooks

Access the genre of choice for notebook containing analysis:

[Country](country_nb/country_data.ipynb)

EDM

[Hip Hop](Monique_data/hiphopraplyrics.ipynb)

Rock

[RnB](Monique_data/rnblyrics.ipynb)

# Natural Language Processing

## Data Preprocessing

### Data Acquisition

We obtained our lyric data from [Shazam Core API](https://rapidapi.com/tipsters/api/shazam-core/) at [RapidAPI.com](https://rapidapi.com/hub)

The specific API endpoints used are:

![endpoints](endpoints_shazam_api.png)


### Genre Top Song Charts

![country-top-songs](country_nb/images/top_artists_country.png)

![Hip Hop](Monique_data/Images/hiphoprap_topcharts.png)

![RnB](Monique_data/Images/rnb_topcharts.png)


## Sentiment Analysis

![country-sent](country_nb/images/country_sentiment_pie.png)

## Ngrams and Frequency Analysis

### Top Word Frequency Analysis

![country-top-words](country_nb/images/top_words_country.png)


## Name entity recognition

![country-ner](country_nb/images/country_ner_freqs.png)

## Word clouds

### Country

![country-wc](country_nb/images/country.png)

### Hip Hop

![Hip Hop](Monique_data/Images/hiphopboom.png)

### RnB

![RnB](Monique_data/Images/rnbart.png)


## Next Word Prediction

- Next word prediction algorithm using the music data from a specific genre, using the following:
    - Markov Chains
    - Kneser Ney Interpolated algorithm
    
### Hip Hop Song via Markov Chains

![Hip Hop](Monique_data/Images/hiphoprap_song.gif)

### RnB Song via Markov Chains

![RnB](Monique_data/Images/rnb_song.png)

---

### Miami FinTech Bootcamp 2021-2022

#### Monique Ferguson, Andrew Hidalgo, Frank Lau and Marcela Castaño