# Zadanie 3 Lista 4

import math

x = 9.8 ** 201
y = 10.2 ** 199

# Funkcja sprawdzająca która metoda powoduje błąd przekroczenia zakresu
def check():
    try:
        z1 = math.sqrt(x**2 + y**2)
    except OverflowError:
        z1 = None
        print('Pierwsza metoda powoduje blad przekroczenia zakresu')

    try:
        z2 = y * math.sqrt((x/y)**2 + 1)
    except OverflowError:
        z2 = None
        print('Druga metoda powoduje blad przekroczenia zakresu')
    
    return z1, z2
 
def main():
    
    z1, z2 = check()
    if z1:
        return f'Pierwsza metoda zwraca wynik {z1}'
    if z2:
        return f'Druga metoda zwraca wynik {z2}'

print(main())