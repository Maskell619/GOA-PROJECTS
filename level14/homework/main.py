number1 = int(input("Enter any number 5-15, The number should not be equal to 10: "))

print("Is between 5-15: " + str(number1 > 5 and number1 < 15) + ", Is Ten: " + str(number1==10))

# 2
age = int(input("Enter your age: "))
print("Age is more than 18: " + str(age>18))
name = input("Enter your name: ")
print('Your name starts with "A": ', str(name.startswith("A")))

# 3
number = int(input("Enter any number: "))

print("Is even: " + number%2==0)
print("Can be devided by three:" + number%3==0)

integer1 = 178
integer2 = 90

print(str(integer1), " is more than 100 or equals to 100: " + str(integer1 >= 100))
print(str(integer2), " is more than 100 or equals to 100: " + str(integer2 >= 100))