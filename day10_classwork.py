# 1. Song class
# define a class Song
# The class constructor needs to have three additional 3 parameters (self and 3 more!)
# title defaults to empty string
# author defaults to empty string
# lyrics by default empty tuple

# inside constructor method:
# set/store these three parameters inside objects variables of the same name (remember to use self!)
#  print on the screen "New Song made" - (try also printing here author and title!)
#
# Minimum:
# Write a method sing that prints the song line by line on the screen, first printing the author and title, if any.
# Write a method yell that prints the song in capital letters line by line on the screen, first printing the author
# and title, if any.
#
# Bonus: make the above sing and chain methods chainable, so we can call them several times (chained)
# Bonus: create an additional parameter max_lines that prints only a certain number of lines for both sing and yell.
# Better do with some default value e.g. -1, at which all rows are then printed.
# Create multiple songs with lyrics


class Song:

    def __init__(self, title="Unknown Title", author="Unknown Artist", lyrics=[]):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print("\nNew Song made:", self.author, "-", self.title)

    def sing(self, max_lines=0):
        print("\nSinging:", self.author, "-", self.title)
        for line in self.lyrics:
            print(line, sep="\n")
            max_lines -= 1
            if max_lines == 0:
                break
        return self

    def yell(self, max_lines=0):
        print("\nSinging:", self.author, "-", self.title)
        for line in self.lyrics:
            print(line.upper(), sep="\n")
            max_lines -= 1
            if max_lines == 0:
                break
        return self


# 2. Rap class
# For those feeling comfortable with class syntax, create a Rap class that inherits from Song
# # no new constructor method is necessary (you can if you want)
# add a new method break_it with two default parameters max_lines=-1 and drop equal to "yeah", which is similar to
# sing, but adds a drop after each word .


class Rap(Song):

    def break_it(self, max_lines=1, drop="yeah"):
        print("\nSinging:", self.author, "-", self.title, "(Rap Version)")
        for line in self.lyrics:
            for word in line.split():
                print(word, drop.upper(), end=" ")
            print()
            max_lines -= 1
            if max_lines == 0:
                break
        return self


def main():
    ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
    ziemelmeita.sing(1).yell()

    vairogi = Song("Vairogi", "Līvi", ["Mūsu dziesmas ir vairogi seni", "Mēs tās par pagalvjiem liksim",
                                       "Daudzu likteņu pilni mēs elposim", "Kā pakalni Daugavas krastos"])
    vairogi.sing(2).yell(1)

    zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
    zrap.break_it(1, "yah")

    not_rap = Rap("Vairogi", "Līvi", ["Mūsu dziesmas ir vairogi seni", "Mēs tās par pagalvjiem liksim",
                                      "Daudzu likteņu pilni mēs elposim", "Kā pakalni Daugavas krastos"])
    not_rap.break_it(2, "*epic guitar solo*")


if __name__ == "__main__":
    main()
