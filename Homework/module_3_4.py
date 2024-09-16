def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word in word:
            same_words.append(word)
        else:
            if word.lower() in root_word.lower():
                same_words.append(word)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
