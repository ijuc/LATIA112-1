# Import the necessary libraries
import requests
from bs4 import BeautifulSoup
import chardet
import csv
# Define the URL to be scraped
url = "https://www.tc.edu.tw/page/78f8e2b3-e309-4bb1-b8e1-4fd7a9d0af83"

# Get the HTML content of the page
response = requests.get(url)

# Detect the encoding of the response
encoding = chardet.detect(response.content)["encoding"]

# Decode the HTML content to the detected encoding
response_content = response.content.decode(encoding)

# Parse the HTML content
soup = BeautifulSoup(response_content, "html.parser")

# Find the title
title = soup.find("h1").text

# Find the text
text = soup.find("div", class_="content").text

# Save the data to a CSV file
with open("education_data.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "text"])
    writer.writerow([title, text])