#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:24:54 2022

@author: averyfield2
"""

import pandas as pd
from cleantext import clean

#airline data
#combine reviews for 3 airlines into one df
df1 = pd.read_csv (r'/Path/american_review_data.csv')
df2 = pd.read_csv (r'/Path/delta_review_data.csv')
df3 = pd.read_csv (r'/Path/sw_data.csv')

frames = [df1, df2, df3]
airline_reviews = pd.concat(frames)
                   
#sort by date 
airline_reviews["Date"] = airline_reviews["Date"].str.replace("Date of travel: ","")
airline_reviews["Date"] = pd.to_datetime(airline_reviews["Date"], errors='coerce')
airline_reviews = airline_reviews.dropna(subset=['Date'])
airline_reviews = airline_reviews.sort_values(by='Date')

#separate before and after pandemic
airline_reviews = airline_reviews.set_index(airline_reviews['Date'])
al_before_pandemic = airline_reviews['2017-06-01':'2020-03-15']
al_after_pandemic  = airline_reviews['2020-03-15':]    

#make csv files
al_before_pandemic.to_csv('/Path/al_before_pandemic.csv')
al_after_pandemic.to_csv('/Path/al_after_pandemic.csv')

print('done')

#airport data
airport_reviews = pd.read_csv (r'/Path/airport_data.csv')

airport_reviews = airport_reviews.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
airport_reviews["Review"] = airport_reviews["Review"].str.replace("Trip Verified","")
airport_reviews["Review"] = airport_reviews["Review"].str.replace("Not Verified","")

airport_reviews["Date"] = pd.to_datetime(airport_reviews["Date"], errors='coerce')
airport_reviews = airport_reviews.dropna(subset=['Date'])
airport_reviews = airport_reviews.sort_values(by='Date')

airport_reviews = airport_reviews.set_index(airport_reviews['Date'])
ap_before_pandemic = airport_reviews['2017-06-01':'2020-03-15']
ap_after_pandemic  = airport_reviews['2020-03-15':] 

ap_before_pandemic.to_csv('/Path/ap_before_pandemic.csv')
ap_after_pandemic.to_csv('/Path/ap_after_pandemic.csv')

print('done')







            

            

