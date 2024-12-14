import pprint
import requests
import datetime
from queue import Queue
from threading import Thread, Event

ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

all_songs = []


class GetGenre(Thread):

    def __init__(self, queue, stop_event):
        self.queue = queue
        self.stop_event = stop_event
        super().__init__()

    def run(self):
        while not stop_event.is_set():  # GetGenre работает пока не получит изменение флага stop_event
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
            all_songs.append({'genre': genre, 'song': f'{GENIUS_URL}{song_id}/apple_music_player'})
        except IndexError as e:
            self.run()  # в случае невозможности получить ссылку на саундтрек, запускаем повторный запрос


queue = Queue()
stop_event = Event()

genre_list = []
genius_list = []

time_start = datetime.datetime.now()
# Запускаем поток GetGenre
for _ in range(4):
    GetGenre_thread = GetGenre(queue, stop_event)
    GetGenre_thread.start()
    genre_list.append(GetGenre_thread)

for _ in range(100):
    Genius_thread = Genius(queue)
    Genius_thread.start()
    genius_list.append(Genius_thread)

for thread in genius_list:
    thread.join()
stop_event.set()  # после отработки всего списка genius_list меняем флаг stop_event на set и завершаем работу GetGenre

for thread in genius_list:  # завершающий шаг прохода по списку genius_list
    thread.join()
time_end = datetime.datetime.now()
print(f'Список ссылок на саундтреки:')
pprint.pprint(all_songs)
print(f'Оставшееся количество необработанных ссылок в очереди: {queue.qsize()}')
print(f'Количество полученных ссылок: {len(all_songs)}')
print(time_end-time_start)
