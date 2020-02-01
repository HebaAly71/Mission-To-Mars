# %%
from splinter import Browser
from bs4 import BeautifulSoup


# %%
# Path to chromedriver


# %%
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

# %%
# Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com/'
browser.visit(url)

# %%
# Parse the HTML
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# %%
# Scrape the Title
title = soup.find('h2').text
title

# %%
# Scrape the top ten tags
tag_box = soup.find('div', class_='tags-box')
# tag_box
tags = tag_box.find_all('a', class_='tag')

for tag in tags:
    word = tag.text
    print(word)

# %%
for x in range(1, 6):
   html = browser.html
   soup = BeautifulSoup (html, 'html.parser')
   quotes = soup.find_all('div', class_='quote')
   for quote in quotes:
      print('page:', x, '----------')
      print(quote.text)
   browser.click_link_by_partial_text('Next')

# %%
