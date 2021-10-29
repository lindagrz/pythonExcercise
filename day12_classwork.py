import string
from collections import Counter


# File Operations You will want to use veidenbaums.txt for analysis. It is in the class git repository under
# Day12_File_Operations folder You can also download it directly from the following link:
# https://raw.githubusercontent.com/ValRCS/Python_TietoEvry_Sep2021/main/Day12_File_Operations/veidenbaums.txt

# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file
# check file_line_len ("veidenbaums.txt") -> should be 971 or 972

def file_line_len(fpath, encoded="UTF-8"):
    return sum(1 for line in open(fpath, mode="r", encoding=encoded))


# 1b -> write the function get_poem_lines (fpath), which returns a list with only those lines that contain poetry.
# So we want to avoid/filter out those lines that contain whitespace and also those lines with poem titles.
# PS preferably use encoding = "utf-8"

def get_poem_lines(fpath, encoded="UTF-8"):
    lines = list()
    with open(fpath, mode="r", encoding=encoded) as f:
        for line in f:
            if not (line == "\n" or line.endswith("***\n")):
                lines.append(line)
    return lines


# 1c -> write the function save_lines (destpath, lines)
# This function will store all lines into destpath file
# 1d -> call save_lines with destpath being "veid_poems.txt" and lines being the poem lines we cleaned from 1b

def save_lines(destpath, lines, encoded="UTF-8"):
    with open(destpath, mode="w", encoding=encoded) as f:
        f.writelines(lines)


# 1e -> write the function clean_punkts (srcpath, destpath)
# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation
# then function will save the cleaned text into destpath

def clean_punkts(srcpath, destpath, encoded="UTF-8"):
    with open(srcpath, mode="r", encoding=encoded) as src_file, open(destpath, mode="w", encoding=encoded) as dest_file:
        text = src_file.read()
        for p in string.punctuation:
            text = text.replace(p, "")
        dest_file.write(text)


# 1f -> write the function get_word_usage (srcpath, destpath)
# The function opens the file and finds the most frequently used words
# recommendation to use Counter module!
# assume that the words are separated by either whitespace or newline (the good old split will come in handy)
# the saved list of words and frequency should be saved in destpath in the following form:
# vards skaits
# un 3423
# es 3242
# PS to test, for srcpath use the file that is poetry only and has no punctuation and also the words are all in
# lowercase


def get_word_usage(srcpath, destpath="", encoded="UTF-8"):
    with open(srcpath, mode="r", encoding=encoded) as f:
        text = f.read()
    words = text.lower().replace("\n", " ").split()
    count = Counter(words)
    with open(destpath, mode="w", encoding=encoded) as f:
        f.write("vards skaits\n")
        for word, c in count.most_common():
            f.write(f"{word} {c}\n")


def main():
    # print(file_line_len("day12_files/veidenbaums.txt"))
    # poem_lines = get_poem_lines("day12_files/veidenbaums.txt")
    # print(poem_lines)
    # save_lines("day12_files/savelines_res.txt", poem_lines)
    # clean_punkts("day12_files/savelines_res.txt", "day12_files/cleanpunkts_res.txt")
    get_word_usage("day12_files/cleanpunkts_res.txt", "day12_files/poem_stats.txt")


if __name__ == "__main__":
    main()
