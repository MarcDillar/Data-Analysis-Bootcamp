import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = 'https://basketball.realgm.com/ncaa/boxscore/2021-01-29/North-Texas-at-Rice/367436'
page = requests.get(url)
soup = BeautifulSoup(page.content , 'html.parser')

#Extracting Columns
tables = soup.find('div', class_= 'boxscore-gamesummary')
columns = tables.find_all('th', class_='nosort')

#Extracting Stats
tables = soup.find('div', class_= 'boxscore-gamesummary')
stats = tables.find_all('td')

#Filling DataFrame
temp_df = pd.DataFrame(stats).transpose()
temp_df.columns = columns

final_df = pd.concat([final_df,temp_df], ignore_index=True)

final_df