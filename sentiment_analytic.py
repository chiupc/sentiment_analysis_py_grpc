import pandas as pd
import numpy as np
import logging
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class sentiment_analytic():
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, filename, col):
        try:
            df = pd.read_csv(filename)
            df = df.dropna()
            df['score'] = df[col].astype('str').apply(lambda x: self.analyzer.polarity_scores(x)['compound'])
            df['sentiment'] = df.score.apply(lambda x: self.labelSentiment(x))
            df.to_csv(filename, header=True, index=False)
            return filename
        except Exception as e:
            logging.log(logging.ERROR, e)
            return "error"

    def labelSentiment(self, score):
        if score < 0:
            return 'negative'
        elif score == 0:
            return 'neutral'
        else:
            return 'positive'

    def get_sentiment_summary(self, fileName):
        df = pd.read_csv(fileName)
        sentiment_dist = (df.sentiment.value_counts() / len(df.index)).to_json() #return sentiment distribution in json
        return sentiment_dist