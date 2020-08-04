# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5. 
# Ответ: 233168

sum = 0 # Создаем переменную для значения суммы.

for m in range(1000): # Для m в диапазоне от 0 до 1000. 
	if m % 3 == 0 or m % 5 == 0: # Если у m остаток от деления на 3 или на 5 = 0.
		sum = sum + m # То к сумме прибавляем значение m
	else: # Иначе
		pass # Пропускаем.
print(sum) # Вывод значения суммы.