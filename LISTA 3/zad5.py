# Zadanie 5 lista 3

# Wyliczanie największego wspólnego dzielnika dwóch liczb za pomocą algorytmu Euklidesa
def euclid_algorithm(a, b):

    # Liczenie NWD w trywialnych przypadkach
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    
    greater = max(a, b)
    smaller = min(a, b)

    while smaller != 0:
        smaller, greater = greater % smaller, smaller

    return greater

# Wyliczenie NWD wszystkich liczb z listy
def greatest_common_divisor(num_list):

    result = 0

    for number in num_list:
        result = euclid_algorithm(result, number)
    
    return result

print(greatest_common_divisor([6513889451940018351850, 3203591805002300, 754054134000235012350003591359000]))
