import utils
import operator
from pathlib import Path
from collections import OrderedDict

sample_in = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

cycles    = {"noop": 1,    "addx": 2}
operation = {"noop": None, "addx": operator.add}

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    print(filename)
    input_split = utils.split_lines(filename)
    #input_split = sample_in.splitlines()

    X = 1
    cycles_count = 0
    cycles_set = OrderedDict()
    cycles_set = {0: 1} # X has value 1 at 0 cycles
    tot_signal_strenth = 0

    for line in input_split:
        instr = line.split()
        op_name, op_arg = (instr[0], instr[1]) if len(instr) > 1 else (instr[0], operator.add)
        cycles_count += cycles[op_name]
        op_func = operation[op_name]
        if (op_func):
            X = op_func(X, int(op_arg))
        cycles_set[cycles_count+1] = X
    cycles_list = list(cycles_set.items())
    
    def get_val_cycle(c: int, do_scoring = False):
        if c in cycles_set:
            return c * cycles_set[c] if do_scoring else cycles_set[c]
        else:
            x = c
            while x not in cycles_set:
                x -= 1
            slask = cycles_set[x]
            return c * slask if do_scoring else cycles_set[x]
    
    for index in range(20, 221, 40):
        tot_signal_strenth += get_val_cycle(index, True)
    print(X)
    print(tot_signal_strenth)

    # part two
    width, height = 40, 6
    chars_sprite_pos = []
    # debug draw sprite pos per cycle up to 20 cycles
    for i in range(20):
        cycle = i+1
        sprite_pos = get_val_cycle(cycle)
        for j in range(width):
            if j == sprite_pos - 1 or j == sprite_pos or j == sprite_pos + 1:
                chars_sprite_pos.append("#")
            else:
                chars_sprite_pos.append(".")
        chars_sprite_pos.append("\n")
    print(''.join(chars_sprite_pos))

    # draw actual pixel-to-sprite matches
    chars_sprite_pos.clear()
    for y in range(height):
        sprite_pos = get_val_cycle(y*width+1)
        for x in range(width):
            cycle = width * y + x + 1
            if x == sprite_pos - 1 or x == sprite_pos or x == sprite_pos + 1:
                chars_sprite_pos.append("#")
            else:
                chars_sprite_pos.append(".")
            sprite_pos = get_val_cycle(cycle+1)
        
             
        chars_sprite_pos.append("\n")
    print(''.join(chars_sprite_pos))
