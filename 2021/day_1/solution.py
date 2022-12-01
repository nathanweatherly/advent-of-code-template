# https://adventofcode.com/2021/day/1

import os
import sys

input_filename = sys.argv[-1]


def read_input():
    enable_word_list = list(map(str.rstrip, open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), input_filename), "r").read().split("\n")))
    return enable_word_list


input = read_input()


def part_one():
    increase_count = 0
    for i in range(len(input)):
        if (i == 0):
            continue
        if (int(input[i]) > int(input[i-1])):
            increase_count += 1
    return increase_count


def part_two():
    increase_count = 0
    for i in range(len(input)):
        if (i < 3):
            continue
        prev_slide = int(input[i-1]) + int(input[i-2]) + int(input[i-3])
        curr_slide = int(input[i]) + int(input[i-1]) + int(input[i-2])
        if (curr_slide > prev_slide):
            increase_count += 1
    return increase_count


print("Part 1: " + str(part_one()))
print("Part 2: " + str(part_two()))
