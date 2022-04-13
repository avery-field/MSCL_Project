#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:52:38 2022

@author: averyfield2
"""

import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk

df1 = pd.read_csv (r'/Path/to_topicmodel/neg_after.csv')
df2 = pd.read_csv (r'/Path/to_topicmodel/pos_after.csv')
df3 = pd.read_csv (r'/Path/to_topicmodel/neg_before.csv')
df4 = pd.read_csv (r'/Path/to_topicmodel/pos_before.csv')

stopwords = set(STOPWORDS)
stopwords.update(["flew", "sometimes", "happened", "share", "concern", "american", 'Colorado', "ex", 'cruise', 'booked',
                  '17th', 'try', 'd', 'none', 'vail', 'things', 'ill', 'departed', 'short', 'airli', 'nov', 'make', 'may',
                  'suppose', ' apart', 'december', 'airlines', 'monday', 'yet', 'please', 'detroit', 'pe', 'august', 'augus',
                  'explain', 'cont', 'truly', 'review', 'milwaukee', 'us', 'aa', 'told', 'said', 'get', 'never', 'american', 'delta', 'southwest', 'south', 'west', 'would', 
                   'next', 'even', 'one', 'back', 'first', 'like', 'could', 'great', 'good', 'bad', 'worst', 'ever', 'years', 'days', ' don t',
                   'airlines', 'airline', 'flight', 'fly', 'flights', 'flying', 'way', 'also', 'got', 'made', 'airport', 'option',
                   'go', 'people', 'call', 'home', 'day', 'asked', 'son', 'two', 'three', 'four', 'five', 'make', 'slc', 'called', 'missed',
                   'many', 'nice', 'love', 'another', 'area', 'always', 'well', 'easy', 'best', 'went', 'much', 'use', 'almost', 'night',
                   'going', 'really', 'know', 'since', 'knowing', 'knows', 'knew', 'little', 'give', 'again', "don't", 'wa',
                   'name', 'length', 'w', 'everyone', 'dtype', 'joke', 'object', 'will', 'ticket', 'pay', 'put', 'needed',
                   'leave', 'luggage', 'see', 'finally', 'now', 'change', 'still', 'money', 'help', 's', 'new', 'month', 'counter',
                   'minute', 'bag', 'hotel', 'issue', 'took', 'let', 'due', 'left', 'tell', 'class', 'nothing', 'voucher', 'least',
                   'take', 'phone', 'arrived', 'book', 'agent', 'boarding', 'family', 'trying', 'need', 'say', 'sit', 'recieve',
                   'dallas', 'without', 'wait', 'bags', 'want', 'better', 'waiting', 'hold', 'gave', 'weather', 'paid', 'sitting',
                   'extra', 'last', "don't", 'dont', 'late', 'cost', 'right', 'changed', 'connection', 'someone', 'recieved',
                   'around', 'cancelled', 'hour', 'find', 'hours', 'able', 'tried', 'every', 'miss', 'available', 'reason', 'long',
                   'number', 'm', 'later', 'point', 'problem', 'days', 'week', 'year', 'canceled', 'return', 'instead'])



#neg after
text = df1['Review'].tolist() 

# join the list and lowercase all the words
text = ' '.join(text).lower()

#create the wordcloud object
wordcloud = WordCloud(stopwords = stopwords,
                      collocations=True).generate(text)

#plot the wordcloud object
plt.imshow(wordcloud, interpolation='bilInear')
plt.axis('off')
plt.show()

#pos after
text = df2['Review'].tolist() 

# join the list and lowercase all the words
text = ' '.join(text).lower()

#create the wordcloud object
wordcloud = WordCloud(stopwords = stopwords,
                      collocations=True).generate(text)

#plot the wordcloud object
plt.imshow(wordcloud, interpolation='bilInear')
plt.axis('off')
plt.show()

#neg before
text = df3['Review'].tolist() 

# join the list and lowercase all the words
text = ' '.join(text).lower()

#create the wordcloud object
wordcloud = WordCloud(stopwords = stopwords,
                      collocations=True).generate(text)

#plot the wordcloud object
plt.imshow(wordcloud, interpolation='bilInear')
plt.axis('off')
plt.show()

#pos before
text = df4['Review'].tolist() 

# join the list and lowercase all the words
text = ' '.join(text).lower()

#create the wordcloud object
wordcloud = WordCloud(stopwords = stopwords,
                      collocations=True).generate(text)

#plot the wordcloud object
plt.imshow(wordcloud, interpolation='bilInear')
plt.axis('off')
plt.show()