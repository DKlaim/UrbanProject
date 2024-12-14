import requests
import pprint
from threading import Thread

ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

genre = requests.get(RANDOM_GENRE_API_URL).json()

data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})

# иногда может не находить
# pprint.pprint(data.json())  # https://genius.com/songs/494663/apple_music_player

data = data.json()
song_id = data['response']['hits'][0]['result']['api_path']
print(f'{GENIUS_URL}{song_id}/apple_music_player')
