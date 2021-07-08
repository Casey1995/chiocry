import requests, shutil, validators

span = []
def intAsignment():
    try:
        url = input("Enter your url: ")
        validators.url(url)
        while not validators.url(url):
            print('Please enter a valid url')
            url = input("Enter your url: ")
        request = requests.get(url)
        served = request.text
        with open ("rock.txt", "w") as output:
            output.writelines(served)
        with open ("rock.txt", "r") as recipe:
            for lines in recipe.readlines():
                if 'span class="description"' in lines:
                    span.append(lines)

        for items in span:
            ingredient = items.replace('<span class="description">', '')
            ingredients = ingredient.replace('</span>', '.')
            print(ingredients)
    except ValueError:
        print('A very specific bad thing happened!')

intAsignment()
