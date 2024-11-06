class WordsFinder:
    def __init__(self, *files):
        self.file_names = str(files)[1:-1].replace(",", '').replace("'", '').split(' ')
        # print(self.file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ', ' — ']:
                        line = line.replace(symbol, '')
                    print(line.lower(), end='')

    def find(self, word):
        pass

    def count(self, word):
        pass


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt, Captain.txt')
    finder2.get_all_words()
