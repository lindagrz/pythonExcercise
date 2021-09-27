# 1. Health check
# Ask user for their temperature.
# If the user enters below 35, then output "not too cold"
# If 35 to 37 (inclusive), output "all right"
# If the temperature  over 37, then output  "possible fever"

# 2. Xmas Bonus The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year
# of service over 2 years. Task. Ask the user for the amount of the monthly salary and the number of years worked.
# Calculate the bonus. Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro. Example2: 1.5
# years of experience, 1500 Euro salary, no bonus(0).

# 3. Ordered output.
# Ask the user to enter 3 numbers, output them in ascending order.
# Note: for now, we solve this task only with if, elif, else actions.
# There is also a solution using sorting and list structure, which we have not yet seen.

def health_check():
    precision = 1
    temp = round(float(input("What is the temperature? ")), precision)
    print("not too cold") if temp < 35 else print("possible fever") if temp > 37 else print("all right")


def xmas_bonus():
    precision = 2
    bonus = 0.15
    service_min = 2

    salary = round(float(input("What is your monthly salary? ")), precision)
    years_worked = round(float(input("For how many years have you worked in the company? ")), precision)

    if years_worked > service_min:
        bonus_amnt = salary * bonus * (years_worked - service_min)
        print(f"Your bonus is {bonus_amnt} \nMerry Christmas!")
    else:
        print("Sorry, no Xmas bonus")


def ordered_output():
    n1 = int(input("Input first number: "))
    n2 = int(input("Input second number: "))
    n3 = int(input("Input third number: "))

    if n1 > n2:
        n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n2 > n3:
        n2, n3 = n3, n2

    print("Result: ")
    print(n1, n2, n3, sep=" <= ")


def main():
    health_check()
    xmas_bonus()
    ordered_output()


if __name__ == "__main__":
    main()
