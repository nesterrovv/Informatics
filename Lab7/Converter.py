import sys
import xml.etree.ElementTree as ET # Для расчета времени парсинга
import time # Для работы со временем

# converting xml tegs for objects and word with it into the future
def tagTextToObject(text: str):
    args = text.split()
    name = args[0]
    dic = dict()
    for arg in args[1:]:
        pair = arg.split("=")
        dic[pair[0]] = pair[1]
    dic.update({"name":name,"childs":[]})
    return dic

def converter(inFileName, outFileName):
    # read text
    file = open(inFileName, "r") # <------------------------------------- HERE TO READ
    text = file.read()
    file.close()
    # START CONVERTING
    root = {"name":"root","childs":[]}
    stack = []
    stack.append(root["childs"])
    start = 0
    finish = 0
    level = 0
    while True:
        # to find <
        p = text.find("<", start)
        if p == -1:
            # если что-то пошло не так
            if level == 0:
                finish = len(text)
                textToStack = text[start:finish]
                textToStack = textToStack.replace("\n","")
                if (len(textToStack) > 0) & (not textToStack.isspace()):
                    stack[-1].append()
                break
            else:
                # если структура оказалась корявой, выкинуть ошибку 
                raise Exception("Structure is not correct (level not ended)")
        else:
            finish = p
            textToStack = text[start:finish]
            textToStack = textToStack.replace("\n","")
            if (len(textToStack) > 0) & (not textToStack.isspace()):
                stack[-1].append(textToStack)
            # найти закрывающую скобку, чтобы определиться с содержимым внутри <>
            p2 = text.find(">", finish+1)
            if p2 == -1:
                raise Exception("Structure is not correct (no pair <>)")
            bracketsText = text[finish+1:p2]
            # определить тип скобок, а то вдруг там комментарий
            l = len(bracketsText)
            if (l >= 5) & (bracketsText[0:3] == "!--") & (bracketsText[-2:] == "--"):
                # тогда комментарий, внести его особым образом
                obj = {"name":"!comment","childs":[bracketsText[3:-2]]}
                stack[-1].append(obj)
            elif (l >= 1) & (bracketsText[-1] == "/"):
                # это независимый тэг и нужно
                # определить что вложено
                pass
                # добавить в создаваемую древовидную структуру
                stack[-1].append(tagTextToObject(bracketsText[:-1]))
            elif (l >= 1) & (bracketsText[0] == "/"):
                # это закрывающий тег, его в YAML не надо переносить
                level-= 1
                stack.pop()
            else:
                # работа с открывающим тегом
                level+= 1
                obj = tagTextToObject(bracketsText)
                stack[-1].append(obj)
                stack.append(obj["childs"])

            finish = p2+1
        start = finish
    
    # начало записи всего нужного в YAML и создание каркаса 
    stack = []
    stack.append([root["childs"],0]) # [list - iterator]
    level = 1
    SPACES_PER_LEVEL = 1
    text = "---\n"
    while True:
        # чтение итератора
        it = stack[-1][1]
        # проверка из списка
        if it == len(stack[-1][0]):
            # если все хорошо
            if level == 1:
                break
            # опуститься на уровень ниже и забыть индекс
            level-= 2
            stack.pop()
            stack[-1][1]+= 1
            continue
        # наконец, чтение элемента
        el = stack[-1][0][it]
        # определение типа элемента
        if (type(el) is dict):
            if (el["name"]=="!comment"):
                # это просто комменатрий - вывести его
                text += " "*SPACES_PER_LEVEL*level + "#" + el["childs"][0] + "\n"
            else:
                # это объект - вывести и его тоже
                text += " "*(SPACES_PER_LEVEL*level-2) + "- " + el["name"] + ":\n"
                # печатаем аргументы, надо для структуры YAML
                level+= 1
                for arg in el.keys():
                    if (arg == "name") | (arg == "childs"):
                        continue
                    text += " "*SPACES_PER_LEVEL*level + arg + ": " + el[arg] + "\n"
                # печатаем вложенности и поднимаемся на уровень выше
                if (len(el["childs"]) > 0):
                    text += " "*SPACES_PER_LEVEL*level + "childs:\n"
                level+= 1
                # добавляем новый список в стак
                stack.append([el["childs"], 0])
                continue
        else:
            # напечатать просто текст
            text += " "*SPACES_PER_LEVEL*level + "\"" + el + "\"\n"
        # увеличить итератор и повторить все эти действия
        stack[-1][1] += 1
    
    file = open(outFileName, "w") # открыть xml
    file.write(text) # считать
    file.close() # закрыть


# ЧУЖОЙ ВАРИАНТ ПРОГРАММЫ. ЗАПУСТИТЬ И ПРОВЕРИТЬ КАК РАБОТАЕТ

XML_NODE_CONTENT = '_xml_node_content'
ATTR_COMMENT = '# Attribute'
def coderoad_converter(node, output, depth=0):
    if not depth:
        ofile.write('---\n')
    # Nodes with both content AND nested nodes or attributes
    # have no valid yaml mapping. Add  'content' node for that case
    nodeattrs = node.attrib
    children = list(node)
    content = node.text.strip() if node.text else ''
    if content:
        if not (nodeattrs or children):
            # Write as just a name value, nothing else nested
            ofile.write(
                '{indent}{tag}: {text}\n'.format(
                    indent=depth*'  ', tag=node.tag, text=content or ''))
            return
        else:
            nodeattrs[XML_NODE_CONTENT] = node.text

    ofile.write('{indent}{tag}:\n'.format(
        indent=depth*'  ', tag=node.tag))

    # Indicate difference node attributes and nested nodes
    depth += 1
    for n,v in nodeattrs.items():
        ofile.write(
            '{indent}{n}: {v} {c}\n'.format(
                indent=depth*'  ', n=n, v=v,
                c=ATTR_COMMENT if n!=XML_NODE_CONTENT else ''))
    # Write nested nodes
    for child in children:
        coderoad_converter(child, output, depth)


inFileName = "xml_timetable.xml" # тут исходный XML
outFileName1 = "my_timetable.yaml" # тут будет YAML на выходе
outFileName2 = "coderoad_timetable.yaml" # тут будет чужой YAML на выходе

TESTS_LENGTH = 1000 # проанализировать скорость исполнения, 1000-кратную (По заданию)

print("Test 1. My program")
start_time = time.time()
for i in range(TESTS_LENGTH):
    converter(inFileName, outFileName1)
delay = time.time() - start_time # посчитать время
print("%d cycles passed in %f s - %f s/operation" % (TESTS_LENGTH, delay, delay/TESTS_LENGTH)) # вывести с форматированием


print("Test 2. Not my program")
start_time = time.time()
for i in range(TESTS_LENGTH):
    with open(inFileName) as xmlf:
        tree = ET.parse(xmlf)
        ofile = open(outFileName2, "w")
        coderoad_converter(tree.getroot(), ofile)
        ofile.close()
delay = time.time() - start_time # посчитать время
print("%d cycles passed in %f s - %f s/operation" % (TESTS_LENGTH, delay, delay/TESTS_LENGTH)) # вывести с форматированием



'''
Для обозначения тегов я использую отдельный параметр объекта в yaml-разметке, чужой же код
помещает все на один уровень. Разница в коде. В моем решении значения выделяются в кавычки, в чужом - нет.
Кроме того, разная работа с комментариями. В моем они переносятся. А в чужом решении нет, там делаются новые
для обозначения атрибутов. Все это порождает отраженную в выводе разницу в коде.
'''