import utils
from pathlib import Path

sample_in = """"""

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    print(filename)
    input_split = utils.split_lines(filename)
    input_split = sample_in.splitlines()