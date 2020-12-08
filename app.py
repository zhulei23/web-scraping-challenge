from flask import Flask, render_template, redirect

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of our Flask app.
app = Flask(__name__)

# Use PyMongo to set up Mongo connection
#mongo = PyMongo(app, url="mongodb://localhost:27017/mars_data")
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set up @app.route("/")
@app.route("/")
def home():

    # Locate data from dictionary & return data
    mars_data = mongo.db.mars_data.find_one()
    return render_template("index.html", mars_data=mars_data)

# Set up a route which will call scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data_update = scrape_mars.scrape()

    # Update the Mongo database using update & upsert=Truepytho
    mongo.db.mars_data.update({}, mars_data_update, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
    



