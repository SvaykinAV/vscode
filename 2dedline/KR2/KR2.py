# Вариант 10:
# Шаг 1: Ввод зашифрованной строки (можно вставить свой текст)
s = input("Введите зашифрованную строку: ")
# Очистка строки: оставляем только латинские буквы и приводим к нижнему регистру
cleaned = ""
for char in s:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        cleaned += char.lower()
# Если после очистки строка пустая
if not cleaned:
    print("Нет латинских букв в строке.")
else:
# Общее количество букв
    total = len(cleaned)  
    # Шаг 2: Подсчитываем частоту каждой буквы
    freq = {}
    for char in cleaned:
        freq[char] = freq.get(char, 0) + 1
    # Перевод в проценты
    for char in freq:
        freq[char] = round(freq[char] / total * 100, 2)
    # Шаг 3: Находим топ-3
    sorted_letters = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    top3 = sorted_letters[:3]
    print("\nТоп-3 самых частых букв:")
    for i, (letter, percentage) in enumerate(top3, 1):
        print(f"{i}. '{letter}' — {percentage}%")
    # Шаг 4: Проверяем гипотезу про английский язык
    most_common = sorted_letters[0][0]
    if most_common == 'e':
        print("\nВероятно, английский язык")
    else:
        print("\nЯзык не определен")