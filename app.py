# App.py
# Flask app to handle requests from HTML page
# Jacob Collins
# December 2022

from flask import Flask, request, render_template

from urls import objects
from manga_updates import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Manga Update')

@app.route('/data', methods=["GET"])
def get_data():
    # Read the JSON file and update the objects with the values from the file
    try:
        with open("data.json") as f:
            return json.load(f)
    except FileNotFoundError:
        # If the file does not exist, use the default values from the objects
            print("Failed to retrieve data")
            return NULL

@app.route('/update', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Handle the POST request
        return update_manga(objects)

    elif request.method == 'GET':
        # Handle the GET request
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
