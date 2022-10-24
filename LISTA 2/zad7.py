# Zadnaie 7     Lista 2

def fib_sequence(n):

    result = []
    for i in range(n):
        result.append(fib(i))
    return result

def fib(n):

    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    

print(fib_sequence(10))
