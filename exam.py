#B1 изменяемыми ето когда мы можем изменит значение переменной и старая ссылка удалиитса останитска толко новая а неизменяемыми ето когда мы можем изменит значение но старая ссылка осатница и она будет потреблят памят



#B2 try-except-finally` нужны для того чтобы наш код не остоновился по середины работы к примеру если я не постовлю try except в своей функции то мой код выдаст ошыбку и мой код остоновитса



# B3 сравнение tuple о list tuple ето тотже самый лист но его нелзя изменит и у tuple нету методов по типу append() и remove() и tuple() нужен тогда когда нам не нужны методы листа и tuple(). работает значително быстрее 




# B4 переменне по типу  int float str bool ето коробки которые хранят определленый вид информации 
# int принимает числа без запятых
# float тоже принимает цисла но с запетыми после числа 
# str принимает все в качестве текста к примеру если мы будем принимат 14 то он примет его в качестве текста а не цифр
# bool он принимает толко True или False









# Короткие задачи


# No
def fibonacci(a):
    a1 = 1
    b = 1
    for i in range(1, a):
        a1+=i-1
        a1+b
        print(a1)


fibonacci(5)







# Done
# a = [i for i in range(1, 51) if i%3==0]
# print(a)





# Done
# cnt = 0
# with open("text.txt", "r") as file:
#     a1 = file.read()
#     for i in a1:
#         cnt += 1

# print(cnt)



# Done
# def word_count(text:str):
#     text = text.replace(".", " ")
#     text = text.replace(",", " ")
#     text = text.replace("!", " ")
#     text = text.replace("?", " ")
#     count = {}
#     text = text.lower()
#     for i in text.split():
#            if i in count:
#                count[i] += 1
#            else:
#                count[i] = 1
#     print(count)


# word_count("Hello, hello! Python is great. Python is fun.")












# Done
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, ammount):
#         self.balance+=ammount
#         print(f"Аккаунт {self.owner} пополнен ена {ammount} новый баланс {self.balance}" )
#     def widthraw(self, ammount):
#         if ammount<self.balance:
#             self.balance -=ammount
#             print(f"Аккаунт {self.owner} уменшен ена {ammount} новый баланс {self.balance}" )
#         else:
#             print("У тя столко денег нету!!!")
#     def __str__(self):
#         print(F"Owner: {self.owner}\nBalace: {self.balance} ")
# car1 = BankAccount("Alice", 1000)
# car1.deposit(500)
# car1.widthraw(2000)














# done
# from datetime import datetime
# def timing_decorator(func):
#     def init():
#         a = datetime.now()
#         func()
#         b = datetime.now()
#         print("Код сработал на",(b-a), "Милисикундах") 

#     return init
# @timing_decorator
# def pro():
#     sum=0
#     for i in range(1, 1000000):
#         sum+=i
#     print("Сумама:",sum)


# pro()



# # Done
# def process_grades(filemae):
#         try:
#             with open(filemae, "r") as file:
#                 ab = file.readlines()
#                 for i in ab:
#                     a1, a2 = i.split()
#                     with open("student.txt", "a") as li:
#                         if int(a2)>60:
#                             acc = "Passed"
#                         else:
#                             acc = "Failed"
#                         li.write(f"{a1} {a2} {acc}\n")

#         except FileNotFoundError:
#              print("File not found")
             
# process_grades("text.txt")