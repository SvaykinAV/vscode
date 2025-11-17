n = int(input("Введите число: "))
s = 0
while n > 0:
    s += n % 10
    n = n // 10
print(f"Сумма цифр: {s}")