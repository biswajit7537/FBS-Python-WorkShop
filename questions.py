# lst = []
# strr = input("Enter a String : ")
# for ch in strr:
#     lst.append(ch)
# print(lst)


# num1 = int(input("Enter 1st number : "))
# num2 = int(input("Enter 2nd number : "))
# div = num1/num2
# print(f"Division of two number {div}")

# Compile time Error
# Logical Error
# Run time Error

# for i in range(5):
#     print(i)

#addition
#multiplication


# num1 = int(input("Enter 1st number : "))
# num2 = int(input("Enter 2nd number : "))
# try:
#     div = num1/num2
#     print(f"Division of two number {div}")
# except:
#     print("Number 2 can not be Zero")


lst1 = [1,2,3,4]
lst2 = [3,4,5,6]

lst = [3,4] #output

lst1 = [1,2,3,4]
lst2 = [3,4,5,6,7]

set1 = set(lst1)
set2 = set(lst2)
set3 = set1.intersection(set2)
lst3 = list(set3)
print("The Common Elements are ")
for element in lst3:
    print(element)