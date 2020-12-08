# Dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
from splinter import Browser
import warnings
warnings.filterwarnings('ignore')

def init_browswer():

# ## Step 1 - Scraping

# Set up splinter
    executable_path = {'executable_path': "chromedriver.exe"}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browswer()

    url_news = 'https://mars.nasa.gov/news/'
    browser.visit(url_news)

    # Create BeautifulSoup object & parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # collect the latest News Title and Paragraph Text
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # URL of page to be scraped
    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)

    # Create BeautifulSoup object & parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Set up featured_image_url
    url_main = 'https://www.jpl.nasa.gov/'
    featured_image_url = soup.find('a', class_='fancybox')['data-fancybox-href']
    featured_image_url_final = url_main + featured_image_url

    # URL of page to be scraped
    url_image = 'https://space-facts.com/mars/'
    browser.visit(url_image)

    # Use Pandas to parse url
    table_facts = pd.read_html(url_image)
    table_facts

    # Create a DataFrame 
    facts_df = table_facts[0]
    facts_df.columns=['Facts', 'Description']
    facts_df

    # Use Pandas to convert the data to a HTML table string.
    facts_df_html = facts_df.to_html(table_id="html_tbl_css", justify='left', index=False)

    # URL of page to be scraped
    url_hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemispheres)

    # Create BeautifulSoup object & parse with 'html.parser'
    hemispheres_html = browser.html
    soup = BeautifulSoup(hemispheres_html, 'html.parser')

    # Locate information for all four Hemisphere 
    hemispheres_results = soup.find_all('div', class_='item')

    # Create a list to hold Mars Hemispheres url
    hemispheres_image_urls = []
    url_hemispheres_main = 'https://astrogeology.usgs.gov'

    # Retrieve titles for hemispheres
    for hem_url in hemispheres_results:
        hemispheres_title = hem_url.find('h3').text
        hemispheres_title = hemispheres_title.replace(" Enhanced","")

    # Retrieve partial url for hemispheres image
    
        hemispheres_image = hem_url.find('a', class_='itemLink product-item')['href']
        browser.visit(url_hemispheres_main + hemispheres_image)
    
        hemispheres_image_html = browser.html
        hemispheres_soup = BeautifulSoup(hemispheres_image_html, 'html.parser')

    # Merge hemispheres main URL & hemispheres image partial URLs
    
        hemispheres_image_url = url_hemispheres_main + hemispheres_soup.find('img', class_='wide-image')['src']
    
    # Append merged URLs into list
        hemispheres_image_urls.append({"title": hemispheres_title, "img_url": hemispheres_image_url})

# Create a dictionary for holding Mission to Mars data to be imported into Mongo
    mars_data = {
    "Mars_News_Title": news_title,
    "Mars_News_Paragraph": news_p,
    "Mars_Featured_Image": featured_image_url_final,
    "Mars_Facts": facts_df_html,
    "Mars_Hemispheres": hemispheres_image_urls}

    browser.quit()

    return mars_data




