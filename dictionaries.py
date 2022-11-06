# dict1 = {1:"Ram",2:"Shyam",3:"abc"}
# print(dict1[2])
# print(dict1)
# print(type(dict1))

# dict1 = {1:"Ram",2:"Shyam",3:"abc",4:[10,20,30,40]}
# print(dict1[4][1])


# lst = [(1,"a"),(2,"b"),(3,"c")]
# d = dict(lst)
# print(d)

# d = {1:"a",2:"b",3:"c",4:"d"}
# d[2] = "xyz"
# print(d.get(4))
# print(d.keys())

# user input
# d = {}
# size = int(input("Enter the size : "))

# for i in range(size):
#     key = eval(input("Enter key : "))
#     val = eval(input("Enter value : "))
#     d[key] = val

# print(d)

d = {1:"One",2:"Two",3:"Three"}
for key,value in d.items():
    print(f"your key is {key} and value is {value}")

# for value in d.values():
#     print()



