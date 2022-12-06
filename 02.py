import utils
from pathlib import Path

sample_in = """A Y
B X
C Z"""

# A Rock
# B Paper
# C Scissors

# X Rock
# Y Paper
# Z Scissors

BEATS = {"A": "C", "B": "A", "C": "B"}
POINTS = {"A": 1, "B": 2, "C": 3}
MAPPING = {"X": "A", "Y": "B", "Z": "C"}
MAPPING_REVERSE = {"A": "X", "B": "Y", "C": "Z"}
SCORE_WIN = 6
SCORE_DRAW = 3
SCORE_LOSS = 0

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    print(filename)
    input_split = utils.split_lines(filename)
    # input_split = sample_in.splitlines()
    print(input_split)

    sum_score = 0
    for round in input_split:
        i,j = round.split()

        # Part two
        slask = {"A", "B", "C"}
        if j == "Z": #win
            j = MAPPING_REVERSE[BEATS[BEATS[i]]]
        elif j == "Y": # draw
            j = MAPPING_REVERSE[i]
        elif j == "X": #loose
            j = MAPPING_REVERSE[BEATS[i]]

        score = POINTS[MAPPING[j]]
        if i == MAPPING[j]:
            score += SCORE_DRAW
        elif BEATS[MAPPING[j]] == i:
            score += SCORE_WIN
        print(score)
        sum_score += score
    print("-------")
    print(sum_score)

