#https://github.com/s-getmanov/st_python6.git

# Введем исходное число
count = 0
x = int(input("Введите натуральное число X: "))
if x <= 2000000000:   
    # перебираем числа от 1 до x включительно.
    for i in range(1, x+1):
        if x % i == 0:
            count += 1
    # Выведем результат
    print("Количество делителей числа", x, "равно", count)
else:
    print("Ошибка: число X больше 2 миллиардов.")



