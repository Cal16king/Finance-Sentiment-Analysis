import json
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

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
most_common_bad = bad_words.most_common(10)  # top 10
most_common_good = good_words.most_common(10)  # top 10

# Create bar plots for most common words
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # Left plot
sns.barplot(x=[word for word, count in most_common_bad], y=[count for _, count in most_common_bad])
plt.title("Top 10 'Bad' Words")
plt.xlabel("Words")
plt.ylabel("Count")

plt.subplot(1, 2, 2)  # Right plot
sns.barplot(x=[word for word, count in most_common_good], y=[count for _, count in most_common_good])
plt.title("Top 10 'Good' Words")
plt.xlabel("Words")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# Generate word clouds for 'bad' and 'good' sentiments
bad_wordcloud = WordCloud(width=400, height=300, background_color='white').generate_from_frequencies(bad_words)
good_wordcloud = WordCloud(width=400, height=300, background_color='white').generate_from_frequencies(good_words)

# Plot word clouds
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # Left plot
plt.imshow(bad_wordcloud, interpolation='bilinear')
plt.title("Word Cloud for 'Bad' Sentiment")
plt.axis("off")

plt.subplot(1, 2, 2)  # Right plot
plt.imshow(good_wordcloud, interpolation='bilinear')
plt.title("Word Cloud for 'Good' Sentiment")
plt.axis("off")

# plt.tight_layout()
plt.show()
