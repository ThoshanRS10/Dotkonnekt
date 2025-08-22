
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

# Download necessary NLTK data
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('vader_lexicon')

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [w for w in tokens if not w in stop_words and w.isalpha()]
    return " ".join(filtered_tokens)

def analyze_sentiment(df, text_column):
    sia = SentimentIntensityAnalyzer()
    df['sentiment_score'] = df[text_column].apply(lambda x: sia.polarity_scores(str(x))['compound'])
    df['sentiment'] = df['sentiment_score'].apply(lambda c: 'Positive' if c >= 0.05 else ('Negative' if c <= -0.05 else 'Neutral'))
    return df

def interpret_query_intent(query):
    # This is a simplified intent recognition. A more complex system could use a trained classifier.
    query = query.lower()
    if 'show' in query and ('distribution' in query or 'histogram' in query):
        return 'histogram'
    if 'relationship' in query or 'correlate' in query or 'scatter' in query:
        return 'scatterplot'
    if 'summarize' in query or 'describe' in query:
        return 'summary'
    # Fallback to direct question answering
    return 'qa'

