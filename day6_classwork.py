# 1a. Average value
# Write a program that prompts the user to enter numbers (float).
# The program shows the average value of all entered numbers after each entry.
# PS. 1a can do without a list

def average_value_1a():
    i = 0
    total = 0

    while True:
        user_input = input("Input a number or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        else:
            i += 1
            total += float(user_input)
            print(f"Average is {total / i:.2f}")


# 1b. The program shows both the average value of the numbers and ALL the numbers entered
# PS Exit the program  by entering "q"

def average_value_1b():
    list_numbers = []

    while True:
        user_input = input("Input a number or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        else:
            list_numbers.append(float(user_input))
            print(f"All numbers: {list_numbers}\nAverage is {sum(list_numbers) / len(list_numbers):.2f}")


# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.

def average_value_1c():
    list_numbers = []
    top = 3

    while True:
        user_input = input("Input a number or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        else:
            list_numbers.append(float(user_input))
            print(f"Numbers: {sorted(list_numbers)[:top]} ... {sorted(list_numbers)[-top:]}\nAverage is {sum(list_numbers) / len(list_numbers):.2f}")


# 2. Cubes
# The user enters the beginning (integer) and end number.
# The output is the entered numbers and their cubes
# For example: inputs 2 and 5 (two inputs)
#
# Output
# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125
# All cubes: [8,27,64,125]
#
# PS could theoretically do without a list, but with a list it will be more convenient
#

def cubes():
    starting_number = int(input("Input starting number: "))
    last_number = int(input("Input last number: "))

    direction = -1 if starting_number > last_number else 1
    list_numbers = list(range(starting_number, last_number + direction, direction))
    list_cubes = []
    for i, val in enumerate(list_numbers):
        list_cubes.append(val ** 3)
        print(f"{val} cubed: {list_cubes[i]}")
    print(f"All cubes: {list_cubes}")


# 3. Reversed words
# The user enters a sentence.
# We output all the words of the sentence in reverse form. - not the whole text reversed!!
#
# Example
# Alus kauss mans -> Sula ssuak snam
#
# PS Split and join operations could be useful here.
#
def reversed_words():
    sentence = input("Input the sentence: ")
    words = sentence.split()
    reversed_word_list = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_word_list).capitalize()
    print(f"{sentence} -> {reversed_sentence}")


# 4. Prime numbers -
# this could be a weekend assignment, there is hardly enough time in class
#
# Find and output the first 20 (even better option to choose how many first primes we want) prime numbers in the form
# of a list i.e. [2,3,5,7,11, ...]

def primes():
    prime_list = []
    max_num = int(input("Enter how many primes should be listed: "))
    current_number = 1

    while len(prime_list) < max_num:
        current_number += 1
        for i in range(2, current_number):  # reused code from lesson 4
            if (current_number % i) == 0:
                break
        else:
            prime_list.append(current_number)
    print(f"Primes: {prime_list}")


def main():
    average_value_1a()
    average_value_1b()
    average_value_1c()
    cubes()
    reversed_words()
    primes()


if __name__ == "__main__":
    main()
