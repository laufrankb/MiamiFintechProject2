# NLP & Machine Music

![robot_sings](https://user-images.githubusercontent.com/78571802/148107819-8f5ad3b1-6885-480d-a8d8-ad4b296bfd87.jpeg)

# Objectives

- Analyze lyric data with Natural Language Processing techniques
    - Tokenization
    - Sentiment analysis
    - N-grams, frequency analysis
    - Named entity recognition
- Become familiar with text prediction algorithms using machine learning
- Explore text prediction methodologies


# Notebooks

Access the genre of choice for notebook containing analysis:

[Country](country_nb/country_data.ipynb)

[EDM](edm_nb/edm3.ipynb)

[Hip Hop](hiphop_rnb_data/hiphopraplyrics.ipynb)

[Rock](rock_nb/rock_data.ipynb)

[RnB](hiphop_rnb_data/rnblyrics.ipynb)

[POP](hiphop_rnb_data/poplyrics.ipynb)


To view the summary for all genres, check out:

[Visualizations for All Genres](all_genres/all_genres_nb.ipynb)


# Predictive Models

- We carried out next word prediction algorithm using the music data from a specific genre, using the following:
    - Markov Chains
    - Maximum Likelihood Estimator Algorithm

## Markov Chains: Randomized text prediction

A Markov chain is a stochastic technique, but it differs from a general stochastic technique in that a Markov chain must be "memory-less." That is, (the probability of) future actions are not dependent upon the steps that led up to the present state. This is called the Markov property. [^1]

![markovgif](https://user-images.githubusercontent.com/78571802/148003935-e50d8c96-3bd6-48b1-b883-f4007ac0b17b.gif)

For more details, we recommend the following [video](https://www.youtube.com/watch?v=MGVdu39gT6k&t=394s&ab_channel=ADashofData).

## Language models with NLTK
![natural_language_toolkit](https://user-images.githubusercontent.com/78571802/148105302-8f285e93-e08f-4b48-b993-8aaef522d9ea.png)

For further reading, consider this [Medium Article](https://medium.com/swlh/language-modelling-with-nltk-20eac7e70853).

Also refer to the [MLE documentation](https://www.nltk.org/api/nltk.lm.html).

## Maximum Likelihood Estimator from NLTK
![Maximum_Likelihood_Estimation](https://user-images.githubusercontent.com/78571802/148105883-7d475804-d254-4285-8874-a88c22aec726.jpeg)

This [article](https://www.kaggle.com/alvations/n-gram-language-model-with-nltk/notebook) served as a starting point to our endeavor in text prediction.

Check out the [Language Model Module](https://www.nltk.org/api/nltk.lm.html) from NTLK for more information on the different models to choose from.

# Natural Language Processing

## Data Preprocessing

We obtained our lyric data from [Shazam Core API](https://rapidapi.com/tipsters/api/shazam-core/) at [RapidAPI.com](https://rapidapi.com/hub)

The specific API endpoints used were:

<img src="endpoints_shazam_api.png" alt="endpoints" height="400"/>

- **@ World Chart by Genre** endpoint: 
    - feed a genre and the limit number of songs to retrieve
    - obtain top chart for genre with trackID, artist, song name

- **@Track Details** endpoint:
    - feed trackID
    - obtain lyrics for song

We then generated a dataframe with the lyrics and dropped any chart songs for which lyrics could not be obtained through the API.

![lyrics df](lyrics_df.png)

### Genre Top Song Charts

![country](country_nb/images/top_artists_country.png)

![EDM](edm_nb/Images/EDM_topartists.png)

![Hip Hop](hiphop_rnb_data/Images/hiphoprap_topcharts.png)

![RnB](hiphop_rnb_data/Images/rnb_topcharts.png)

![POP](hiphop_rnb_data/Images/pop_topcharts.png)


## Sentiment Analysis

![country-sent](country_nb/images/country_sentiment_pie.png)

![EDM](edm_nb/Images/EDM_sentiment.png)

![Hip Hop](hiphop_rnb_data/Images/hiphop_sentiment_pie.png)

![RnB](hiphop_rnb_data/Images/rnb_sentiment.png)

![POP](hiphop_rnb_data/Images/pop_sentiment.png)


## Ngrams and Frequency Analysis

### Top Word Frequency Analysis

![country](country_nb/images/top_words_country.png)

![EDM](edm_nb/Images/EDM_topwords.png)

![hiphop](hiphop_rnb_data/Images/top_words_hiphop_bar.png)

![RnB](hiphop_rnb_data/Images/top_words_rnb_bar.png)

![POP](hiphop_rnb_data/Images/top_words_pop_bar.png)


## Named Entity Recognition

![country-ner](country_nb/images/country_ner_freqs.png)

![EDM](edm_nb/Images/EDM_named_entities.png)

![hiphop](hiphop_rnb_data/Images/entities_count_hiphop.png)

![RnB](hiphop_rnb_data/Images/entities_count_rnb.png)

![POP](hiphop_rnb_data/Images/entities_count_pop.png)

## Word Clouds

### Country

![country](country_nb/images/country.png)

### EDM

![EDM](edm_nb/Images/EDMwordcloud.png)

### Hip Hop

![Hip Hop](hiphop_rnb_data/Images/hiphopwordcloud.png)

### RnB

![RnB](hiphop_rnb_data/Images/rnbartwordcloud.png)

### POP

![RnB](hiphop_rnb_data/Images/popwordcloud.png)


## Next Word Prediction

We used Google's Text-To-Speech library to generate mp4 files of our Markov Chains and AI generated lyrics. 

![gtts](gtts.png)

Here are lyric snippets for each genre:

### Snippet of Country MLE Algorithm
https://user-images.githubusercontent.com/88758706/147867791-15da3590-8103-4dcc-8985-bb47984f72ad.mp4

### Snippet of EDM MLE Algorithm
https://user-images.githubusercontent.com/88758706/147998783-cf94e0ca-1ecc-458b-afba-5ed73c1e9237.mp4

### Snippet of Hip Hop Markov
https://user-images.githubusercontent.com/78571802/147998097-49ba5026-94dd-4478-94f8-34065f5601de.mp4

### Snippet of Hip Hop MLE Algorithm

https://user-images.githubusercontent.com/78571802/147998169-11a84032-4863-4f35-a7e1-63434e5df615.mp4

### Snippet of RnB Markov
https://user-images.githubusercontent.com/78571802/147998248-55b7fc05-d831-4fc8-82c4-36b73ca5e0b6.mp4

### Snippet of RnB MLE Algorithm
https://user-images.githubusercontent.com/78571802/147998991-dcebb568-14ed-433b-8bce-310863c86a1a.mp4

### Snippet of Pop Markov
https://user-images.githubusercontent.com/78571802/147999040-23548f23-577c-4792-980f-8c48bc1f1d18.mp4


### Snippet of Pop MLE Algorithm
https://user-images.githubusercontent.com/78571802/147999052-7a7eaa10-e389-4bdb-bf99-449a0c4c0fe0.mp4


### Model Scores



## Conclusions

### Summary of All Genres

Here are the overall results for the sentiment analysis:

![Sentiment](all_genres/images/overall_sentiment_pie.png)

### *VADER concluded that most of the top chart songs across genres were **Positive***

<br>

These are the most used words in the Top Chart Songs for the analyzed genres:

![Top Words](all_genres/images/all_top_words.png)


This is the word cloud for the most used words across genres:

![WC](all_genres/images/wc.png)

### *'like', 'yeah', 'know', 'got' and 'love' are the most used words across all analyzed genres.*

<br>

These are the frequencies of each Named Entity found in the Top Chart Songs for all genres:

![Entities](all_genres/images/all_entities.png)

### *The main focus across the analyzed genres seems to be **people***

<br>

### Limitations

- NER: The Person and GPE Named entities were greatly mis-identified by the Spacy's NER. The image below is from the country dataset.

    ![limitations NER](country_nb/images/ner_limitations.png)


---

[^1]: https://brilliant.org/wiki/markov-chains/

---

### Miami FinTech Bootcamp 2021-2022

#### Monique Ferguson, Andrew Hidalgo, Frank Lau and Marcela Castaño
