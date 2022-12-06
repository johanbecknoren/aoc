import utils
from pathlib import Path

sample_in = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    print(filename)
    input_split = utils.split_lines(filename)
    # input_split = sample_in.splitlines()

    num_stacks = -1
    stacks = []
    stack_end_idx = 0

    # calc end line index of stacks
    for line in input_split:
        if "[" not in line:
            num_stacks = len(line.split())
            break
        stack_end_idx += 1

    # init list to hold stacks
    for stack in range(num_stacks):
        stacks.append([])

    # read crates into stacks lists
    for i in range(stack_end_idx):
        line = input_split[i]
        cursor = 0
        while cursor < len(line):
            crate: str = line[cursor: cursor+4].strip()
            if crate:
                stacks[int(cursor/4)].append(crate)
            cursor += 4
    for stack in stacks:
        stack.reverse()

    # parse move commands
    commands = []
    for i in range(stack_end_idx+2, len(input_split)):
        line = input_split[i].split()
        commands.append((int(line[1]), int(line[3]), int(line[5])))

    # execute move commands
    for command in commands:
        amount, frm, to = command
        # part one
        # for i in range(amount):
        #     crate = stacks[frm-1].pop()
        #     stacks[to-1].append(crate)

        # part two
        crates = []
        for i in range(amount):
            crates.append(stacks[frm-1].pop())
        for i in range(amount):
            stacks[to-1].append(crates.pop())

    for stack in stacks:
        if stack:
            print(stack.pop())
        else:
            print("EMPTY!")
    