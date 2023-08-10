from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/artwork")
def artwork(keyword="Monet", skip=0, limit=5):
    url = "https://openaccess-api.clevelandart.org/api/artworks"
    params = {
        'q': keyword,
        'skip': skip,
        'limit': limit,
        'has_image': 5
    }

    r = requests.get(url, params=params)

    data = r.json()

    tombstone = []

    for artwork in data['data']:
        tombstone.append(artwork['tombstone'])

    # print(f"{tombstone}\n{image}\n---")
    # print_openaccess_results("monet", 0, 10)
    return {"artworks": tombstone}

@app.route("/exhibition")
def get_artwork():
    # exhibition number: 180667
    exhibition_id = 180667
    exhibition = requests.get(f"https://openaccess-api.clevelandart.org/api/exhibitions/{exhibition_id}")
    # Get exhibition
    # For each artwork in an exhibition search for the artist's name
    data = exhibition.json() 
    christian_artworks = []

    for artwork in data['data']['artworks']:        
        artwork_id = artwork['id']
        single_artwork = requests.get(f"https://openaccess-api.clevelandart.org/api/artworks/{artwork_id}").json()
        for culture in single_artwork['data']['culture']:
            if "Christian" in culture:
                print(single_artwork['data']['id'])
                christian_artworks.append(single_artwork['data']['tombstone'])
    print(christian_artworks)
    return {"exhibition": christian_artworks}


if __name__ == "__main__":
    app.run(debug=True)