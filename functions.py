# Functions

# def greet():
#     print("Hello, Welcome !")

# greet()

# def greet(name):
#     print(f"Hello, Welcome {name}")

# greet("Biswajit")
# greet("Ram")


# import test
# test.greet("Biswajit")


# def add(num1,num2):
#     return num1+num2

# print(add(2,3))


# def add(num1,num2):
#     print(num1+num2)
# print(add(2,3))


# def add(num1,num2):
#     print(num1+num2)
#     return num1+num2
# print(add(2,3))




def swap(num1,num2):
    temp = num1
    num1 = num2
    num2 = temp
    print(num1,num2)

# num1 = 5
# num2 = 6
# print(num1,num2)
# print("After Swapping")
# swap(num1,num2)
# temp = num1
# num1 = num2
# num2 = temp
# print(num1,num2)


# num1 = 5
# num2 = 6
# print(num1,num2)
# num1,num2 = num1,num2
# print("After Swapping")
# swap(num1,num2)


# def addition(num1,num2):
#     return num1+num2

# print(addition(2))  # Error


# def addition(num1,num2,num3,num4=1):
#     return num1+num2+num3+num4

# print(addition(2,3,4))

# def addition(*numbers):
#     for number in numbers:
#         print(number, end=",")
    

# addition(1,2,3,4,5,7,8,9,10)


def details(**values):
    print(values)
    
    
details(roll=1,name="Biswajit",age=22)

