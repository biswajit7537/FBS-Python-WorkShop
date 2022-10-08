print("---------- Welcome To Tip Calculator !! ----------\n\n")

bill = float(input("What is your total bill amount ? "))
tip = int(input("How many percentage of tip you want to give ? "))
people = int(input("How many number of people you want to split the bill ? "))

tip_amount = bill * (tip/100)
total_bill = bill+tip_amount
each_amount = round(total_bill/people,2)

print(f"Each person should pay ₹{each_amount}")
print("\n\nThank you")

#round()

# escape charaters
# f-string (Formated String)


age = 15
mark = 95
class1 = 9

# print(f"My age is {age} and my mark is {mark} and I read in class {class1}")