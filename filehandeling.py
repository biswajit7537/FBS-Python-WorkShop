#read
# file = open("myfile.txt","r")
# print(file.read())

#Write 

# file = open("myfile.txt","w")
# file.write("Heloo, Python")
# file.close()


try:
    file = open("data.txt","r")
    print("Hello, Welcome",file.read())
except:
    file = open("data.txt","w")
    name = input("Enter Your Name : ")
    file.write(name)

print("Thank You !!")