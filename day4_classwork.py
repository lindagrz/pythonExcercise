# 1. FizzBuzz
# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz
# So if number divided by 5 then Fizz If divided by 7 then Buzz, If divided by 5 AND 7 then FizzBuzz otherwise the
# same number
#  Note: such a task became popular as the first task to ask to determine whether a person knows about programming
# at all smile
#
#  2. Christmas tree
# Enter the height of the tree
# Print the tree: Ex. height == 3
# The printout would be:
#   *
#  ***
# *****
# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)
#
# 3. Primes Check if entered positive number is a prime number.
#  A prime number is a number that divides without remainder only by itself and 1.
# Hint: what numbers do we have to check?


def fizzbuzz():
    fizz = 5
    buzz = 7
    end_num = 100
    end_str = ", "

    for i in range(1, end_num + 1):
        if i == end_num:
            end_str = ""
        if i % (fizz * buzz) == 0:
            print("FizzBuzz", end=end_str)
        elif i % buzz == 0:
            print("Buzz", end=end_str)
        elif i % fizz == 0:
            print("Fizz", end=end_str)
        else:
            print(i, end=end_str)


def christmas_tree():
    height = int(input("Enter the height of the tree: "))
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))


def primes():
    num_to_test = int(input("Enter a number: "))
    if num_to_test > 1:  # 1 is not a prime + is it positive?
        for i in range(2, num_to_test):  # test all numbers in range up to the input
            if (num_to_test % i) == 0:
                print(f"{num_to_test} is not a prime number")
                break
        else:  # from for
            print(f"{num_to_test} is a prime number")
    else:
        print(f"{num_to_test} is not a prime number")


def main():
    # fizzbuzz()
    # christmas_tree()
    primes()


if __name__ == "__main__":
    main()
