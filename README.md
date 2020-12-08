# web-scraping-challenge

Step 1 - Scraping
* Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
* Create a Jupyter Notebook file called 'mission_to_mars_SZ.ipynb' and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

Process:
1. Import dependencies
2. Scraping Process:

NASA Mars News
* Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
Process:
1. Set up splinter & URL page to be scraped [here] (https://mars.nasa.gov/news/)
2. Create BeautifulSoup object & parse with 'html.parser'
3. Collect the lastest News Title & Paragraph Text

JPL Mars Space Images - Featured Image
Visit the url for JPL Featured Space Image [here] (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
Process: 
1. Set up splinter
2. Create BeautifulSoup object & parse with 'html.parser'
3. Set up Featured_Image_URL and retrieve URL for image

Mars Facts
* Visit the Mars Facts webpage [here] (https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* Use Pandas to convert the data to a HTML table string.
Process:
1. Set up splinter & URL page to be scraped
2. Use Pandas to parse URL
3. Create a DataFrame/table for Facts
4. Use Pandas to convert the data to a HTML table string

Mars Hemispheres
* Visit the USGS Astrogeology site [here] (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
Process: 
1. Set up splinter & URL page to be scraped
2. Create BeautifulSoup object & parse with 'html.parser'
3. Locate information for all four Hemispheres
4. Create a dictionary to hold Mars Hemispheres URL
    * Retrieve titles for Hemispheres
    * Retrieve partial URL for Hemispheres images
    * Merge Hemispheres main URL & Hemispheres image partial URLs
    * Append merged URLs into list

Step 2 - MongoDB and Flask Application
* Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
Process:
1. Converting Jupyter Notebook 'mission_to_mars_SZ.ipynb' to a Python script called 'scrape_mars.py'
    * Set up 'def init_browswer():'
    * Set up 'def scrape():
    * Create a dictionary for holding 'Mission to Mars' data to be imported into Mongo called 'mars_data'
2. create a route called /scrape that will import your scrape_mars.py script and call your scrape function called 'app.py' file
    * Import Pymongo libarary
    * Create an instance of Flash app
    * Set up @app.route("/")
    * Set up a route @app.route("/scrape") which will call scrape function
    * Run the scrape functions 
    * Update the Mongo database using update
    * Redirect back to home page
3. Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
    * Set up Bootstrap CSS
    * Set up template for header
    * Latest Mars News
    * Featured Mars Mage
    * Mars Facts Table
    * Mars Hemispheres Images
