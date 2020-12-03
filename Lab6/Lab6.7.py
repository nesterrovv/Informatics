def checkArgs(*args, **kwargs):
    s = 'Превышено количество аргументов'
    if len(args) <= 3 and len(kwargs) < 3:
        return args, kwargs
    else:
        return s
print(checkArgs(1, 2, 3, key1 = 1, key2 = 2))
