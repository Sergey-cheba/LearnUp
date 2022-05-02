# Создать консольный интерфейс для регистрации новых пользователей и просмотра списка аккаунтов. 
# К классу User добавить 3 любых свойства и методы для установки их значений. 
# В случае возникновения исключений при создании объектов класса User, выводить предупреждающие сообщения и 
# продолжать корректно работать с приложением.

import re
import random
import string

class User():

    def setLogin(self):
        self.login = 0
        while self.login == 0:
            login = input("Введите логин ")
            try:
                if re.fullmatch(r'[A-Za-z0-9_]{,20}', login):
                    self.login = login
                    print("Логин сохранен")
                else:
                    raise Exception("Логин не соответсвует условиям")    
            except Exception as x:
                print(x)
        

    def setPassword(self):
        self.password = 0
        while self.password == 0:
            password = input("Введите пароль ")
            confirmPassword = input("Повторите пароль ")
            try:
                if re.fullmatch(r'[A-Za-z0-9_]{,20}', password) and password == confirmPassword:
                    self.password = password
                    print("Пароль сохранен")
                else:
                    raise Exception("Пароль не соответсвует условиям")    
            except Exception as x:
                print(x)

    def setNickname(self,nickname):
        self.nickname = nickname


def newAccount(name):
    name = User()
    name.setLogin()
    name.setPassword()
    name.setNickname(input("Введите свой ник "))
    return name

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

a = 0
arr = []

while a == 0:
    start = int(input("Выберите дейстивие" + "\n" + "1 - Создать аккаунт" + "\n" + "2 - Посмотреть список аккаунтов"+ "\n" + "3 - Завершить программу"+ "\n"))
    if start == 1:
        arr.append(newAccount(generate_random_string(10)))
        print("Аккаунт успешно сохранен")
    elif start == 2:
        for i in arr:
            print(i.__dict__)
    elif start == 3:
        a = 1
        print("Программа завершена")
    else:
        start = int(input("Попробуй снова" + "\n" "Выберите дейстивие" + "\n" + "1 - Создать аккаунт" + "\n" + "2 - Посмотреть список аккаунтов"+  "\n" + "3 - Завершить программу"+ "\n"))

