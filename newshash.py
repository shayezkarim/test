#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 05:49:02 2020

@author: shayez
"""

import tweepy
import csv
import pandas as pd



#path of database 








####input your credentials here
consumer_key = 'o8ZIaSRCI23qSrpnhZP6yUDje'
consumer_secret = 'r4gBWfn0W2GVWWEHhvN9jntE9MiujiCuIjORFiRK6NiD5cdyMz'
access_token = '335305300-QT61ohBCSrop73nbtLoxyHrqdCp53L3cTbXz0htE'
access_token_secret = 'Swger0CsAAWDrBCIL63Keram6D4nePfy2hgoKTCKLGHj4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile )



query  =['drug resistance' ,'drug-resistance','drug-resistant','drug resistant','antimicrobial resistance','antimicrobial-resistance','antimicrobial resistant' ,'antimicrobial-resistant','pan resistance' ,'pan-resistance','pan resistant','pan-resistant','multiple resistance' ,'multiple-resistance' ,'multiple resistant' ,'multiple-resistant' ,'multiple drug resistance' ,'multiple drug resistant','antibiotic resistant' ,'antibiotic-resistance' ,'antibiotic-resistant' ,'antibiotic resistance','mdr' ,'amr' ,'multi-drug resistant','multi-drug resistance','multi drug resistance','multi resistant','multi drug resistant','predicted resistance pattern','pan drug-resistance','pan drug resistance','pan drug resistant','pan drug-resistant','resistant bacteria','resistance bacteria']



for query  in query:
    tweets = tweepy.Cursor(api.search,q= query + "-filter:retweets" ,
                           lang="en",
                           since="2020-07-12").items()
    for tweet in tweets:
        #print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.user.screen_name,tweet.text.encode('utf-8')])
       



print("Records Saved Successfully")

