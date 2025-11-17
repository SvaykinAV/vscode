symvol = input("Введите символ для рисования: ")
height = int(input("Введите высоту прямоугольник: "))
width = int(input("Введите ширину прямоугольний: "))
i = 0
while i < height:
    j = 0
    while j < width:
        print(symvol, end="")
        j += 1
    print()
    i += 1