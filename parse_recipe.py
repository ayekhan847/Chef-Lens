#This file holds the recipe parsing function
import requests
from recipe_scrapers import scrape_html

def parse_recipe(url):
    """
    Parses recipe data from a given URL using the recipe-scrapers library.

    Parameters:
    - url (str): The URL of the recipe page to parse.

    Returns:
    - dict: A dictionary containing the recipe title, ingredients, instructions, and image URL.
    """
    # Fetch HTML content from the URL
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html_content = response.content

    # Initialize the scraper with HTML content and original URL
    scraper = scrape_html(html_content, org_url=url)

    # Extract data
    title = scraper.title()
    ingredients = scraper.ingredients()
    instructions = scraper.instructions()
    image_url = scraper.image()

    # Structure data into a dictionary
    recipe_data = {
        "title": title,
        "ingredients": ingredients,
        "instructions": instructions,
        "image_url": image_url
    }

    return recipe_data