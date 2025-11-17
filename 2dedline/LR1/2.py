count = 0
while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    count += 1
print(F"Количество введённых чисел до нуля: {count}")