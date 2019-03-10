Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> myd_dict = dict()
>>> my_dict
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    my_dict
NameError: name 'my_dict' is not defined
>>> myd_dict
{}
>>> my_dict = {}
>>> my_dict
{}
>>> fruits = {"
	      
SyntaxError: EOL while scanning string literal
>>> fruits= {"Apple": "Red", "Banana":"Yellow"}
	      
>>> fruits
	      
{'Apple': 'Red', 'Banana': 'Yellow'}
>>> 
======= RESTART: /Users/mizunoureshi/Documents/pythone code/190109.py =======
{}
>>> 
======= RESTART: /Users/mizunoureshi/Documents/pythone code/190109.py =======
{}
Traceback (most recent call last):
  File "/Users/mizunoureshi/Documents/pythone code/190109.py", line 4, in <module>
    facts["code"] = "fun"
NameError: name 'facts' is not defined
>>> 
======= RESTART: /Users/mizunoureshi/Documents/pythone code/190109.py =======
{}
>>> 
======= RESTART: /Users/mizunoureshi/Documents/pythone code/190109.py =======
{}
fun
>>> bill = {"Bill Gates": "charitable"}
	      
>>> "Bill Gates" in bill
	      
True
>>> books = {"Dracula":"Stoker", "1984": "orwell"}
	      
>>> del books["Dracula"]
	      
>>> books
	      
{'1984': 'orwell'}
>>> 
