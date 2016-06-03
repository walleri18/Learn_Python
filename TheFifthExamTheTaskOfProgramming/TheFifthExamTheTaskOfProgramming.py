import random

#Написать программу, которая для целочисленной матрицы размером (N x M)
# определяет среднее арифметическое её элементов, а также количество положительных
# и отрицательных элементов в каждой строке.

print("Экзаменационная задача №5. Матрица, среднее арифметическое, "
      "количество отрицательных и положительных элементов в каждой строке")

#Количество строк матрицы
N = random.randint(0, 10)

#Количество столбцов матрицы
M = random.randint(0, 10)

#Наша матрица
matrix = []

#Заполняем матрицу
for i in range(N):

    #Создаём буферную строку матрицы
    stringMatrix = []

    #Заполняем буферную строку матрицы
    for j in range(M):
        stringMatrix.append(random.randint(-100, 100))

    #Вставляем буферную строку матрицы
    matrix.append(stringMatrix)

    #Удаляем буферную строку матрицы
    del stringMatrix

#Считаем среднее арифметическое матрицы
arithmeticMean = 0.0

for i in range(N):
    for j in range(M):
        arithmeticMean += matrix[i][j]

arithmeticMean /= (N * M)

#Определим количество положительных и количество отрицательных элементов в каждой строке
numberPositive = []
numberNegative = []

for i in range(N):

    #Временная переменная хранящая количество положительных элементов в i-ой строке
    countPositive = 0

    #Временная переменная хранящая количество отрицательных элементов в i-ой строке
    countNegative = 0

    for j in range(M):
        if matrix[i][j] > 0:
            countPositive += 1
        elif matrix[i][j] < 0:
            countNegative += 1

    #Добавляем количество положительных и количество отрицательных элементов по каждой строке
    numberPositive.append(countPositive)
    numberNegative.append(countNegative)

#Вывод результата
print("\nСреднее арифметическое матрицы размеров " + str(N) + " * " + str(M) + ": " + str(arithmeticMean) + "\n")

for i in range(N):
    print("Количество положительных чисел в " + str(i + 1) + " строке: " + str(numberPositive[i]))
    print("Количество отрицательных чисел в " + str(i + 1) + " строке: " + str(numberNegative[i]))

input("\n\nДля завершения нажмите любую клавишу...")