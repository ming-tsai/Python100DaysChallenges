# string array management
# street_name = "Abbey Road"
# print(street_name[4] + street_name[7])

# Length of string
# print(len("12345"))

# classes of data types
# print(type(123))
# print(type(3.14))
# print(type("Hello"))
# print(type(True))

# type conversion
# print(int("123") + int("456"))
# print(str(123) + str(456))
# print(float("3.14") + float("2.71"))
# print(bool("True") and bool("False")) 

# name_of_user = input("What is your name? ")
# length_of_name = len(name_of_user)
# print("Number of letters in the name " + name_of_user + " is " + str(length_of_name) + " characters.")


# height = 1.65 
# weight = 84

# # Write your code here.
# # Calculate the bmi using weight and height.
# bmi = weight / (height ** 2)

# print(f"Your BMI is: {bmi:.2f}")

# print(6 + 4 / 2 - (1 * 2))

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip_as_percent = tip_percentage / 100
total_tip_amount = total_bill * tip_as_percent
total_bill_with_tip = total_bill + total_tip_amount
bill_per_person = total_bill_with_tip / number_of_people
print(f"Each person should pay: ${bill_per_person:.2f}")





