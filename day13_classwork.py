import requests
import json
import time


def main():
    url = "https://api.punkapi.com/v2/beers"
    response = requests.get(url)
    print("Status", response.status_code)

    while True:
        search = input("\nWhat kind of a beer are you looking for?\nInput a keyword or 'Q' to exit: ")
        # an empty line will print all - that's not a bug it's a feature

        if search.lower() == 'q':
            break

        picked_answers = {}

        for beer_data in response.json():
            if search.lower() in beer_data.get('description').lower():
                name = beer_data.get("name")
                tagline = beer_data.get("tagline")
                description = beer_data.get("description")
                abv = "ABV", beer_data.get("abv")
                ibu = "IBU", beer_data.get("ibu")
                attenuation_level = "Attenuation", beer_data.get("attenuation_level")
                image_url = beer_data.get("image_url")
                picked_answers[name] = tagline, description, abv, ibu, attenuation_level, image_url

        if picked_answers == {}:
            print("No items found!")
        else:
            print(f"Number of beers matching criteria: {len(picked_answers)} (details exported to file).")
            with open(f"beer_search_{search}.json", mode="w") as write_file:
                json.dump(picked_answers, write_file, indent=4)

        time.sleep(0.3)


if __name__ == "__main__":
    main()
