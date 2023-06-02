#https://github.com/s-getmanov/st_python6.git

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))
s = ""

# перебираем числа от A до B включая В.
for i in range(a,b+1):
    if i%2 == 0:
        s = s + str(i)+" "

print(s)