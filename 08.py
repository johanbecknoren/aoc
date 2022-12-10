import utils
from pathlib import Path
import numpy

sample_in = """30373
25512
65332
33549
35390"""

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    print(filename)
    input_split = utils.split_lines(filename)
    # input_split = sample_in.splitlines()

    dim = (len(input_split[0]), len(input_split))
    print("dims: " + str(dim))
    mat: numpy.ndarray(shape=dim, dtype=int, order="C")
    data = []
    for line in input_split:
        row = []
        for c in line:
            data.append(int(c))
    
    mat = numpy.array(data)
    mat = numpy.reshape(mat, dim)
    r_begin = c_begin = 1 # ignore outer border since they're all visible
    r_end = c_end = dim[0] - 2
    sum_visible = (dim[0]-1) * 4
    scenic_scores = []
    for r in range(r_begin, r_end+1):
        for c in range(c_begin, c_end+1):
            left, right, up, down = numpy.flip(mat[r][:c]), mat[r][c+1:], numpy.flip(mat[:,c][:r]), mat[:,c][r+1:]
            dirs = [left, right, up, down]
            left_max, right_max, up_max, down_max, current = numpy.max(left), numpy.max(right), numpy.max(up), numpy.max(down), mat[r][c]
            # part one
            if current > left_max or current > right_max or current > up_max or current > down_max:
                sum_visible += 1

            # part two
            def calc_scenic(current: int, trees: list[int]) -> int:
                score = 0
                for tree in trees:
                    if tree >= current:
                        return score+1
                    score += 1
                return score
            score = 1
            for dir in dirs:
                score *= calc_scenic(current, dir)
            scenic_scores.append(score)

    print(sum_visible)
    print(list(reversed(sorted(scenic_scores)))[0])
