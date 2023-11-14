# Import the necessary libraries
import scrapy

# Define the Spider class
class EducationSpider(scrapy.Spider):

    # Define the name of the spider
    name = "education"

    # Define the start URL
    start_urls = ["https://www.tc.edu.tw/page/78f8e2b3-e309-4bb1-b8e1-4fd7a9d0af83"]

    # Define the parse() method
    def parse(self, response):
        # Find the title
        title = response.css("h1::text").get()

        # Find the text
        text = response.css("div.content::text").get()

        # Yield the data
       