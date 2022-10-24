# Zadanie 7 Lista 3 

import math

# Funkcja obliczajaca pierwiastki trojmianu kwadratowego o podanych wspolczynnikach
def solve_quadratic(a, b, c):

    # Sprawdzenie przypadku gdy wspolczynnik przy x^2 jest rowny 0
    if a == 0:
        if b == 0:
            # Wypisanie odpowiedniego komunikatu gdy mamy doczynienia z wielomianem stopnia zerowego bądz wielomianem zerowym
            return 'Każda liczba rzeczywista jest pierwiastkiem' if c == 0 else 'Brak pierwiastkow'
        # Zwrocenie pierwiastka w przypadku gdy mamy doczynienia z wielomianem pierwszego stopnia
        return f'Jedynym pierwiastkiem jest liczba {-c/b}'

    # Obliczenie wyroznika trojmianu kwadratowego
    delta = b**2 - 4*a*c

    # Brak rozwiazan rzeczywistych w przypadku gdy wyroznik jest mniejszy od 0
    if delta < 0:
        return 'Brak pierwiastkow'
    # Jedno rozwiazanie w przypadku gdy wyroznik jest rowny 0
    if delta == 0:
        return f'Jedynym pierwiastkiem jest liczba {-b/(2*a)}'
    
    # Obliczenie obu pierwiastkow trojmianu
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return f'Pierwiastki trojmianu to {x1} oraz {x2}'


print('Podaj współczynniki trójmainu kwadratowego w postaci a*x^2 + b*x + c')
a = input('Podaj a ')
b = input('Podaj b ')
c = input('Podaj c ')
print(solve_quadratic(float(a), float(b), float(c)))
