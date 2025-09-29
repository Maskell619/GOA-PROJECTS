# 1
sentance = input("Enter sentance: ")
sentance = sentance.lower()
if "python" in sentance:
    print("Python is in the sentance")
else:
    print("Python is not in the sentace")

# 2
word = input("Enter something: ")

if word.startswith("c"):
    print('The word starts with letter "c"')

# 3
filename = input("Enter file name: ")

if ".png" in filename:
    print("The externsion is .png") 

# 4
numbers = list(input("Enter list of numbers: "))
numbers_copy = numbers.copy()

for n in numbers:
    if n == ",":
        numbers_copy.remove(',')

    
for n in numbers_copy:
    print(n)