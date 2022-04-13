#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:50:48 2022

@author: averyfield2
"""

import csv
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time

path_to_file = "/Path/american_review_data.csv"

pages_to_scrape = 1000

url = "https://www.tripadvisor.com/Airline_Review-d8729020-Reviews-American-Airlines"


driver = webdriver.Safari()
driver.get(url)


csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)


for i in range(0, pages_to_scrape):

    # give the DOM time to load
    time.sleep(2) 

    # Click the "expand review" link to reveal the entire review.
    driver.find_element_by_xpath(".//div[contains(@data-test-target, 'expand-review')]").click()
    container = driver.find_elements_by_xpath("//div[@data-reviewid]")

   
    for j in range(len(container)): # A loop defined by the number of reviews

        # Grab the rating
        rating = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
        # Grab the title
        title = container[j].find_element_by_xpath(".//div[contains(@data-test-target, 'review-title')]").text
        #Grab the review
        review = container[j].find_element_by_xpath(".//q[@class='XllAv H4 _a']").text.replace("\n", "  ")
        #Grab the date
        try:
            date = container[j].find_element_by_xpath(".//span[contains(@class, 'euPKI _R Me S4 H3')]").text
        except NoSuchElementException:
            date = "n/a"
        print(date)
        print(rating)
        print(title)
        print(review)
        print('')
        
        csvWriter.writerow([date, rating, title, review]) 
                    
    driver.find_element_by_xpath('.//a[@class="ui_button nav next primary "]').click()

driver.quit()

path_to_file = "/Path/delta_review_data.csv"

pages_to_scrape = 1000

url = "https://www.tripadvisor.com/Airline_Review-d8729060-Reviews-Delta-Air-Lines"

# import the webdriver
driver = webdriver.Safari()
driver.get(url)

# open the file to save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)


for i in range(0, pages_to_scrape):

    # give the DOM time to load
    time.sleep(2) 

    driver.find_element_by_xpath(".//div[contains(@data-test-target, 'expand-review')]").click()

    container = driver.find_elements_by_xpath("//div[@data-reviewid]")
   
    for j in range(len(container)): # A loop defined by the number of reviews

        # Get rating
        rating = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
        # Get title
        title = container[j].find_element_by_xpath(".//div[contains(@data-test-target, 'review-title')]").text
        #Get review
        review = container[j].find_element_by_xpath(".//q[@class='XllAv H4 _a']").text.replace("\n", "  ")
        #Get date
        try:
            date = container[j].find_element_by_xpath(".//span[contains(@class, 'euPKI _R Me S4 H3')]").text
        except NoSuchElementException:
            date = "n/a"
        print(date)
        print(rating)
        print(title)
        print(review)
        print('')
        
        csvWriter.writerow([date, rating, title, review]) 
           
    driver.find_element_by_xpath('.//a[@class="ui_button nav next primary "]').click()

driver.quit()

path_to_file = "/Path/sw_data.csv"

pages_to_scrape = 1000

url = "https://www.tripadvisor.com/Airline_Review-d8729156-Reviews-Southwest-Airlines"

# import the webdriver
driver = webdriver.Safari()
driver.get(url)

# open the file to save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)

# change the value inside the range to save the number of reviews we're going to grab
for i in range(0, pages_to_scrape):

    # give the DOM time to load
    time.sleep(2) 

    # Click the "expand review" link to reveal the entire review.
    try:
        driver.find_element_by_xpath(".//div[contains(@data-test-target, 'expand-review')]").click()
    except NoSuchElementException or ElementNotInteractableException:
        pass
    # Now we'll ask Selenium to look for elements in the page and save them to a variable. First lets define a  container that will hold all the reviews on the page. In a moment we'll parse these and save them:
    container = driver.find_elements_by_xpath("//div[@data-reviewid]")

    # Next we'll grab the date of the review:
    #dates = driver.find_elements_by_xpath(".//div[@class='_2fxQ4TOx']")
    
    print(len(container))
    #print(dates)
    
   # Now we'll look at the reviews in the container and parse them out
   
    for j in range(len(container)): # A loop defined by the number of reviews

        # Grab the rating
        rating = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
        # Grab the title
        title = container[j].find_element_by_xpath(".//div[contains(@data-test-target, 'review-title')]").text
        #Grab the review
        review = container[j].find_element_by_xpath(".//q[@class='XllAv H4 _a']").text.replace("\n", "  ")
        #Grab the date
        
        try:
            date = container[j].find_element_by_xpath(".//span[contains(@class, 'euPKI _R Me S4 H3')]").text
        except NoSuchElementException:
            date = "n/a"
        print(date)
        print(rating)
        print(title)
        print(review)
        print('')
        
        #Save that data in the csv and then continue to process the next review
        csvWriter.writerow([date, rating, title, review]) 
        
    # When all the reviews in the container have been processed, change the page and repeat            
    driver.find_element_by_xpath('.//a[@class="ui_button nav next primary "]').click()


driver.quit()


