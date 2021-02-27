import string
from collections import Counter
import sys
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import json

with open('myfile.json', 'r', encoding="utf8") as sample_data:
    d = json.load(sample_data)
    sample_test = [str(i.get('review_text')).replace("  ", "") for i in d]

def sentiment_analyse(sentiment_text):
    lower_case = sentiment_text.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
    # Using word_tokenize because it's faster than split()
    tokenized_words = word_tokenize(cleaned_text, "english")
    # Removing Stop Words
    final_words = []
    for word in tokenized_words:
        if word not in stopwords.words('english'):
            final_words.append(word)

    # Lemmatization - From plural to single + Base form of a word (example better-> good)
    lemma_words = []
    for word in final_words:
        word = WordNetLemmatizer().lemmatize(word)
        lemma_words.append(word)
    sentiment_text=" ".join(lemma_words)

    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)

    if score['neg'] > score['pos']:

        return "Negative Sentiment"
    elif score['neg'] < score['pos']:
        return "Positive Sentiment"
    else:
        return "Neutral Sentiment"



