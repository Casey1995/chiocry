import requests, shutil, validators

span = []
def intAsignment():
    try:
        url = input("Enter your url: ")
        
        #Validating the user entered url.
        validators.url(url)
        while not validators.url(url):
            print('Please enter a valid url')
            url = input("Enter your url: ")
            
        #Fetching/reading the contents of the url.
        request = requests.get(url)
        served = request.text
        #creating a file rock.txt, and writing the scrapped content from the web(url) to it.
        with open ("rock.txt", "w") as output:
            output.writelines(served)

        #Reading/parsing the file to get ingredients
        with open ("rock.txt", "r") as recipe:
            for lines in recipe.readlines():
                if 'span class="description"' in lines:
                    span.append(lines)

        for items in span:
            ingredient = items.replace('<span class="description">', '')
            ingredients = ingredient.replace('</span>', '.')
            return ingredients
    except ValueError:
        print('A very specific bad thing happened!')

intAsignment()
