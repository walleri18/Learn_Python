import random

#Даны два массива из N целых чисел каждый.
# Определить, для какого из них среднее арифметическое значение элементов больше.
# Для решения задачи написать функцию, принимающую массив в качестве параметра и возвращающую среднее значение.

#Функция для подсчёта среднего арифметического массива
def arifmeticMean(massiv):
    resultArifmeticMean = sum(massiv)
    resultArifmeticMean /= len(massiv)
    return resultArifmeticMean

print("Экзаменационная задача №7. Два массива, их среднии арифметические, сравнение\n\n")

#Создаём массивы
N = random.randint(1,10)

massivOne = []
massivTwo = []

for i in range(N):
    massivOne.append(random.randint(-100, 100))
    massivTwo.append(random.randint(-100, 100))

#Считаем и выводим результат
print("Среднее арифметическое первого массива: " + str(arifmeticMean(massivOne)))
print("Среднее арифметическое второго массива: " + str(arifmeticMean(massivTwo)))

if arifmeticMean(massivOne) > arifmeticMean(massivTwo):
    print("Среднее арифметическое первого массива больше среднего арифметического второго массива")
elif arifmeticMean(massivTwo) > arifmeticMean(massivOne):
    print("Среднее арифметическое второго массива больше среднего арифметического первого массива")
else:
    print("Среднии арифметического первого и второго массива равны")

input("\n\nДля завершения нажмите любую клавишу...")