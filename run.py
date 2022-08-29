import requests 
from bs4 import BeautifulSoup
import time
import sys

URL = 'https://eu.finalfantasyxiv.com/lodestone/worldstatus/'
    
while(True):
    website = requests.get(URL)
    results = BeautifulSoup(website.content, 'html.parser')
    server = results.find_all('li', class_= 'item-list')
    for server in server:
        if server.find('p', string='Omega'):
            if server.find('i', class_='world-ic__available js__tooltip'):
                print("Server Free")
                sys.exit(0)
            if server.find('i', class_='world-ic__unavailable js__tooltip'):
                print("Server Full")
            if server.find('i', class_='world-ic__3 js__tooltip'):
                print("Server Offline")
    time.sleep(5)
