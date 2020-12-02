'''
Создайте программу, которая выводит на экран
дополнительный код введенного с клавиатуры шестнадцатеричного числа
на восемь разрядов
'''

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is

sum = 0
number = input()

for i in range (len(number)):
    numeral = number[i]
    discharge = 7 - i
    try:
        sum += int(numeral)* 16**(discharge)
    except:
        if number[i] == 'A':
            sum += 10 * 16**(discharge)
        elif number[i] == 'B':
            sum += 11 * 16**(discharge)
        elif number[i] == 'C':
            sum += 12 * 16**(discharge)
        elif number[i] == 'D':
            sum += 13 * 16**(discharge)
        elif number[i] == 'E':
            sum += 14 * 16**(discharge)
        elif number[i] == 'F':
            sum += 15 * 16**(discharge)
            
decimal_number = sum
binary_number = bin(decimal_number)
binary_number = int(binary_number.replace('0b', ''))
print(twos_comp(binary_number, 8))