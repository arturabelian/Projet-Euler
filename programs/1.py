# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5. 
# Ответ: 233168

sum_of_number = 0

for numb in range(1000):
	if numb % 3 == 0 or numb % 5 == 0:
		sum_of_number = sum_of_number + numb

print(sum_of_number)