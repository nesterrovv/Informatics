'''
Создайте функции
encodeHuffman(fileIn, fileOut) и decodeHuffman(fileIn,
fileOut), осуществляющие кодирование и декодирование текста с
использованием метода Хаффмана соответственно. fileIn – полное имя
файла с исходным текстом, fileOut – полное имя файла, куда
необходимо записать результат. Функции возвращают True, если ошибок
не возникло, и False в ином случае.
'''
# for priority queue
import heapq
# Counter: to calculate the symbol frequency
# namedtuple: for compact class declaration
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left", "right"])):
	'''
	 the second argument is the prefix of the code that we
	 have accumulated, going down from the root to the node
	'''
	def walk(self, code, acc):
		self.left.walk(code, acc +'0')
		self.right.walk(code, acc +'1')


class Leaf(namedtuple("Leaf", ["char"])):
	def walk(self, code, acc):
		# "or '0'" necessary for correct work with single-valued strings
		code[self.char] = acc or '0'

def huffman_encode(fileInputPath, fileOutputPath):

	fileInput = open(fileInputPath, 'r')
	s = fileInput.read()
	fileInput.close()

	'''
	 the queue is presented as a list.
	 the second component is unique. added because when element
	 returned to the priority queue, no comparison happened
     between the third components (an error occurs when comparing Node and Leaf)
    '''
	h=[]
	for ch, freq in Counter(s).items():
		h.append((freq, len(h), Leaf(ch)))
	# creating a priority queue 
	heapq.heapify(h)

	count = len(h)
	while len(h) > 1:
		# getting two elements with the minimum frequency
		freq1, _count1, left = heapq.heappop(h)
		freq2, _count2, right = heapq.heappop(h)
		# add a new item to the queue
		heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
		count += 1

	global code
	code = {}
	# this branch is necessary to work correctly with empty lines
	if h:
		# there is only one element left - the root of the tree
		[(_freq, _count, root)] = h
		# tree traversal and filling dictionary "code"
		root.walk(code, "")

	encoded = "".join(code[ch] for ch in s)

	fileOutput = open(fileOutputPath, 'w')
	fileOutput.write(encoded)
	fileOutput.close()


def huffman_decode(fileInputPath, fileOutputPath):

	fileInput = open(fileInputPath, 'r')
	encodedStr = fileInput.read()
	fileInput.close()

	pointer = 0
	decodedStr = ''
	while pointer < len(encodedStr):
		for ch in code.keys():
			if encodedStr.startswith(code[ch], pointer):
				decodedStr += ch
				pointer += len(code[ch])

	fileOutput = open(fileOutputPath, 'a')
	fileOutput.write('\n' + decodedStr)
	fileOutput.close()

def main():
    try:
        fileInputPath = input('Введите имя исходного файла (с раширением): ')
        fileOutputPath = input('Введите имя файла для записи (с раширением): ')
        huffman_encode(fileInputPath, fileOutputPath)
        huffman_decode(fileOutputPath, fileOutputPath)
        print('True')
    except:
        print('False')
    finally:
        print('Программа завершила работу')

if __name__ == "__main__":
	main()