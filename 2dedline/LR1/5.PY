text = input("Введите текст: ")
glasnie = "аоеиыяуюэёeyuoaiАОЕИЫЯУЮЭЁEYUOAI"
result = ""
i = 0
while i < len(text):
    if text[i] not in glasnie:
        result += text[i]
    i += 1
print("Результат", result)
