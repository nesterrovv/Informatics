'''
Создайте программу, которая преобразует
введенное с клавиатуры двенадцатеричное число в систему с основанием
14 и выводит результат преобразования на экран.
'''

number = input()
sum = 0 
for i in range(len(number)):
    numeral = number[i]
    discharge = len(number) - 1 - i
    try:
        sum += int(numeral)* 12**(discharge)
    except:
        if number[i] == 'A':
            sum += 10 * 12**(discharge)
        elif number[i] == 'B':
            sum += 11 * 12**(discharge)
decimal_number = sum

result = ''
div = decimal_number
while div != 0:
    div = decimal_number // 14
    ost = decimal_number % 14
    if ost > 9:
        if ost == 10:
            ost = 'A'
        if ost == 11:
            ost = 'B'
        if ost == 12:
            ost = 'C'
        if ost == 13:
            ost = 'D'
    result += str(ost)
    decimal_number = div
print(result[::-1])