text = input("Введите строку: ")
ct = text.lower().replace(" ","")
left = 0
right = len(ct) - 1
print(f"Проверяем строка (без пробелов и в нижнем регистре): '{ct}'")
while left < right:
    print(f"Сравниваем '{ct[left]}' и '{ct[right]}'")
    if ct[left] != ct[right]:
        print("Символы не совпадают!")
        break
    left += 1
    right -= 1
else:
    print(f"Строка '{text}' является палиндром")
if left < right:
    print(f"Строка '{text}' не является палиндром")