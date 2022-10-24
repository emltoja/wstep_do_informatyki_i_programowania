# Zad 6 Lista 3

# Funkcja wyliczająca silnię podanej liczby
def factorial(n):

    if n == 0:
        return 1
    return n * factorial(n - 1)

# Funkcja licząca symbol Newtona podanych liczb
def binomial_coefficient(n, k):

    return factorial(n) / (factorial(k) * factorial(n - k))

# Funkcja zwracająca n pierwszych wierszy trojkata Paskala
def pascal_triangle(n):

    result = []

    for i in range(n):
        row = []
        for k in range(i+1):
            row.append(binomial_coefficient(i, k))
        result.append(row)

    return result

for row in pascal_triangle(7):
    print(row)
