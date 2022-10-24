# Zadanie 5     Lista 2

import time

def char_counter(string, char):
    string = string.upper()
    char = char.upper()
    count = 0
    for letter in string:
        if char == letter:
            count += 1
    return count

def built_in_char_counter(string, char):
    string = string.upper()
    char = char.upper()
    return string.count(char)

start1 = time.time()

for _ in range(10**5):
    char_counter('anaconda', 'a')

end1 = time.time()

print(end1 - start1)

start2 = time.time()

for _ in range(10**5):
    built_in_char_counter('anaconda', 'a')

end2 = time.time()

print(end2 - start2)
