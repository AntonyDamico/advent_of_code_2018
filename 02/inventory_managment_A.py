with open('data/02a.txt') as f:
    words = [line.strip() for line in f]

# def check_rep(word):
#     # if there's just one letter in the word it does not
#     # make sense to check for duplicates
#     wdict = {}
#     while len(word) > 1:
#         cuenta = word.count(word[0])
#         wdict[cuenta] = 1
#         word = word.replace(word[0], '')
#     return wdict

def check_rep(word):
    # if there's just one letter in the word it does not
    # make sense to check for duplicates
    double = 0
    triple = 0
    while len(word) > 1:
        cuenta = word.count(word[0])
        if cuenta == 2:
            double = 1
        if cuenta == 3:
            triple = 1
        word = word.replace(word[0], '')
    return double, triple



# words = [
#     'abcdef',
#     'bababc',
#     'abbcde',
#     'abcccd',
#     'aabcdd',
#     'abcdee',
#     'ababab',
# ]

double = 0
triple = 0

for word in words:
    duplicate, triplicate = check_rep(word)
    double += duplicate
    triple += triplicate

print(double, triple)

print(double * triple)