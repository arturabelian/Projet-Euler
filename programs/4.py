# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

# 999 * 999 = 998001

# Ответ: - 997799

def reverse(n):
	a = int(n)
	rev = 0
	while( a > 0):
		dig = a % 10
		rev = rev * 10 + dig
		a = a // 10
	return rev
	

def ispalindrom(num):
	a = reverse(num)
	if a == num:
		return True
	else:
		return False
	

for i in range(998001):
	inc = ispalindrom(i)
	if inc == True:
		print(i)

