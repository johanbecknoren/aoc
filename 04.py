import utils
from pathlib import Path

sample_in = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    print(filename)
    input_split = utils.split_lines(filename)
    # input_split = sample_in.splitlines()

    num_fully_contained = 0
    num_overlaps = 0
    for row in input_split:
        left, right = row.split(",")
        l_start, l_end = left.split("-")
        r_start, r_end = right.split("-")
        l = [v for v in range(int(l_start), int(l_end)+1)]
        r = [v for v in range(int(r_start), int(r_end)+1)]
        overlap = len(set(l) & set(r))

        # part one
        if overlap == len(l) or overlap == len(r):
            num_fully_contained += 1

        # part two
        if overlap > 0:
            num_overlaps += 1

    print("Fully contained: " + str(num_fully_contained))
    print("Num overlapping pais: " +str(num_overlaps))
    