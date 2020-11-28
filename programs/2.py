# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают 4 000 000.
# Ответ: 4613732

sum_of_number = []

def fib(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
        if a % 2 == 0:
            sum_of_number.append(a)
    print(sum(sum_of_number))
fib(4000000)