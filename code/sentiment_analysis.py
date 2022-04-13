#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:53:46 2022

@author: averyfield2
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

sid = SentimentIntensityAnalyzer()

#airline reviews after pandemic
al_after = pd.read_csv (r'/Path/al_after_pandemic.csv')

al_after['scores'] = al_after['Review'].apply(lambda review: sid.polarity_scores(review))
al_after['compound']  = al_after['scores'].apply(lambda score_dict: score_dict['compound'])

avg_sent_al_after = al_after['compound'].mean()
print('Airline sentiment after pandemic:')
print(avg_sent_al_after)

#airline reviews before pandemic
al_before = pd.read_csv (r'/Path/al_before_pandemic.csv')

al_before['scores'] = al_before['Review'].apply(lambda review: sid.polarity_scores(review))
al_before['compound']  = al_before['scores'].apply(lambda score_dict: score_dict['compound'])

avg_sent_al_before = al_before['compound'].mean()
print('Airline sentiment before pandemic:')
print(avg_sent_al_before)

#airport reviews after pandemic
ap_after = pd.read_csv (r'/Path/ap_after_pandemic.csv')

ap_after['scores'] = ap_after['Review'].apply(lambda review: sid.polarity_scores(review))
ap_after['compound']  = ap_after['scores'].apply(lambda score_dict: score_dict['compound'])

avg_sent_ap_after = ap_after['compound'].mean()
print('Airport sentiment after pandemic:')
print(avg_sent_ap_after)

#airport reviews before pandemic
ap_before = pd.read_csv (r'/Path/ap_before_pandemic.csv')

ap_before['scores'] = ap_before['Review'].apply(lambda review: sid.polarity_scores(review))
ap_before['compound']  = ap_before['scores'].apply(lambda score_dict: score_dict['compound'])

avg_sent_ap_before = ap_before['compound'].mean()
print('Airport sentiment before pandemic:')
print(avg_sent_ap_before)

#move pos and neg reviews to their own df's for topic modeling
after_frames = [al_after, ap_after]
after_pandemic = pd.concat(after_frames)
after_pandemic = after_pandemic.sort_values(by='compound')
after_pandemic = after_pandemic.set_index(after_pandemic['compound'])

pos_after = after_pandemic[0.71:1.0]
neg_after = after_pandemic[-1.0:0.7]

before_frames = [al_before, ap_before]
before_pandemic = pd.concat(before_frames)
before_pandemic = before_pandemic.sort_values(by='compound')
before_pandemic = before_pandemic.set_index(before_pandemic['compound'])

pos_before = before_pandemic[0.71:1.0]
neg_before = before_pandemic[-1.0:.7]

pos_after.to_csv('/Path/to_topicmodel/pos_after.csv')
neg_after.to_csv('/Path/to_topicmodel/neg_after.csv')
pos_before.to_csv('/Path/to_topicmodel/pos_before.csv')
neg_before.to_csv('/Path/to_topicmodel/neg_before.csv')