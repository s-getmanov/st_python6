#https://github.com/s-getmanov/st_python6.git

n = int(input("Введите количество чисел: "))
input_null = 0

for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    if num == 0:
        input_null = input_null+1 

print(f"Вы ввели {input_null} нулей.")


