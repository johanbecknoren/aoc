from typing import overload
import utils
from pathlib import Path

sample_in = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def get_prio(c: str) -> int:
    if (c.islower()):
        return ord(c) - 96
    if (c.isupper()):
        return ord(c) - 38

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    print(filename)
    input_split = utils.split_lines(filename)
    # input_split = sample_in.splitlines()

    sum_prio = 0
    sum_prio2 = 0
    i: int = 0
    for ruck in input_split:
        i += 1

        # part one
        comp_size = int(len(ruck) / 2)
        left = ruck[:comp_size]
        right = ruck[comp_size:]
        overlap = list(set(left) & set(right))
        assert(len(overlap) == 1)

        prio = get_prio(overlap[0])
        sum_prio += prio

        # part two
        if i % 3 == 0:
            elf1, elf2, elf3 = (input_split[i-3], input_split[i-2], input_split[i-1])
            overlap2 = list(set(elf1) & set(elf2) & set(elf3))
            assert(len(overlap2) == 1)
            print(overlap2)
            prio = get_prio(overlap2[0])
            print("prio: " + str(prio))
            sum_prio2 += prio



        # print("left:  " + left)
        # print("right: " + right)
        # print("-----")
        # print(ord("z"))
        # print(ord("a"))
        # print(ord("Z"))
        # print(ord("A"))
    print("Overlap sum: " + str(sum_prio))
    print("Overlap sum 2: " + str(sum_prio2))

    # part two

