import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Load the dataset from CSV
data = pd.read_csv("C:/Users/koppo/OneDrive/Documents/Book1.csv")
feedback_column = data['feedback']

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    return tokens

# Process the feedback data
all_tokens = []
for feedback in feedback_column:
    tokens = preprocess_text(feedback)
    all_tokens.extend(tokens)

# Calculate word frequency distribution
word_freq = Counter(all_tokens)

# Get user input for N
try:
    N = int(input("Enter the value of N for top N words: "))
except ValueError:
    print("Invalid input. Using default value N=10.")
    N = 10

# Display the top N words and their frequencies
top_words = word_freq.most_common(N)
print(f"Top {N} most frequent words:")
for word, freq in top_words:
    print(f"{word}: {freq}")

# Create lists for plotting
words = [word for word, _ in top_words]
frequencies = [freq for _, freq in top_words]

# Plot the bar graph
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies)
plt.xlabel('Words')
plt.ylabel('Frequencies')
plt.title(f'Top {N} Most Frequent Words')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
