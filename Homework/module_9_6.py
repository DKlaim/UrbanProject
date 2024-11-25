def all_variants(text):
    i = j = 1
    for n in range(1, len(text) + 1):
        while i != len(text) + 1:
            yield text[i - n:i]
            i += 1
        j += 1
        i = j


a = all_variants("abc")
for i in a:
    print(i)
