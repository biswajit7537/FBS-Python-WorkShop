# set
# st = {1,2,3,4}
# print(type(st))

# st = {1,2,"a","b",5.6}
# print(st[0])  

# st = {1,2,3,1,2,4,5,3}
# print(st)

# adding elements
# st = {1,2,3}
# st.add(10)
# print(st)

# union

# st1 = {1,2,3}
# st2 = {"a","b","c"}
# st = st1.union(st2)
# print(st)

# stt = st1 | st2
# print(stt)

# Intersection

# st1 = {1,2,3,4,5}
# st2 = {4,5,"a","b","c"}
# st = st1.intersection(st2)
# print(st)

# stt = st1 & st2  # st1 intersection set2
# print(stt)

# Difference

# st1 = {1,2,3,4,5}
# st2 = {4,5,"a","b","c"}

# print(st1-st2)
# print(st2-st1)

# user input
# st = eval(input("Enter the set : "))
# print(st)

# input
# st = set()
# print(type(st))
# size = int(input("Enter the size of the set : "))

# for i in range(size):
#     ele = int(input("Enter value : "))
#     st.add(ele)
# print(st)


# st1 = {1,2,3,4,5,6}
# st2 = {1,2,3,4,5,6}
# print(st1 <= st2)
# print(st1 == st2)

# removing duplicate elements from a List
lst = [1,2,1,3,4,5,1,3,2,10]
st = set(lst)
lst = list(st)
print(lst)