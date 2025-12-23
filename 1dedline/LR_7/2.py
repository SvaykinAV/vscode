password1 = input("Введите пароль: ")
password2 = input("Подтвердите пароль: ")
if password1 == password2:
    print("Пароль сохранен")
    login_password = input("Введите пароль для авторизации: ")
    if login_password == password1:
        print("Access")
    else:
        print("Denied")    
else:
    print("Пароли не совпадают")