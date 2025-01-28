age = int(input("Enter your age: "))
license = bool(input("Have License (True/False): "))


print("You are  in the country: " + str(age >= 18 and license))


# 2
cost = int(input("Enter your Cost: "))
have_vip = bool(input("Enter True/False if you have vip: "))
print("Discount: " + str(cost >= 100 or have_vip))

# 3
temp = int(input("Enter Temperature: "))


print("Heater or AC on: " + str(temp < 15 or temp > 30))

# 4
permission = bool(input("Do you have permission to enter: "))
have_card = bool(input("Do you have card to enter: "))

print("You are in:", str(permission or have_card))