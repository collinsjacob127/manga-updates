import requests
import json
import time
import random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import os

from urls import objects
from urls import tags

if __name__ == "__main__":
    # Read the JSON file and update the objects with the values from the file
    try:
        with open("data.json") as f:
            data = json.load(f)
            for obj in objects:
                for saved in data:
                    # Check if the URL is present in the JSON file
                    if obj["url"] == saved["url"]:
                        # Update the object with the values from the JSON file
                        obj.update(saved)
    except FileNotFoundError:
        # If the file does not exist, use the default values from the objects
        pass

    # Create a session to store cookies
    session = requests.Session()

    # Generate a random user agent
    ua = UserAgent()

    # Iterate through the objects
    for obj in objects:
        # Get the URL and domain from the object
        url = obj["url"]
        domain = url.split("/")[2]

        # Set the user agent and referrer in the request headers
        headers = {
            "User-Agent": ua.random,
            "Referer": url
        }

        # Use the session to send a GET request to the URL
        time.sleep(random.uniform(1, 3))
        response = session.get(url, headers=headers)

        # Check if the page has redirected
        if response.history:
            # Wait a random amount of time before getting the final destination page
            time.sleep(random.uniform(1, 3))
            response = session.get(response.url, headers=headers)
        
        # print(response.text)

        # Use the tags dictionary to get the tags for 'current chapter' and 'last updated'
        try:
            current_chapter_tag = tags[domain]["current_chapter"]
            last_updated_tag = tags[domain]["last_updated"]
        except KeyError:
            # Handle the case where the domain is not present in the tags dictionary
            print(f"No tags available for domain {domain}")
            continue

        # Parse the HTML content of the response using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        current_chapter = ""
        last_updated = ""

        # Extract the 'current chapter' and 'last updated' values from the page
        try:
            current_chapter = soup.select_one(current_chapter_tag).text
        except:
            print(f"Invalid selecter for chapter at {url}")
        try:
            last_updated = soup.select_one(last_updated_tag).text
        except:
            print(f"Invalid selecter for last_updated at {url}")

        # Compare the values with the ones in the object
        if current_chapter != obj["current_chapter"]:
            print(f"Current chapter for {obj['title']} has changed from {obj['current_chapter']} to {current_chapter}")
            obj["current_chapter"] = current_chapter
        if last_updated != obj["last_updated"]:
            print(f"Last updated for {obj['title']} has changed from {obj['last_updated']} to {last_updated}")
            obj["last_updated"] = last_updated

        print("-------------------------------------------------------")

    test_object = {
        "title": "Test",
        "current_chapter": "Test Chapter",
        "url": "test url",
        "last_updated": "Test date"
    }

    # objects.append(test_object)
    # Write the updated list of objects to a JSON file 
    with open("data.json", "w") as f:
        json.dump(objects, f)
