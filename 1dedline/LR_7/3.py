text = input("Введите произвольный текст: ")
word = input("Введите слово: ")
if word in text:
    count = text.count(word)
    print(f"Слово '{word}' встречается в тексте {count} раз(а)")
else:
    print(f"Слово '{word}' не найдено в тексте")