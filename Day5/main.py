# students_score = [85, 92, 78, 96, 88, 90, 91, 87, 95, 89]

# max_score = 0
# for score in students_score:
#     max_score = max_score > score and max_score or score

# print(f"The highest score in the class is: {max_score}")

# total = 0
# for number in range(1, 101):
#     total += number

# print(total)
# print(sum(range(1, 101)))

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)