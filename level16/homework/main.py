bool1 = True
bool2 = False

print("At least one variable is true: " + str(bool1 or bool2))
print("Both variables are True: " + str(bool1 and bool2))

num1 = 5
num2 = 6

print("First number is equal or greater than the second number: " + str(num1 >= num2))

age = int(input("Enter you age: "))

print("Your age is between 6-12: " + str(age >= 6 and age <= 12))

print("opposite of " + str(bool1) + " is: " + str(bool(bool1) and bool2))
print("opposite of " + str(bool2) + " is: " + str(bool(bool2) or bool1))