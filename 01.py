import utils
from pathlib import Path

sample_in = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    input_split = utils.split_lines(filename)
    max_calories = 0
    sum_calories = 0

    list_cals = []

    for s in input_split:
        if s is "":
            if sum_calories > max_calories:
                max_calories = sum_calories
            list_cals.append(sum_calories)
            sum_calories = 0
        else:
            sum_calories = sum_calories + int(s)

    list_cals.sort(reverse=True)
    top_three_cal_sum = list_cals[0] + list_cals[1] + list_cals[2]

    print("#1 max calories: " + str(max_calories))
    print("#2 top three calories sum: " + str(top_three_cal_sum))
