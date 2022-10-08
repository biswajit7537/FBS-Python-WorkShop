# import random

# print(random.randrange(10))
# print(random.random())
# print(random.randint(2,10))
# print(random.uniform(2,15))


# var1 = "HELLO WELCOME TO PYTHON"
# var = "Hello welcome to python"
# print(len(var))     it will print the length of the string
# print(var.upper())    # it will convert the string into upper case

# print(var1.lower())     # it will convert the string into lower case

# print(var.title())        # it will convert all the starting letter of a word into upper case


# var = "Python"
# for ch in var:
#     print(ch)s
# print(var[3])
# print(var[0:4])
# print(var[:3])
# print(var[10])  # error

# print(var[-2])

# print(var[1:4:2])



#list in python

# var = [10,20,30,40]
# print(type(var))
# print(var[3])


# lst = [1,2,3,"a","b"]

# lst[2] = "abc"
# print(lst)

# st = "Python"
# st[2] = "z"


# lst = [1]*30
# print(lst)


# st = "Hello" * 10
# print(st)


# lst = ["a","b","c"]

# for x in lst:
#     print(x)

# for index in range(0,3):
#     print(lst[index])


# list1 = ["a","b","c"]
# list2 = [1,2,3,4]
# lst = list1+list2
# print(lst)

# lst = [1,2,["a","b","c"],3,4,[10,20]]

# print(lst[2][1])

# for x in lst:
#     print(x)


# numbers = [1,5,6]

# res = 1
# for number in numbers:
#     res = res*number 

# print(res) 

# numbers = [1,5,6]

# lst = [1,5,7]
# lst.append(15)

# print(lst)


# lst = [10,5,50,3,29,4,2]
# var = lst[0]
# for x in lst:
#     if x > var:
#         var = x

# print(var)

# user input list
# program to calculate maximum element in list
# lst = []

# n = int(input("How many numbers you want to enter ? "))

# for x in range(n):
#     element = int(input(f"Enter the {x+1} element : "))
#     lst.append(element)

# var = lst[0]
# for x in lst:
#     if x > var:
#         var = x

# print(f"The greatest number is {var}")

# var = 15
# print("hello {var}")
# print(f"hello {var}")

lst = [10,5,50,3,29,4,2]
print(max(lst))
