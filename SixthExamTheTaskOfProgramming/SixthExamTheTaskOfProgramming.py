#Имеется строка текста и слово. Определить, сколько раз встречается в тексте каждая буква слова.

print("Экзаменационная задача №6. Строка, строчка, количество вхождений каждой буквы слова в строке.\n")

#Принимаем строку
studiedLine = input("Введите пожалуйста исследуемую строку: ")

#Принимаем слово
analyzedWord = input("Введите пожалуйста исследуемое слово: ")

#Для удобства делаем строку studiedLine в виде списка
newStudiedLine = []

#Копируем посимвольно строку в список
for i in range(len(studiedLine)):
    newStudiedLine.append(studiedLine[i])

#Удаляем строку из-за ненадобности
del studiedLine

#Делаем проверку того что в analyzedWord слово, а не строка
newAnalyzedWord = []

#Флаг на проверку того, что символ уже записали
flag = False

for i in range(len(analyzedWord)):

    #Если это не пробел
    if flag == True and analyzedWord[i] == " ":
        del analyzedWord
        del flag
        break

    elif analyzedWord[i] != " ":

        #Меняем флаг, говорящий, что в списке есть как минимум один элемент
        flag = True

        #Посимвольно копируем строку в список
        newAnalyzedWord.append(analyzedWord[i])

#Считаем количество вхождений каждого символа слова в строке
counterChar = []

for i in range(len(newAnalyzedWord)):
    counterChar.append(newStudiedLine.count(newAnalyzedWord[i]))

#Вывод результата
print("\nРезультат: \n")

for i in range(len(newAnalyzedWord)):
    print(newAnalyzedWord[i] + ": " + str(counterChar[i]))

input("\nДля завершения нажмите любую клавишу...")