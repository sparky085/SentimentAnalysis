#!/usr/bin/env /opt/homebrew/bin/python3.9

import nltk
##nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define a function to perform sentiment analysis
def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return 'Positive'
    elif sentiment['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Example usage
text1 = "I love this product! It works perfectly."
text2 = "This movie was terrible. I hated it."
text3 = "The weather is nice today."

print(analyze_sentiment(text1))
print(analyze_sentiment(text2))
print(analyze_sentiment(text3))
