# 1. The Big Result
# Write an add_mult function that requires three parameters / arguments
# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.
# PS Assume that numeric parameters will always be passed to the function, no need to check types
# Various solutions are possible (you are allowed to use other data structures inside function such as list).
# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30
#

def add_mult(a, b, c):
    parameters = [a, b, c]
    parameters.sort()
    print(f"equation: ({parameters[0]} + {parameters[1]}) * {parameters[2]}")
    return (parameters[0] + parameters[1]) * parameters[2]


def add_mult_alternative(*parameters):
    """
    Needs 3 parameters to calculate result
    """
    parameters = list(parameters)
    if len(parameters) == 3:
        parameters.sort()
        print(f"equation: ({parameters[0]} + {parameters[1]}) * {parameters[2]}")
        return (parameters[0] + parameters[1]) * parameters[2]
    else:
        print("Incorrect number of parameters! Please specify 3")
        return False


# 2. Palindrome
# Write the function is_palindrome (text) which returns a bool True or False depending on whether the
# word or sentence is read equally from both sides. PS You can start with a one-word solution from the beginning,
# but the full solution will ignore whitespace and uppercase and lowercase letters.

def is_palindrome(word: str):
    word = word.replace(" ", "").lower()
    return word == word[::-1]


# 3. City Population
# The city has a known population p0
# A percentage of population perc is added each year
# Every year a certain number of delta also arrive (or leave)
# We need to know when (if at all) the city will reach a population of p
# Write a function get_city_year (p0, perc, delta, p) that returns the years (full) when p is reached.
# If p cannot be reached, then we return -1
#


def get_city_year(p0, perc, delta, p, years=1):
    predicted_p = p0 + p0 * (perc / 100) + delta
    if p0 > predicted_p: return -1
    if predicted_p >= p:
        return years
    else:
        return get_city_year(predicted_p, perc, delta, p, years + 1)


def main():
    print(add_mult(2, 5, 4))  # -> 30
    print(add_mult_alternative(2, 5, 4))

    print(is_palindrome("Alus ari i ra    sula"))  # ->  True
    # print(is_palindrome("ABa"))  # -> True
    # print(is_palindrome("nava"))  # -> False

    print(get_city_year(1000, 2, 50, 1200))  # -> 3
    # print(get_city_year(1000, 2, -50, 5000))  # -> -1
    # print(get_city_year(1500, 5, 100, 5000))  # -> 15
    # print(get_city_year(1500000, 2.5, 10000, 2000000))  # -> 10


if __name__ == "__main__":
    main()
