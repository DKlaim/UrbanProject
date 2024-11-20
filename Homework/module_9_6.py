def all_variants(text):
    i = 1
    for j in range(1, len(text) + 1):
        while i != len(text) + 1:
            yield text[i - j:i]
            i += 1
        i = 1


a = all_variants("abc")
for i in a:
    print(i)
