print("Добро пожаловать в Арифметический калькулятор!!!\n\n")

while True:
    operation = input("Введите пожалуйста необходимую"
                      " арфметическую операцию(+,-,*,/): ")
    one_argument = input("\n\nВведите пожалуйста первый аргумент: ")
    two_argument = input("\n\nВведите пожалуйста второй аргумент: ")

    one = float(one_argument)
    two = float(two_argument)

    print("\n\nРезультат вычислений: ")

    if operation == "+":
        print(one_argument + " " + operation + " " + two_argument + " = " + str(one + two))
    elif operation == "-":
        print(one_argument + " " + operation + " " + two_argument + " = " + str(one - two))
    elif operation == "*":
        print(one_argument + " " + operation + " " + two_argument + " = " + str(one * two))
    elif operation == "/":
        print(one_argument + " " + operation + " " + two_argument + " = " + str(one / two))
    else:
        print(one_argument + " " + operation + " " + two_argument + " = ?" +
              "\n\nНеизвестная операция. Я не могу вычислить")

    select = input("Желаете продолжить вычисления?(Yes/No)")

    if select == "No" or select == "N":
        break

    print("\n\n")

print("Для выхода из программы нажмите любую клавишу...")