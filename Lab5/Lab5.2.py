'''
Циклы
'''
# while
print("Numbers < 10 (while):")
i = 0
while (i<10):
    print(i, end=" ") # print in one line
    i += 1
    print("\n")

# for
print("Numbers < 10 (for):")
for i in range(0,10):
    print(i, end=" ")
else:
    print("\nThe next number is 10\n")
# break
sum = 0
for i in range(0,100):
    if i > 10:
        print("\nWe reached the end, final sum: ",sum)
        break
    sum += i
# continue
i = 0
while i<=15:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print("\n")

# pass
print("Let's print numbers again!")
for i in range(0,10):
    pass
    print(i, end=" ")
print("\n\n")

# Job with for-cycle
for i in range(500):
    if i % 7 == 0:
        print(i, end = ' ')
else:
    print('\n' + 'All numbers were printed!')

# Job with while-cycle
i = 0
while i != 500:
    if i % 7 == 0:
        print(i, end = ' ')
    i += 1
else:
    print('\n' + 'All numbers were printed!')

# Job-2 with for-cycle
for i in range(500):
    if i >= 300:
        print('\n' + 'All numbers were printed!')
        break
    if i % 7 == 0 and i % 14 != 0:
        print(i, end = ' ')

# Job-2 with while-cycle
i = 0
while i != 500:
    if i >= 300:
        print('\n' + 'All numbers were printed!')
        break
    if i % 7 == 0 and i % 14 != 0:
        print(i, end = ' ')
    i += 1

# Matrix
a = [[0 for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        if i == j:
            a[i][j] = i + 1
for i in range(4):
    string = str(a[i]).replace('[', '')
    string = string.replace(']', '')
    print(string)
    print('')

