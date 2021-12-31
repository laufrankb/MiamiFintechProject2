# Project Title

(project image)

(summary of project bla bla)


# Notebooks

Access the genre of choice for notebook containing analysis:

[Country](country_nb/country_data.ipynb)

EDM

[Hip Hop](hiphop_rnb_data/hiphopraplyrics.ipynb)

Rock

[RnB](hiphop_rnb_data/rnblyrics.ipynb)

[POP](hiphop_rnb_data/poplyrics.ipynb)

# Natural Language Processing

## Data Preprocessing

### Data Acquisition

We obtained our lyric data from [Shazam Core API](https://rapidapi.com/tipsters/api/shazam-core/) at [RapidAPI.com](https://rapidapi.com/hub)

The specific API endpoints used were:

<img src="endpoints_shazam_api.png" alt="endpoints" height="400"/>


### Genre Top Song Charts

![country](country_nb/images/top_artists_country.png)

![Hip Hop](hiphop_rnb_data/Images/hiphoprap_topcharts.png)

![RnB](hiphop_rnb_data/Images/rnb_topcharts.png)

![POP](hiphop_rnb_data/Images/pop_topcharts.png)


## Sentiment Analysis

![country-sent](country_nb/images/country_sentiment_pie.png)

![Hip Hop](hiphop_rnb_data/Images/hiphop_sentiment_pie.png)

![RnB](hiphop_rnb_data/Images/rnb_sentiment.png)

![POP](hiphop_rnb_data/Images/pop_sentiment.png)


## Ngrams and Frequency Analysis

### Top Word Frequency Analysis

![country](country_nb/images/top_words_country.png)

![hiphop](hiphop_rnb_data/Images/top_words_hiphop_bar.png)

![RnB](hiphop_rnb_data/Images/top_words_rnb_bar.png)

![POP](hiphop_rnb_data/Images/top_words_pop_bar.png)


## Name entity recognition

![country-ner](country_nb/images/country_ner_freqs.png)

![hiphop](hiphop_rnb_data/Images/entities_count.png)

![RnB](hiphop_rnb_data/Images/entities_count_rnb.png)

![POP](hiphop_rnb_data/Images/entities_count_pop.png)

## Word clouds

### Country

![country](country_nb/images/country.png)

### Hip Hop

![Hip Hop](hiphop_rnb_data/Images/hiphopboom.png)

### RnB

![RnB](hiphop_rnb_data/Images/rnbart.png)

### POP

![RnB](hiphop_rnb_data/Images/popwordcloud.png)


## Next Word Prediction

- Next word prediction algorithm using the music data from a specific genre, using the following:
    - Markov Chains
    - Kneser Ney Interpolated algorithm
    

---

### Miami FinTech Bootcamp 2021-2022

#### Monique Ferguson, Andrew Hidalgo, Frank Lau and Marcela Castaño