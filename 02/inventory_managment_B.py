with open('data/02a.txt') as f:
    words = [line.strip() for line in f]

# words = [
#     'abcde',
#     'fghij',
#     'klmno',
#     'pqrst',
#     'fguij',
#     'axcye',
#     'wvxyz'
# ]

def comparar(comp_word, words):
    for word in words:
        if comp_word == word:
            continue
        count = 0
        for i in range(len(word)):
            if word[i] != comp_word[i]:
                count += 1
                if count > 1:
                    break
        if count == 1:
            return comp_word, word
    return None, None

for word in words:
    one, two = comparar(word, words)
    if one is not None:
        break

for i in range(len(one)):
    if one[i] == two[i]:
        print(one[i], end='')






