# %%
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

# %%
# %%
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

# %%
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# %%
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

# %%
news_title = slide_elem.find("div", class_='content_title').get_text()
# %%
print(news_title)

# %%
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

# %% 'Markdown'
"### Featured Images"


# %%
# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# %%
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')

# %%
# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# %%
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()

# %%
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

# %%
# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# %%
# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url

# %%
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

# %%
browser.quit() 

# %%
