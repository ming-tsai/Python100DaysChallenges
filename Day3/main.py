# This is the code for Day 3 of the 100 Days of Code Challenge.
# Validate the number is even or odd.
# number_to_check = int(input("Which number do you want to check? "))
# if number_to_check % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# height = float(input("Enter your height in cm: "))
# bill = 0
# if height >= 120:
#     age = int(input("Enter your age: "))
#     if not age >= 45 and not age <= 55:
#         if age < 12:
#             bill += 5
#         elif age < 18:
#             bill += 7
#         else:
#             bill += 12
        
#         wants_photo = input("Do you want a photo taken? Y or N ")
#         if wants_photo == "Y":
#             bill += 3
    
#     print(f"Your final bill is ${bill}.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# # 🚨 Do not modify the values above
# # Write your code below 👇
# if bmi < 18.5:
#     print("underweight")
# elif bmi < 25:
#     print("normal weight")
# else:
#     print("overweight")

# print("Welcome to Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: +$1

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")
