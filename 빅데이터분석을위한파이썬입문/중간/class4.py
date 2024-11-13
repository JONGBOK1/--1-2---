Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t=turtle.Turtle()
t.shape('turtle')
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(180)
>>> t.forward(200)
>>> t.left(45)
>>> t.right(45)
>>> x=100
>>> y=100
>>> x,y
(100, 100)
>>> y=200
>>> x,y
(100, 200)
>>> x,y=100+200
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x,y=100+200
TypeError: cannot unpack non-iterable int object
>>> x,y=100,200
>>> result=x+y
>>> result
300
>>> len("hello!!!!!!!!!!!!")
17
>>> w=80
... h=179
... bmi=w/h*h
... 
SyntaxError: multiple statements found while compiling a single statement
>>> w=80
>>> h=179
>>> bmi=w/h*h
>>> bmi
80.0

