with open('data/01a.txt') as f:
    numbers = [int(line.strip()) for line in f]

print(sum(numbers))