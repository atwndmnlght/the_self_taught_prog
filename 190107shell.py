Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = list()
>>> fruit
[]
>>> fruit = []
>>> fruit
[]
>>> fruit = ["Apple","Orange","pear"]
>>> fruit
['Apple', 'Orange', 'pear']
>>> fruit = ["Apple","Orange","Pear"]
>>> fruit.append("Banana")
>>> fruit.append("Peach")
>>> fruit
['Apple', 'Orange', 'Pear', 'Banana', 'Peach']
>>> random[]
SyntaxError: invalid syntax
>>> random = []
>>> random.append(True)
>>> random.append(100)
>>> random.append(1.1)
>>> random.append("Hello")
>>> random
[True, 100, 1.1, 'Hello']
>>> fruit = ["Apple","Orange","Pear"]
>>> fruit[2]
'Pear'
>>> colors = ["blue","green","yellow"]
>>> colors
['blue', 'green', 'yellow']
>>> colors[2] = "red"
>>> colors
['blue', 'green', 'red']
>>> colors = ["blue","green","yell"]
>>> colors
['blue', 'green', 'yell']
>>> item = colors.pop()
>>> item
'yell'
>>> colors
['blue', 'green']
>>> colors.pop()
'green'
>>> colors
['blue']
>>> colors1 = ["blue","green","yellow"]
>>> colors2 = ["orange", "pink", "black"]
>>> colors1 + colors2
['blue', 'green', 'yellow', 'orange', 'pink', 'black']
>>> colors = ["blue","green","yellow"]
>>> "green" in colors
True
>>> "red" in colors
False
>>> "red" not in colors
True
>>> len(colors)
3
>>> 
======= RESTART: /Users/mizunoureshi/Documents/pythone code/190108.py =======
何色でしょう:pink
あたり
>>> my_tuple = tuple()
>>> my_tuple
()
>>> my_tuple = ()
>>> my_tuple
()
>>> rndm = ("M.Jackson", 1958, True)
>>> rndm
('M.Jackson', 1958, True)
>>> dys = ("1084", "Brave New World", "Fahrenheit 451")
>>> dys[2]
'Fahrenheit 451'
>>> "1084" in dys
True
>>> "1984" not in dys
True
>>> 
