#!/bin/bash

import requests
import re
import codecs
import time,random
#  from xgoogle.search import GoogleSearch, SearchError

#from google import google
import os
os.chdir("./Google-Search-API/")
from google import google

from bs4 import BeautifulSoup
from openpyxl import Workbook
#  wb = Workbook()
dest_filename="files.xlsx"

DOWNLOAD_URL= 'http://www.google.com'

#  ws1 = wb.active
#  ws1.title =

def download_page(url):
    headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36' }
    data = requests.get(url,headers=headers).content
    return data


def main():
    #  url="http://www.google.com"
    #  url=DOWNLOAD_URL
    #  doc = download_page(url)
    #  print doc
    f = open('a.txt','wb')
    results = google.search("abc filetype:doc",1000)
    time.sleep(2)
#    print results
    for res in results:
        print res.name.encode('utf8')
        print res.link.encode('utf8')
        print res.google_link.encode('utf8')
        print res.page
        print res.index
        print '\n'
    print 'done'
    f.close

if __name__ == '__main__':
    main()
