# 1. Exercise - Age 100
#
#     Write a program that asks for and saves a username
#     Ask a question about the user's age, using the username in the question.
#     Shows in how many years the user will be 100 years old smile
#     BONUS: Let the program also show the year when the user will be 100 years old.
#     It could use a variable with the current year.
#     It would be even better to get the current year automatically
#     then you will need two additional lines:
#     import datetime # let's talk about imports separately
#     currentYear = datetime.datetime.now (). year
#
# 2. Exercise - Room volume
#
#     Ask user to input 3 numbers - width, length, height
#     Find the volume of the room
#     PS Think about units and what is the most appropriate data type for this
#
# 3. Exercise - Temperature Conversion
#
#     Write a program that asks user for temperature in Celsius and prints out this same temperature in Farenheit
#     formula is: fahrenheit = 32+celsius*(9/5)
#     PS Remember about data type conversion, also consider precision

def exercise1():
    from datetime import date
    comp_age = 100

    username = input("Input your username: ")
    user_age = input(f"Hello {username} 😀, what is your age? ")
    to_hundred = comp_age - int(user_age)
    year_hundred = date.today().year + to_hundred
    print(f"You will be {comp_age} years old in {to_hundred} years in {year_hundred}", end="\n")


def exercise2():
    precision = 2

    print("This program will calculate room volume.")
    width = input("Input room width: ")
    length = input("Input room length: ")
    height = input("Input room height: ")
    volume = float(width) * float(length) * float(height)
    print(f"Room volume is {round(volume, precision)} cubic units", end="\n")


def exercise3():
    precision = 1

    celsius = input("Input temperature in C: ")
    fahrenheit = 32 + float(celsius) * (9 / 5)
    print(f"Temperature in F is {round(fahrenheit, precision)}")


def main():
    exercise1()
    exercise2()
    exercise3()


if __name__ == "__main__":
    main()
