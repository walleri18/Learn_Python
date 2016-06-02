#Подключяем математическую библиотеку
import math

#Условие экзаменационной задачи №1 для C++
# Задано два момента времени в часах, минутах и секундах (в пределах одних суток).
# Найти длительность промежутка времени между этими моментами в тех же единицах.

#Количество часов в сутках
HOURS = 24

#Количество минут в часе
MINUTES = 60

#Количество секунд в минуте
SECONDS = 60


print("Экзаменационная задача №1. Промежутки времени.\n\n")

#Объявление и инициализация переменных для первого и второго момента
oneHour = 0
oneMinute = 0
oneSecond = 0
twoHour = 0
twoMinute = 0
twoSecond = 0

#Узнаём первый момент
while True:
    oneHour = int(input("Введите пожалуйста количество часов в первом моменте: "))
    oneMinute = int(input("\nВведите пожалуйста количество минут в первом моменте: "))
    oneSecond = int(input("\nВведите пожалуйста количество секунд в первом моменте: "))

    #Если момент времени записан в правильном пределе, то идём дальше
    if (oneHour < HOURS and oneHour > 0) and (oneMinute < MINUTES and oneMinute > 0) and (oneSecond < SECONDS and oneSecond > 0):
        break
    else:
        print("\nОШИБКА!!!\n\n\n")

#Узнаём второй момент
while True:
    twoHour = int(input("\nВведите пожалуйста количество часов во втором моменте: "))
    twoMinute = int(input("\nВведите пожалуйста количество минут во втором моменте: "))
    twoSecond = int(input("\nВведите пожалуйста количество секунд во втором моменте: "))

    # Если момент времени записан в правильном пределе, то идём дальше
    if (twoHour < HOURS and twoHour > 0) and (twoMinute < MINUTES and twoMinute > 0) and (twoSecond < SECONDS and twoSecond > 0):
        break
    else:
        print("\nОШИБКА!!!\n\n\n")

#Переводим всё в секунды
tmpOneAllSeconds = oneHour * MINUTES * SECONDS + oneMinute * SECONDS + oneSecond
tmpTwoAllSeconds = twoHour * MINUTES * SECONDS + twoMinute * SECONDS + twoSecond

#Узнаём разницу между моментами в секундах
resultAllSeconds = tmpOneAllSeconds - tmpTwoAllSeconds
resultAllSeconds = math.fabs(resultAllSeconds)#Модуль числа

#Раскладываем на часы, минуты и секунды
resultHour = int(resultAllSeconds // (MINUTES * SECONDS))
resultMinute = int((resultAllSeconds % (MINUTES * SECONDS)) // SECONDS)
resultSecond = int((resultAllSeconds % (MINUTES * SECONDS)) % SECONDS)

#Выводим результат
print("\n\nРезультат: " + str(resultHour) + " часов " + str(resultMinute) + " минут " + str(resultSecond) + "\n\n")

input("Для завершения нажмите любую клавишу...")