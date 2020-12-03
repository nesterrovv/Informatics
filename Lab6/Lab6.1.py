'''
Кортежи
'''
# создание кортежа
a1 = tuple()
a2 = 1, 2, 3, "abc"
a3 = (1, 2, 3, "abc")
print("Tuple a1 = ", a1)
print("Tuple a2 = ", a2)
print("Tuple a3 = ", a3)
# создание кортежа из других структур данных
l = [1, 2, 3, "abc"] # из списка
a4 = tuple(l)
print("Tuple a4 from list l = ", a4)
a5 = tuple("Hello, World!") # из строки
print("Tuple a5 from string = ", a5)
# вложенность кортежей
a6 = a2, a3
print("Tuple a6 formed by a2 and a3 = ", a6)
# объединение кортежей
a7 = a2 + a3
print("Tuple a7 by combining a2 and a3 = ", a7)
# доступ к элементам кортежей
print("a6[0]: ", a6[0])
print("a6[0][3]: ", a6[0][3])
# a6[0][3] = "cba"
'''
В случае раскомметирования строки 26 выдаст ошибку, т.к. нельзя
переопределять элементы кортежа, который является неизменяемым объектом
'''
print("\n")

day = int(input('Enter the day of birth '))
month = input('Enter the month of birth ')
year = int(input('Enter the year of birth '))
surname = input('Enter your surname ')
name = input('Enter your name ')
second_name = input('Enter your second name ')
k1 = (day, month, year)
k2 = (surname, name, second_name)
k3 = k1 + k2
print(k3)

k4 = k1, k2
print(k4)
print(k4[1][1])