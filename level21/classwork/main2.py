num = 1

while num < 6:
    print(num)
    num += 1

num = 1
summary = 0

while num < 11:
    summary += num
    num += 1

print(summary)

num2 = 1

number = int(input("ჩაწერე რიცხვი: "))

while num2 < (number + 1):
    print(num2)
    num2 += 1


password = "1234"

number = input("Enter password: ")

if number != password:
    print("Try again")

while password != number:
    number = input("Enter password: ")

    if number != password:
        print("Try again")
    
print("Correct password")

cor_number = 7

guess = int(input("Enter correct number: "))

if guess != cor_number:
    print("Try again")

while cor_number != guess:

    guess = int(input("Enter correct number: "))

    if guess != cor_number:
        print("Try again")

    
print("Correct")