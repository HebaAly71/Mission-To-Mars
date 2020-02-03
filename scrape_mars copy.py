# %%
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import requests

# %%
def mars_news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        # Use the parent element to find the first <a> tag and save it as `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None
    return news_title, news_p
# %%
# Image URL Function
def featured_image(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    try:
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    except AttributeError:
        return None
    
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    
    return img_url

# %%
def mars_facts():
    try:
      # use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]
    except BaseException:
        return None
    # Assign columns and set index of dataframe
    df.columns=['description', 'value']
    df.set_index('description', inplace=True)
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

# %%
# Challenge
#def hemispheres(browser):

# %%
browser = Browser('chrome', executable_path='/usr/local/bin/chromedriver', headless=False)
# %%
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
# %%
# parsing
html = browser.html
#news_soup = BeautifulSoup(html, 'html.parser')
# %%
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
# %%
x = range(3)
title_dict=[]
for heading in soup.find_all(["h3"]):
    heading1 = heading.text.strip()
    title_dict.append(heading1)

# %%
def hemispheres(browser):
    # A way to break up long strings
    url = (
        "https://astrogeology.usgs.gov/search/"
        "results?q=hemisphere+enhanced&k1=target&v1=Mars"
    )
    browser.visit(url)
    # Click the link, find the sample anchor, return the href
    hemisphere_image_urls = []
    for i in range(4):
        # Find the elements on each loop to avoid a stale element exception
        browser.find_by_css("a.product-item h3")[i].click()
        hemi_data = scrape_hemisphere(browser.html)
        # Append hemisphere object to list
        hemisphere_image_urls.append(hemi_data)
        # Finally, we navigate backwards
        browser.back()
    return hemisphere_image_urls
# %%
def scrape_hemisphere(html_text):
    #url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    #browser.visit(url)
    # parse html text
    #reqs = requests.get(url)
    #soup = BeautifulSoup(reqs.text, 'lxml')
    hemi_soup = BeautifulSoup(html_text, "html.parser")
    # adding try/except for error handling
    try:
        title_elem = hemi_soup.find("h2", class_="title").get_text()
        sample_elem = hemi_soup.find("a", text="Sample").get("href")
    except AttributeError:
        # Image error will return None, for better front-end handling
        title_elem = None
        sample_elem = None
    hemispheres = {
        "title": title_elem,
        "img_url": sample_elem
    }
    return hemispheres
# %%
slide_elem = news_soup.select_one('div.result-list')
print(slide_elem)
# %%
hem_title = slide_elem.find("div", class_='description')
# %%
hem_title_1 = hem_title.find('a', )
print(hem_title_1)
# %%
def scrape_all():
   # Initiate headless driver for deployment
    #executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', executable_path='/usr/local/bin/chromedriver', headless=True)
    news_title, news_paragraph = mars_news(browser)
    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now()
    }
    #if __name__ == "__main__":
    return data
    #if __name__ == "__main__":
    # If running as script, print scraped data
    #print(scrape_all())
    

# %%
#browser.quit() 

# %%
# A way to break up long strings
browser = Browser('chrome', executable_path='/usr/local/bin/chromedriver', headless=False)
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
    # Click the link, find the sample anchor, return the href
hemisphere_image_urls = []
for i in range(4):
    # Find the elements on each loop to avoid a stale element exception
    browser.find_by_css("a.product-item h3")[i].click()
    hemi_data = scrape_hemisphere(browser.html)
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemi_data)
    # Finally, we navigate backwards
    browser.back()
    hemisphere_image_urls2 = pd.DataFrame(hemisphere_image_urls)
print(hemisphere_image_urls2)
    # return hemisphere_image_urls

# %%
print(hemi_data)
# %%
listofTuples = [("Riti" , 11), ("Aadi" , 12), ("Sam" , 13),("John" , 22),("Lucy" , 90)]
studentsDict = dict(listofTuples)

# %%
