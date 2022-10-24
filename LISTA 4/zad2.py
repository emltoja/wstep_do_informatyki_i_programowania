# Zadanie 2 Lista 4
import math
import matplotlib.pyplot as plt
import numpy as np

# Funkcja licząca silnię z danej liczby
def factorial(num):

    if num == 0:
        return 1
    return num * factorial(num - 1)


# Funkcja zwracająca n-ty wyraz rozwinięcia funkcji wykładniczej w szereg
def term(x, N):

    return x**N/factorial(N)


# Funkcja licząca przybliżenie funkcji wykładniczej po rozwinięciu w szereg
def calc_exp(x, N):

    result = 0
    for i in range(N + 1):
        result += term(x, i)
    return result


# Funkcja licząca błąd przybliżenia
def calc_err(x, N):
    
    return abs(calc_exp(x, N) - math.exp(x)) / math.exp(x)


# Funkcja tworząca i wyświetlająca wykresy
def visualize():

    xaxis = np.arange(1, 61, 1)
    yaxis1, yaxis2, yaxis3, yaxis4 = [], [], [], []
    
    # Obliczenie błędów dla podanych wartości
    for n in xaxis:

        yaxis1.append(calc_err(2, n))
        yaxis2.append(calc_err(10, n))
        yaxis3.append(calc_err(-2, n))
        yaxis4.append(calc_err(-10, n))

    # Utworzenie i opisanie 4 wykresów dla 4 podanych wartości
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].plot(xaxis, yaxis1)
    axs[0, 1].plot(xaxis, yaxis2)
    axs[1, 0].plot(xaxis, yaxis3)
    axs[1, 1].plot(xaxis, yaxis4)

    axs[0, 0].set_title(' x = 2 ')
    axs[0, 1].set_title(' x = 10 ')
    axs[1, 0].set_title(' x = -2 ')
    axs[1, 1].set_title(' x = -10 ')

    for ax in axs.flat:
        ax.set(xlabel='N', ylabel='error')
    
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.show()


visualize()








            
