string = input("Введите логическое выражение: ")
str1, str2, str3, str4, str5 = string.split()
expression_ru = string.replace("and", "и").replace("or", "или").replace("False", "Ложь").replace("True", "Правда")
print(f"Выражение на русском: {expression_ru}")
match str1:
    case "True":
        bool1 = True
    case "False":
        bool1 = False
match str3:
    case "True":
        bool2 = True
    case "False":
        bool2 = False

match str5:
    case "True":
        bool3 = True
    case "False":
        bool3 = False
match str2:
    case "and":
        match str4:
            case "or":
                result = (bool1 and bool2) or bool3
            case "and":
                result = bool1 and bool2 and bool3
    case "or":
        match str4:
            case "and":
                result = bool1 or (bool2 and bool3)
            case "or":
                result = bool1 or bool2 or bool3
print(f"Результат: {result}")