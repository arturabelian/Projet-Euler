# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

# Какое самое маленькое число делится нацело на все числа от 1 до 20?

# Ответ: 232792560

def conditions(i):
    if i % 1 == 0 and i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
        print(i)
        
for i in range(1, 300000000, 5):
    conditions(i)



