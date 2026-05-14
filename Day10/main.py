# def format_name(first_name, last_name):
#     return f"{first_name} {last_name}".title()

# f_name = input("What is your first name? ")
# l_name = input("What is your last name? ")

# print(format_name(f_name, l_name))

def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(is_leap_year(2000))
print(is_leap_year(2020))