first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(couple_words[0]) - len(couple_words[1]) for couple_words in zip(first, second) if
                len(couple_words[0]) != len(couple_words[1]))

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))
