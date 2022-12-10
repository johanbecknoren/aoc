import utils
from pathlib import Path

sample_in = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    print(filename)
    input_split = utils.split_lines(filename)
    #input_split = sample_in.splitlines()

    commands = []
    for line in input_split:
        dir, length = line.split()
        commands.append((dir, int(length)))
    dir = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    x_max, y_max = -100000, -100000
    x_min, y_min = 100000, 100000
    h_pos = (0,0)
    t_pos = (0,0)
    tails_pos = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    
    def sign(x): 
        return 0 if x == 0 else (1-(x<=0)) * 2 - 1

    def move_tail(head_pos, tail_pos, v = None):
        diff_x, diff_y = head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]
        if abs(diff_x) < 2 and abs(diff_y) < 2:
            return tail_pos
        while abs(diff_x) >= 2 or abs(diff_y) >= 2:
            if head_pos[0] != tail_pos[0] and head_pos[1] != head_pos[1]: # always move diagonally in this case
                x = sign(diff_x)
                y = sign(diff_y)
            else:
                x = min(1, abs(diff_x)) * sign(diff_x)
                y = min(1, abs(diff_y)) * sign(diff_y)
            tail_pos = (tail_pos[0] + x, tail_pos[1] + y)
            diff_x, diff_y = head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]
            # print(tail_pos)
            if v:
                v.add(tail_pos)
        return tail_pos

    visited = set()
    visited.add((0, 0))

    # hacky debug visualization
    def debug_print_visited():
        # larger sample
        x, y = 21, 26
        chars_visited = []
        chars_state = []
        for i in reversed(range(-5, x-5)):
            for j in range(-11, y-11):
        # small sample
        # x, y = 5, 6
        # chars_visited = []
        # chars_state = []
        # for i in reversed(range(x)):
        #     for j in range(y):
                if i == 0 and j == 0:
                    chars_visited.append("s")
                elif (j,i) in visited:
                    chars_visited.append("#")
                else:
                    chars_visited.append(".")
                
                chars_state.append(".")
                for k in reversed(range(len(tails_pos))):
                    if tails_pos[k] == (j,i):
                        chars_state.pop()
                        chars_state.append(str(k+1))
                if (j,i) == h_pos:
                    chars_state.pop()
                    chars_state.append("H")
            chars_visited.append("\n")
            chars_state.append("\n")
        visited_as_string = ''.join(chars_visited)
        print(visited_as_string)
        state_as_string = ''.join(chars_state)
        #print(state_as_string)

    for c in commands:
        #print(c)
        for step in range(c[1]):
            x = h_pos[0] + dir[c[0]][0]
            y = h_pos[1] + dir[c[0]][1]
            prev_h_pos = h_pos
            h_pos = (x, y)
            # part one
            #t_pos = move_tail(h_pos, t_pos, visited)
            # part two
            tails_pos[0] = move_tail(h_pos, tails_pos[0]) # first tail follows head
            for i in range(1,8): # other tails follow tail in front
                tails_pos[i] = move_tail(tails_pos[i-1], tails_pos[i])
            tails_pos[8] = move_tail(tails_pos[7], tails_pos[8], visited)
    debug_print_visited()
            

    #print(visited)
    count = 0
    for v in visited:
        count += 1
    print("Visited: " + str(count))

    



    # part two:
    # 2793, too high
