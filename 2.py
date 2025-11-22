a.  Start Python3. (In Windows, click Start > Python3.x > Python3, where x is the release version.)

Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32

Type "help", "copyright", "credits" or "license" for more information.

>>> 

b.  Perform some basic calculations. Enter the calculations at the Python prompt >>>.

>>> 1 + 2

3

>>> 2 * 4

8

>>> 6 / 2

3.0

c.  Print a text string.

>>> “How are you?”

‘How are you?’

d.  Use the type() command to determine the basic data type: integer (int), float, string (str), and Boolean.

>>> type(65)

<class 'int'>

>>> type(45.6)

<class 'float'>

>>> type("Hi!")

<class 'str'>

>>> type(True)

<class 'bool'>

>>> 1<2

True

>>> 1<1

False

>>> 1==1

True

>>> 1>=1

True

e.  Create a variable.

>>> x=3

>>> x*5

15

>>> "Good!"*x

'Good!Good!Good!'

f.   Combine multiple strings together and print as one string.

>>> str1="Cisco"

>>> str2="Networking"

>>> str3="Academy"

>>> space=" "

>>> print(str1+space+str2+space+str3)

Cisco Networking Academy

g.  Convert data type from a numeric number to a string.

>>> x=5

>>> str(x)

‘5’

>>> y=4.2

>>> str(y)

‘4.2’

h.  Note that integers are not rounded up when converting from float. The decimal is ignored.

>>> int(8.21)

8

>>> int(8.99)

8

>>> int(8.21) + int(8.99)

16

i.   Convert an integer to a float.

>>> x=5

>>> x

5

>>> float(x)

5.0

>>> type(x)

<class 'int'>

>>> x=float(x)

>>> type(x)

<class 'float'>

>>> x

5.0

j.   Obtain user input.

>>> name=input("What is your name? ")

What is your name? John

>>> print("Hi " + name + ", it is nice to meet you!")

Hi John, it is nice to meet you!

k.  Use quit() to exit the interactive interpreter.
