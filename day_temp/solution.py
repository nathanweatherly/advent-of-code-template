import os
import sys

input_filename = sys.argv[-1]

# returns input as a list of strings separated by newlines
def read_input():
    enable_word_list = list(map(str.rstrip, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), input_filename), "r").read().split("\n")))
    return enable_word_list


input = read_input()


# YOU IMPLEMENT THIS
def part_one():
    return "TODO"


# YOU IMPLEMENT THIS
def part_two():
    return "TODO"


print("Part 1: " + str(part_one()))
print("Part 2: " + str(part_two()))
