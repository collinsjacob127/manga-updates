from bs4 import BeautifulSoup
import os

with open('manhuaplus.html', 'r') as f:
    html = f.read()

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# Define the CSS selector variables
title_selector = "ul > li.wp-manga-chapter > span.chapter-release-date"

# Use the select_one method to find the first element matching the title selector
button = soup.select(title_selector)


print(f"Button: {button}")

for title in button:
    print(f"Sub-Button: {title}")
