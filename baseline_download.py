#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:25:44 2019

@author: shayez
"""
#import library

import sh
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import wget
import os

#to create directory


try:
    sh.mkdir('-p','ftpfile/baseline')
except:
    pass
    
#to change directory
sh.cd('ftpfile/baseline')

#NCBI FTP link 

url="https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/"

#empty list to store pubmed file name from ftp web 
list2 = []

soup = bs(urlopen(url))
for link in soup.findAll('a'):
        list2.append(link.string)

#use this code if download iterrupted by deleting dowloaded list         

#del list2[0:1980]      

#loop for get only zip xml file else pass and Append pubmed file name to url to dowload ftp file 
for i in list2:
     if i.endswith(".gz"):
         sh.wget(url + i)
     else:
        pass

