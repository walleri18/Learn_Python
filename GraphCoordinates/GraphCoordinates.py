#Экзаменационное задание №2 для C++. График функций.
#Написать программу, которая по введённому значению аргумента вычисляет значение функции, заданной в виде графика

print("Экзаменационное задание №2. График функций.\n\n")

while True:

    #Получаем аргумент
    argument = float(input("Введите пожалуйста аргумент для функции графика: "))
    result = 0

    #Сравнение аргумента с диапозонами и вычисление результата функций
    if argument <= -2 or argument >= 2:
        result = 0

    elif argument > -2 and argument < -1:
        result = -(2 + argument)

    elif argument > 1 and argument < 2:
        result = 2 - argument

    else:
        result = argument

    print("\n\nРезультат вычислений для аргумента " + str(argument) + ": " + str(result) + "\n\n")

    select = input("Желаете продолжить?(Yes/No):")

    if select == "No" or select == "n" or select == "N":
        break
    else:
        print("\n\n")

input("\n\nДля завершения нажмите любую клавишу...")