import random

#Экзаменационная задача №3 для C++
#Написать программу, которая для целочисленного массива из N элементов определяет,
# сколько положительных элементов располагается между его максимальным и минимальным элементами

print("Экзаменационная задача №3. Подсчёт количества положительных элементов между "
      "минимальными и максимальными элементами\n\n")

#Получение размера списка (массива)
N = int(input("Какого размера массив Вы желаете?: "))

#Объявляем и инициализируем пустой список (подразумеваем, что это массив)
massiv = []

#Наш искомый результат
countPositiveElement = 0

for i in range(N):
    massiv.append(random.randint(-100,100))

#Индекс максимального элемента
maximumIndexElement = massiv.index(max(massiv))

#Индекс минимального элемента
minimumIndexElement = massiv.index(min(massiv))

if minimumIndexElement > maximumIndexElement:
    for i in range(maximumIndexElement + 1, minimumIndexElement):
        if massiv[i] > 0:
            countPositiveElement += 1
elif maximumIndexElement > minimumIndexElement:
    for i in range(minimumIndexElement + 1, maximumIndexElement):
        if massiv[i] > 0:
            countPositiveElement += 1

print("\n\nРезультат работы программы:\n")
if countPositiveElement != 0:
    print("Максимальное число: " + str(max(massiv)))
    print("Индекс максимального числа: " + str(maximumIndexElement) + "\n")
    print("Минимальное число: " + str(min(massiv)))
    print("Индекс минимального числа: " + str(minimumIndexElement) + "\n")
    print("Количество положительных чисел: " + str(countPositiveElement))
else:
    print("Максимальное число: " + str(max(massiv)))
    print("Индекс максимального числа: " + str(maximumIndexElement) + "\n")
    print("Минимальное число: " + str(min(massiv)))
    print("Индекс минимального числа: " + str(minimumIndexElement) + "\n")
    print("Положительные числа отсутствуют")

input("\n\nДля завершения нажмите любую клавишу...")