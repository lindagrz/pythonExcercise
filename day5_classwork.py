# 1. Confusion T
# he user enters a name. You print user name in reverse (should begin with capital letter) then extra
# text: ",a thorough mess is it not ", then the first name of the user name then "?" Example: Enter: Valdis ->
# Output: Sidlav, a thorough mess is it not V?
#
#
# 2. Almost Hangman
# Write a program to recognize a text symbol The user (first player) enters the text. Only
# asterisks instead of letters are output. Assume that there are no numbers, but there may be spaces. The user (i.e.
# the other player) enters the symbol. If the letter is found, then the letter is displayed in ALL the appropriate
# places, all other letters remain asterisks.
# Example: First input: Kartupeļu lauks -> ********* ***** Second input:
# a -> *a****** *a***
#
# In principle, this is a good start to the game of hangman.
# https://en.wikipedia.org/wiki/Hangman_(game)
#
#
# 3. Text conversion
# Write a program for text conversion Save user input Print the entered text without changes
# Exception: if the words in the input are not .... bad, then the output is not ...  bad section must be changed to
# is good


def confusion():
    name = input("Enter a name: ")
    print(name[::-1].title())


def almost_hangman():
    word = input("First player, enter the text: ")
    # word = "Kartupeļu lauks"

    guessed = "*" * len(word)
    letter = " "  # to add back the spaces before starting

    while not letter == "0":
        for i, c in enumerate(word):
            if c.lower() in letter.lower():  # guesses are not case sensitive
                guessed = guessed[:i] + c + guessed[i + 1:]

        if guessed.find("*") == -1:
            print("Good job!")
            break

        print(guessed)
        letter = input("Player 2: Guess a letter (or input 0 to give up): ")

    print(f"The answer was: {word}")


def text_conversion():
    text = input("Input text: ")
    # text = "The weather is not bad"
    # text = "The car is not new"
    # text = "This cottage cheese is not so bad"
    # text = "That was pretty bad, was in not my friend?"
    # text = "This sport is not badminton!"

    start = "not"
    tail = "bad"
    alternative = "good"

    # # for the Latvian language variation
    # text = "Laikapstākļi nav slikti"
    # text = "Mašīna nav jauna"
    # text = "Kartupeļu biezenis nav nemaz tik slikts"
    # start = "nav"
    # tail = "slikt"
    # alternative = "ir lab"

    if text.find(start) != -1 and text.find(tail, text.find(start)) != -1 and text.split(tail)[1][0].isspace():
        starting_text = text.split(start)[0]
        ending_text = text.split(tail)[1]
        print(f"Result: {starting_text}{alternative}{ending_text}")
    else:
        print(f"Nothing to convert: {text}")


def main():
    # confusion()
    # almost_hangman()
    text_conversion()


if __name__ == "__main__":
    main()
