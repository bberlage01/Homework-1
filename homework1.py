Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Problem 1
type("Rosewater")
<class 'str'>
type("0.001")
<class 'str'>
type(37)
<class 'int'>
type(False)
<class 'bool'>
#Problem 2
#the + operator in a print statement will add the strings together like so:
print("Good"+"Morning")
GoodMorning
first="Hello"
second="World"
print(first+second)
HelloWorld
#the , operator keeps the two strings separate
print("Hi","friend")
Hi friend
first="Hi"
second="Friend"
print(first,second)
Hi Friend
#Problem 3
#the following are built in functions used to convert data types
int(2.4)
2
float(3)
3.0
str(86)
'86'
bool(1)
True
#int function converts its argument to an integer
#float function converts its argument to a float number
#str function converts its argument to a string
#bool function converts its argument to true or false
#Problem 4
#you can display the sentences of a paragraph containing at least five lines using only one print statement by using \n
print("Put a price on emotion\nLooking for something to buy\nYou\'ve got my devotion\nBut man I can hate you sometimes\nI don\'t want to fight you")
Put a price on emotion
Looking for something to buy
You've got my devotion
But man I can hate you sometimes
I don't want to fight you
I don't want to fight you
SyntaxError: unterminated string literal (detected at line 1)
#Problem 5
flour=2
milk=1
egg=4
oil=.4
vanilla=.012
cake=2*flour+0.5*(milk-egg+vanilla)+oil**2
print(cake)
2.6660000000000004
