import json
import time
from requests import post, get
import base64

# TOKEN ACQUISITION ...

def get_token():

    client_id=""
    client_secret=""

    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print('No Artist With Name Found')
        return None
    else:
        return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

token = get_token()

result = search_for_artist(token, "Voidpiercer")

# print(result)

artist_id = result["id"]
artist_name = result["name"]
artist_followers = result["followers"]
artist_genres = result["genres"]

print(f'\n{artist_name} (ID) : {artist_id}'), time.sleep(.3)
print('Followers: ', artist_followers['total']), time.sleep(.3)
print('Genre(s): ',artist_genres[0]), time.sleep(.3)

print('\nTop Ten Songs\n')

songs = get_songs_by_artist(token, artist_id)

for index, song in enumerate(songs):
    print(f"{index + 1}. {song['name']}")
    time.sleep(.3)

# print(songs)
