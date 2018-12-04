with open('data/01a.txt') as f:
    numbers = [int(line.strip()) for line in f]

# def check_frec(numbers):
#     final_frecs = [0]
#     frec = 0
#     i = 0
#     while True:
#         frec += numbers[i]
#         if frec in final_frecs:
#             return frec
#         final_frecs.append(frec)
#         i += 1
#         if i == len(numbers):
#             i = 0

def check_frec(numbers):
    frec = 0
    seen_frecs = {frec}
    
    while True:
        for num in numbers:
            frec += num
            if frec in seen_frecs:
                return frec
            seen_frecs.add(frec)

# def check_frec(s: str) -> int:
#     val = 0
#     seen = {val}

#     while True:
#         for num in numbers:
#             val += num
#             if val in seen:
#                 return val
#             else:
#                 seen.add(val)

print(check_frec(numbers))

# print(check_frec([-6, +3, +8, +5, -6]))
