import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from collections import Counter
from openai import OpenAI


def call_gpt(client, prompt, model="gpt-3.5-turbo", temperature=0.1):

    pre_prompt = "If the sentence is true, answer: 'Yes'. If not, answer 'No'. Here's the sentence: "

    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": pre_prompt},
                  {"role": "user", "content": prompt}],
                  temperature=temperature)
    return completion.choices[0].message.content
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


def count_words(text, n):
    tokenized_text = word_tokenize(text)
    word_counts = Counter(tokenized_text)
    most_common_words = dict(word_counts.most_common(n))
    return most_common_words


def clean_text(text,
               language="english",
               words_to_remove=["said"],
               remove_punctuation=True,
               remove_url=True,
               remove_numbers=True,
               remove_small_words=True,
               lemma=True):
    
    text = text.lower()

    text = re.sub(r'\s+', ' ', text)

    if remove_punctuation:
        text = re.sub(r'[^\w\s]', ' ', text) 

    if remove_url:
        text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text) # remove url links

    if remove_numbers:
        text = re.sub(r'\d+', '', text) 

    if remove_small_words:
        text = re.sub(r'\b\w{1,3}\b', '', text) 

    if lemma:
        lemmatizer = WordNetLemmatizer()
        text = " ".join([lemmatizer.lemmatize(word) for word in text.split()])

    stop_words = set(stopwords.words(language))
    stop_words.update(words_to_remove)
    words = nltk.word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    return " ".join(words)