""" This script takes in a lyrics df and returns a sentiment analysis """
""" Returns scores from sentiment analysis as a dataframe with TrackID as index """

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

import nltk as nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


def lyrics_sentiment(df):

    text_sentiment = []

    for index, row in df.iterrows():
        try:
            sentiment = analyzer.polarity_scores(row['Lyrics'])
            compound = sentiment["compound"]
            pos = sentiment["pos"]
            neu = sentiment["neu"]
            neg = sentiment["neg"]
            
            text_sentiment.append({
                
                "TrackID": index,
                "compound": compound,
                "positive": pos,
                "negative": neg,
                "neutral": neu  
            })
            
        except AttributeError:
            pass

        sentiments_df = pd.DataFrame(text_sentiment).set_index('TrackID')

    return sentiments_df