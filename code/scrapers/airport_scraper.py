#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:54:43 2022

@author: averyfield2
"""

import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time

path_to_file = "/Path/airport_data.csv"

urls = ["https://www.airlinequality.com/airport-reviews/atlanta-hartsfield-airport/?sortby=post_date%3ADesc&pagesize=100",
        'https://www.airlinequality.com/airport-reviews/chicago-ohare-airport/?sortby=post_date%3ADesc&pagesize=100]',
        'https://www.airlinequality.com/airport-reviews/los-angeles-lax-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/dallas-fort-worth-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/denver-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/new-york-jfk-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/san-francisco-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/las-vegas-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/seattle-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/charlotte-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/phoenix-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/orlando-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/miami-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/houston-george-bush-intercontinental-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/fort-lauderdale-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/newark-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/akron-canton-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/albuquerque-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/baltimore-washington-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/boston-logan-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/tampa-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/st-louis-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/sacramento-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/salt-lake-city-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/san-diego-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/raleigh-durham-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/philadelphia-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/phoenix-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/nashville-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/new-orleans-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/milwaukee-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/minneapolis-st-paul-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/myrtle-beach-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/la-guardia-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/kansas-city-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/detroit-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/fort-myers-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/honolulu-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/indianapolis-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/san-juan-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/toronto-pearson-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/vancouver-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/montreal-trudeau-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/edmonton-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/london-gatwick-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/london-heathrow-airport/?sortby=post_date%3ADesc&pagesize=100',
        'https://www.airlinequality.com/airport-reviews/manchester-airport/?sortby=post_date%3ADesc&pagesize=100']
        
# open the file to save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)

for url in urls:
    # import the webdriver
    driver = webdriver.Safari()
    driver.get(url)

    # give the DOM time to load
    time.sleep(2)
    
    container = driver.find_elements_by_xpath(".//article[contains(@class, 'comp comp_media-review-rated list-item media position-content review-')]")

    for j in range(len(container)):
        #get rating
        try:
            rating = container[j].find_element_by_xpath(".//span[contains(@itemprop, 'ratingValue')]").text
        except NoSuchElementException:
            rating = "n/a"
        print(rating)
        #get title
        title = container[j].find_element_by_xpath(".//h2[contains(@class, 'text_header')]").text
        print(title)
        #get date
        date = container[j].find_element_by_xpath(".//time[contains(@itemprop, 'datePublished')]").text
        print(date)
        #get review
        review = container[j].find_element_by_xpath(".//div[@itemprop='reviewBody']").text.replace("\n", "  ")
        print(review)
        
        csvWriter.writerow([date, rating, title, review]) 
        


    
    driver.quit()


    
    
    
    