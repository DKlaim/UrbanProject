from .mod1 import hello
# from Lessons_4.mods.mod1 import hello  # Пример абсолютного импорта (указываем абсолютный путь от корневой директории)


def good_word(name):
    hello(name)
    print(f'{name}, ты лучший!')

if __name__ == '__main__':
    good_word('Urban')