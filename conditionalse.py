# Conditional statements
# if , if else, elif
# indentation 

# num1 = 2
# num2 = 10

# if num1>num2:
#     print("num1 is greater than num2")
#     var = "Python"
#     print(var)

# print("Program is finished")

# if else

# num1 = 2
# num2 = 10

# if num1>num2:
#     print("num1 is greater than num2")
# else:
#     print("You are in else part")

# print("Bye")

# elif

# num1 = 10
# num2 = 10

# if num1>num2:
#     print("num1 is greater than num2")
# elif num1==num2:
#     print("numbers are equal")
# else:
#     print("You are in else part")


# print("Bye")


# odd and even
# %

# num = int(input("Enter a number : "))

# if num%2 == 0:
#     print("Even")
# else:
#     print("Odd")


# var = 11

# if var == 10:
#     print("number is 10")

#     if var < 15:
#         print("It is less than 15")
#         if var > 5:
#             print("It is greater than 5")

# print("Bye")




# Loops
# While loop, for loop

# var = 1
# while var <=10 :
#     print("Hello, Welcome", var)
#     var += 1


# print only even numbers between 1 to 20

# pass keyword

# counter = 1

# while counter<=20:
#     if counter%2 == 0:
#         pass
#     else:
#         print(counter)
    
#     counter += 1


# var = 20

# while var > 30:
#     print(var)
#     var +=2

# else:
#     print("Inside else part")


# for loop

# for num in range(0,10,3):
#     print(num)


# print all the numbers which are divisible by 3 between 1 to 30 


# for num in range(1, 31):
#     if num%3 == 0:
#         print(num)


# List unpacking
# lst = ["a","b","c",1,2,3]

# var1 = lst[0]
# var2 = lst[1]
# var3 = lst[2]

# var1, var2, var3, *others = lst

# print(var1,var2,var3, sep=", ")
# print(others)

# lst = ["a","b","c",1,2,3]

# print(lst[1:4])
# print(lst[1:6:2])
# print(lst[-1])

# some buildin list functions

# lst = ["a","b","c"]
# # lst.append("d")
# lst.insert(1,"xyz")
# print(lst)


# lst1 = ["a","b","c"]
# lst2 = [1,2,3,4]

# lst1.extend(lst2)
# print(lst1)


# lst = [1,2,3,4]
# print(sum(lst))


# lst = [1,2,3,4,1,5,1,8,1]
# print(lst.count(1))
# print(lst.count(4))


# lst = [2,3,4,1,5,1,8,1]
# print(lst.index(4))
# print(lst.index(1))

# lst = [2,3,4,1,5,1,8,1]
# lst.pop()
# print(lst.pop(0))
# print(lst)

# lst = [2,3,4,1,5,1,8,1]
# del lst[2]
# print(lst)

# lst = [2,3,4,1,5,1,8,1]
# lst.remove(8)
# print(lst)

# lst = [2,3,4,1,5,1,8,1]
# print(min(lst))


#eval()

# var = eval(input("Enter a List : "))
# print(type(var))
# print(var)

# name = "Python"
# lst = list(name)
# print(lst)

# Q. print the elements of the list which are present in the even position.

st = "abcdefghijklmnopqrstuvwxyz"
lst = list(st)

for i in range(len(lst)):
    if i%2 == 0:
        print(lst[i])

