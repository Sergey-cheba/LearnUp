
# 1. Создать класс User. В нем определить метод setLogin(login). Логин должен содержать только латинские буквы, 
# цифры и знак подчеркивания. Длина login должна быть меньше 20 символов. Если login не соответствует этим требованиям, 
# необходимо выбросить WrongLoginException.
import re

class User():
    def setLogin(self,login):
        try:
            if re.fullmatch(r'[A-Za-z0-9_]{,20}', login):
                self.login = login
                print("Логин сохранен")
            else:
                raise Exception("Логин не соответсвует условиям")    
        except Exception:
            print("WrongLoginException")
     
         
        
user = User()

user.setLogin("123123asd_") # True 
user.setLogin("123456789zxcvbnmasdfg") # False больше 20 символов
user.setLogin("123456789привет") # False Присутствует кириллица
user.setLogin("123123!!!") # False Присутствуют другие символы

print("FIN")
        
