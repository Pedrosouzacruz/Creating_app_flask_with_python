from flask import Flask
from flask_ngrok import run_with_ngrok
from flask import request 
from flask import jsonify
from flask import render_template
app = Flask(__name__)

d = [{"Id":1,
      "Name":"Mahesh",
      "Age":25,
      "City":"Bangalore",
      "Country":"India"},

      {"Id":2,
      "Name":"Alex",
      "Age":26,
      "City":"London",
      "Country":"United Kingdom"},   
      {"Id":3,
      "Name":"David",
      "Age":27,
      "City":"San Francisco",
      "Country":"United States of America"},
     {"Id":4,
      "Name":"John",
      "Age":28,
      "City":"Toronto",
      "Country":"Canada"},     
      {"Id":5,
      "Name":"Chris",
      "Age":29,
      "City":"Paris",
      "Country":"France"}]

"""@app.route("/") #code to assign HomePage URL in our app to function home.
def homepage():
    return render_template("homepage.html")"""

@app.route("/") #code to assign HomePage URL in our app to function home.

def home():

  return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE URL AND TO CHECK OUT PUT ADD '/output' TO THE URL.</h3></marquee>"

@app.route("/index")
def index():
    return render_template("json.html")

if __name__ == "__main__":
    run_with_ngrok(app)

app.run()
