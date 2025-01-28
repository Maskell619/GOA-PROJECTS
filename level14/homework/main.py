number1 = int(input("Enter any number 5-15, The number should not be equal to 10: "))

print("Is between 5-15: " + str(number1 > 5 and number1 < 15) + ", Is Ten: " + str(number1==10))

# 2
age = int(input("Enter your age: "))
print("Age is more than 18: " + str(age>18))
name = input("Enter your name: ")
print('Your name starts with "A": ', str(name.startswith("A")))