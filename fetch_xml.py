#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:24:03 2019

@author: shayez
"""
import sqlite3 
import lxml.etree as ET 
import glob
import requests
import gzip

#root path of pubmed xml file 
root_path = '/home/shayez/Desktop/Mtech_Desktop/web/Shv/smsk/ftpfile'

#path of database 
d_path = '/home/shayez/Desktop/Mtech_Desktop/web/Shv'
all_xml = glob.glob(f'{root_path}/**/*.xml.gz', recursive=True)

conn = sqlite3.connect('/home/shayez/Desktop/Mtech_Desktop/web/Shv/NewNCBI2.db')
co = conn.cursor()
co.execute('''CREATE TABLE IF NOT EXISTS pubdata (PMID text , Date text, Abstract text);''')
print ("Opened database successfully")

#sort xml file
all_xml.sort()

#fetch pmid, abstract, date,  from xml file and store into database 
for all_xml in all_xml :
    f=gzip.open(all_xml,'r')
    print(all_xml)
    dom = ET.parse(f)
    pmdat = dom.findall('PubmedArticle')
    for c in pmdat:
        PMID = c.find('MedlineCitation/PMID').text
        Date = c.find('MedlineCitation/Article/Journal/JournalIssue/PubDate/Year')
        Date2 = c.find('MedlineCitation/Article/Journal/JournalIssue/PubDate/MedlineDate')
        Abstract = c.find('MedlineCitation/Article/Abstract/AbstractText')
        if Abstract is None :
            pass
        elif Date is None:
            example =[(PMID,Date2.text,Abstract.text)]
            co.executemany('INSERT INTO pubdata(PMID,Date,Abstract)  VALUES (?,?,?)',example)
        else:
            example =[(PMID,Date.text,Abstract.text)]
            co.executemany('INSERT INTO pubdata(PMID,Date,Abstract)  VALUES (?,?,?)',example) 

#use this code for deleting duplicate entry

#co.execute("DELETE from pubdata where rowid NOT IN (select min(rowid) from pubdata group by  PMID);") 

conn.commit()
print("Records Saved Successfully")
conn.close()


