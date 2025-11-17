from random import randint
random_num = randint(1, 100)
guess = None
print("Угадай число от 1 до 100!")
while guess != random_num:
    guess = int(input("Ваша попытка: "))
    if guess < random_num:
        print("Загаданное число БОЛЬШЕ")
    elif guess > random_num:
        print("Загаданное число МЕНЬШЕ")
    else:
        print("Вы угадали число, Поздравляю! ")