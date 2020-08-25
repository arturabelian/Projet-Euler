# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

# 999 * 999 = 998001

# Ответ: - 906609

def palindrome():
    palindromes = (i * j for i in reversed(range(100, 1000)) for j in reversed(range(100, 1000)) if str(i * j) == str(i * j)[::-1])
    return max(palindromes)

result = palindrome()
print(result)

