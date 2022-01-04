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

![markov_diagram](https://user-images.githubusercontent.com/78571802/148133690-19f915e5-c53d-4169-99d2-61d1402faf05.png)

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

<img src="images/endpoints_shazam_api.png" alt="endpoints" height="400"/>

- **@ World Chart by Genre** endpoint: 
    - feed a genre and the limit number of songs to retrieve
    - obtain top chart for genre with trackID, artist, song name

- **@Track Details** endpoint:
    - feed trackID
    - obtain lyrics for song

We then generated a dataframe with the lyrics and dropped any chart songs for which lyrics could not be obtained through the API.

![lyrics df](images/lyrics_df.png)

### Genre Top Song Charts

![country](country_nb/images/top_artists_country.png)

![EDM](edm_nb/Images/EDM_topartists.png)

![Hip Hop](hiphop_rnb_data/Images/hiphoprap_topcharts.png)

![RnB](hiphop_rnb_data/Images/rnb_topcharts.png)

![POP](hiphop_rnb_data/Images/pop_topcharts.png)

![Rock](rock_nb/Images/rock_top_artists.png)


## Sentiment Analysis

![country-sent](country_nb/images/country_sentiment_pie.png)

![EDM](edm_nb/Images/EDM_sentiment.png)

![Hip Hop](hiphop_rnb_data/Images/hiphop_sentiment_pie.png)

![RnB](hiphop_rnb_data/Images/rnb_sentiment.png)

![POP](hiphop_rnb_data/Images/pop_sentiment.png)

![Rock](rock_nb/Images/rock_sentiment_pie.png)


## Ngrams and Frequency Analysis

### Top Word Frequency Analysis

![country](country_nb/images/top_words_country.png)

![EDM](edm_nb/Images/EDM_topwords.png)

![hiphop](hiphop_rnb_data/Images/top_words_hiphop_bar.png)

![RnB](hiphop_rnb_data/Images/top_words_rnb_bar.png)

![POP](hiphop_rnb_data/Images/top_words_pop_bar.png)

![Rock](rock_nb/Images/rock_top_words.png)


## Named Entity Recognition

![country-ner](country_nb/images/country_ner_freqs.png)

![EDM](edm_nb/Images/EDM_named_entities.png)

![hiphop](hiphop_rnb_data/Images/entities_count_hiphop.png)

![RnB](hiphop_rnb_data/Images/entities_count_rnb.png)

![POP](hiphop_rnb_data/Images/entities_count_pop.png)

![Rock](rock_nb/Images/Rock_NER_entities.png)

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

### Rock

![Rock](rock_nb/Images/Rock.png)


## Next Word Prediction

We used Google's Text-To-Speech library to generate mp4 files of our Markov Chains and AI generated lyrics. 

![gtts](images/gtts.png)

### Here is a look at our code with Markov Chains
![markov_gif](https://user-images.githubusercontent.com/78571802/148111847-1577f6eb-9936-42cf-83cc-7abdd400b69d.gif)

### Here is a look at our code with Maximum Likelihood Estimator
![mle_gif](https://user-images.githubusercontent.com/78571802/148111899-4bfbd4e3-b225-4bc0-a1f3-46c8fdef0ee9.gif)

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

### Snippet of Rock Markov
https://user-images.githubusercontent.com/86018812/148119641-90848fd8-6bd8-4d09-8b4a-1ccf039f0b4e.mp4

### Pop Text MLE Algorithm
https://user-images.githubusercontent.com/78571802/147999052-7a7eaa10-e389-4bdb-bf99-449a0c4c0fe0.mp4

### Snippet of Pop MLE Algorithm
https://user-images.githubusercontent.com/78571802/148133094-b3e24bdb-d81d-4384-857c-41e2964fb45f.mp4





### Model Scores

*MLE is an N-gram model Algorithm*

![scores](images/n-gram-modeling.PNG)


Some examples from the Country Lyrics Model:

The probability of 'woman' appearing in the text is: 0.00139

The probability of 'feel like' to be followed by 'a' is: 0.5

The probability of 'feel like a' to be followed by woman' is: 1.0

![unigram](country_nb/images/unigram_scores_mle.png)

![jingle](country_nb/images/jingle-mle-scores.png)


#### Perplexity

![perplexity](images/perplexity.png)

From the Country Lyrics Model:

The perplexity of 'aliens are' is: inf

The perplexity of 'old man' is: 7.667

The perplexity of 'bell rock' is: 3.4

The perplexity of 'jingle bell' is: 1.333

The perplexity of 'country boy' is: 1.273


Feel free to read up more on [Perplexity and Language Models](https://towardsdatascience.com/perplexity-in-language-models-87a196019a94) or watch this [video](https://www.youtube.com/watch?v=NCyCkgMLRiY&ab_channel=ArtificialIntelligence-AllinOne).

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


- Detokenizer: Returned text is readable, but lacking in punctuation and paragraph structure.

- NER: The Person and GPE Named entities were greatly mis-identified by the Spacy's NER. The image below is from the country dataset.

    ![limitations NER](country_nb/images/ner_limitations.png)

---

### Miami FinTech Bootcamp 2021-2022

#### Monique Ferguson, Andrew Hidalgo, Frank Lau and Marcela Castaño

[^1]: https://brilliant.org/wiki/markov-chains/
