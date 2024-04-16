import json
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Load the JSON data
with open('results.json', 'r') as file:
    data = json.load(file)

# Initialize counters for "bad" and "good" sentiments
bad_words = Counter()
good_words = Counter()

# Stopwords to filter out common words
stop_words = set(stopwords.words('english'))

# Function to clean, tokenize, and filter nouns and adjectives
def process_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    tagged = pos_tag(filtered_tokens)
    nouns_adjectives = [word for word, tag in tagged if tag.startswith('NN') or tag.startswith('JJ')]
    return nouns_adjectives

# Loop through each item and count words based on sentiment
for text, attributes in data['data'].items():
    words = process_text(text)
    if attributes['sentiment'] == 'bad':
        bad_words.update(words)
    elif attributes['sentiment'] == 'good':
        good_words.update(words)

# Get the most common words for each sentiment
most_common_bad = bad_words.most_common(15)
most_common_good = good_words.most_common(15)

print('\n\n\n\n',"Most common nouns and adjectives for 'bad' sentiment:", most_common_bad, '\n\n\n\n')
print("Most common nouns and adjectives for 'good' sentiment:", most_common_good, '\n\n\n\n')
