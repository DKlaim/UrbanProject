class WordsFinder:
    def __init__(self, *files):
        self.file_names = str(files)[1:-1].replace(",", '').replace("'", '').split(' ')

    def get_all_words(self):
        all_words = {}
        list_words = []
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ', ' — ']:
                        line = line.lower().replace(symbol, '')
                    list_words += line.split()
            all_words[file_name] = list_words
            list_words = []
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                return {name: words.index(word.lower()) + 1}

    def count(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                return {name: words.count(word.lower())}


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
