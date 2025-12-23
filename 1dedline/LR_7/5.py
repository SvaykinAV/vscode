import math
user_input = input("Введите выражение (число1 знак число2): ")
parts = user_input.split()
if len(parts) != 3:
    print("Ошибка: введите выражение в формате 'число1 знак число2'")
else:
    try:
        n1 = float(parts[0])
        operator = parts[1]
        n2 = float(parts[2])
        result = None
        if operator == '+':
            result = n1 + n2
        elif operator == '-':
            result = n1 - n2
        elif operator == '*':
            result = n1 * n2
        elif operator == '/':
            result = n1 / n2 if n2 != 0 else "Ошибка: деление на ноль!"
        elif operator == '%':
            result = n1 % n2 if n2 != 0 else "Ошибка: деление на ноль!"
        elif operator == '//':
            result = n1 // n2 if n2 != 0 else "Ошибка: деление на ноль!"
        elif operator == '**':
            result = n1 ** n2
        elif operator == '%%':
            result = (n2 / 100) * n1
        elif operator == '/**':
            if n1 < 0:
                result = "Ошибка: нельзя извлечь корень из отрицательного числа"
            else:
                result = math.sqrt(n1)
        else:
            result = f"Ошибка: неизвестный оператор '{operator}'"
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: введите корректные числа")