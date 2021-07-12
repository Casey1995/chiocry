from bs4 import BeautifulSoup
import requests, json

def recipe():
  try:
    url = input("Enter your url: ")
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    data = json.loads(soup.find('script', type='application/ld+json').text)
    for key, value in enumerate(data["recipeIngredient"]):
      ingredients = value
      return ingredients
  except ValueError:
    print("A very specific bad thing happened!")
recipe()

#url = "https://www.bettycrocker.com/recipes/lemon-raspberry-bars/5aaa9c08-53f9-404f-89e0-47ef9e49e605"
