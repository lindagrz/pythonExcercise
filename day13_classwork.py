import requests
import json
import time
from operator import itemgetter


def main():
    url = "https://api.punkapi.com/v2/beers"
    response = requests.get(url)

    while True:
        time.sleep(0.3)
        picked_answers = []

        # this will search all descriptions
        search = input("\nWhat kind of a beer are you looking for? (input a keyword or 'Q' to exit)\n")

        if search.lower() == 'q':
            break
        for beer_data in response.json():
            if search in beer_data['description'].lower():
                print(beer_data['name'], "-", beer_data['description'])
                picked_answers.append(itemgetter('name', 'description')(beer_data))
        with open("beer_data.json", mode="a") as write_file:
            json.dump(picked_answers, write_file, indent=4)


if __name__ == "__main__":
    main()
