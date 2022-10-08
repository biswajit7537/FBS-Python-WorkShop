#boolean datatype
# True, False


# Arithmetic operators
# +, -, *, /, //, **, %

# var1 = 10
# var2 = 5
# print(var1+var2)
# print(var1-var2)
# print(var1*var2)
# print(var1/var2)
# print(var1**var2)  # var1 to the power var2
# print(var1//var2)  # floor division
# print(var1%var2)   


# Comparison operators

# var1 =10
# var2 = 15

# print(var1>var2)
# print(var1>=var2)
# print(var1<var2)
# print(var1<=var2)
# print(var1==var2)
# print(var1 != var2)

#Logical Operators
# and , or, not

# var = True and True
# var = False and True 
# var = False and False

# var = True or True
# var = False or True
# var = False or False
# print(var)

# var = (2>1) and (5>3) and (10<4)
# print(var)

# var = not True
# var = not (5>3)
# print(var)

# identity Operators
# is , is not

# name = 10
# var = 10
# print(var is name )

# name = 10
# var = 14
# print(var is not name )

# Membership Operator

# in, not in

# var = "Hello Welcome"

# print("abc" in var)

# var = "Hello Welcome"

# print("W" not in var)

# Bitwise Operators
# &, |, ^, ~, << , >>

# print(9&7)
# print(9|7)
# print(9^7)

# print(~-7)

# print(14<<2)  # (x<<y) = x*(2**y)
# print(14>>3)  # (x>>y) = x/(2**y)

# Assignment Operators
# =, +=, -=, *=, **=,/=, //= , &=, ~= , ^= ,.. ect.
var = 5
var = var + 3

var += 3  # var = var+3
var *= 2  # var = var*2
var //=3  # var = var//3


# Variable naming rules

# 2var = 10    This is not allowed

# my name = "Biswajit"   This is not allowed

# my%name = "abc"   this is not allowed

_myname = "abc"  # valid

name = "abc"     #valid
Name = "def"     #valid


# type casting

# num = 134
# var = str(num)
# print(type(var))

# var = "456"
# num = int(var)
# print(type(num))

# var = "456"
# print(type(var))
# num = float(var)
# print(type(num))


# var = "hello welcome"
#len()

# print(len(var))

# print(len(1354))


# user input in python
#input()

# name = input("Enter a number : ")

# String Concatination
# var = "Hello"
# num = "Welcome"


# print("Hello"+" "+"Welcome")

# name = input("Enter your age : ")

# print("Your age is "+name)

# num1 = input("Enter first number : ")
# num2 = input("Enter second number : ")
# new_num1 = int(num1)
# new_num2 = int(num2)
# # print(type(new_num1), type(new_num2))
# # print("Addition of two number is "+str(new_num1+new_num2))
# print("Addition of two number is ",(new_num1+new_num2))

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("Addition of two number is ",(num1+num2))










