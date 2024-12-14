from queue import Queue
import requests
from threading import Thread

ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

all_songs = []


class GetGenre(Thread):

    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        genre = requests.get(RANDOM_GENRE_API_URL).json()
        self.queue.put(genre)


class Genius(Thread):

    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        genre = self.queue.get()
        data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
        data = data.json()
        try:
            song_id = data['response']['hits'][0]['result']['api_path']
            # print(f'{GENIUS_URL}{song_id}/apple_music_player')
            all_songs.append(f'{GENIUS_URL}{song_id}/apple_music_player')
        except IndexError as e:
            pass


queue = Queue()

# genre_thread = GetGenre(queue)
# genius_thread = Genius(queue)
#
# genre_thread.start()
# genius_thread.start()
#
# genre_thread.join()
# genius_thread.join()

genre_list = []
genius_list = []

for _ in range(10):
    thread = GetGenre(queue)
    thread.start()
    genre_list.append(thread)

for _ in range(10):
    thread = Genius(queue)
    thread.start()
    genius_list.append(thread)

for thread in genius_list:
    thread.join()

print(all_songs)
print(len(all_songs))
