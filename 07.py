import utils
from pathlib import Path
from enum import IntFlag

sample_in = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

class Type(IntFlag):
    DIR = 0,
    FILE = 1

class Node:
    def __init__(self, type, parent = None, children = [], size = 0, name = "") -> None:
        self.parent: Node = parent
        self.children: list[Node] = children
        self.size: int = size
        self.type: Type = type
        self.name: str = name

def has_child(child_name: str, node: Node) -> Node:
    for child in node.children:
        if child_name == child.name:
            return child
    return None

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    print(filename)
    input_split = utils.split_lines(filename)
    # input_split = sample_in.splitlines()

    root = Node(type=Type.DIR)
    root.name = "/"
    current_dir: Node = root
    for line in input_split[1:]:
        if line.startswith("$"):
            if "cd" in line:
                target_dir = line[5:]
                if ".." in target_dir:
                    current_dir = current_dir.parent
                    continue
                child = has_child(target_dir, current_dir)
                if child:
                    current_dir = child
                else:
                    n = Node(name=target_dir, type=Type.DIR, parent=current_dir)
                    current_dir.children.append(n)
                    current_dir = n
            if "ls" in line:
                continue
        elif line.startswith("dir"):
            if has_child(line[4:], current_dir) is None:
                current_dir.children.append(Node(name=line[4:], type=Type.DIR, parent=current_dir, children=[]))
        else:
            size, name = line.split()
            if has_child(name, current_dir) is None:
                current_dir.children.append(Node(name=name, size=size, type=Type.FILE, parent=current_dir, children=[]))
                current_dir.size += int(size)
                # propagate size up
                slask = current_dir.parent
                while slask is not None:
                    slask.size += int(size)
                    slask = slask.parent
    # print the tree
    def draw_node(node: Node, depth: str):
        dir = ""
        if node.type == Type.DIR:
            dir = " (dir)"
        print(depth + "- " + node.name + ", size: " + str(node.size) + dir)
        for n in node.children:
            draw_node(n, depth=depth + "    ")
    # draw_node(root, "")

    # part two
    used_space = root.size
    unused_space = 70000000 - used_space
    to_delete = 30000000 - unused_space

    # max_dir_size = 100000 # part one
    max_dir_size = to_delete
    dir_sizes = []
    def iterate_nodes(node: Node, space):
        # if node.type == Type.DIR and node.size <= space: # part one
        if node.type == Type.DIR and node.size >= space:
            dir_sizes.append(node)
        for n in node.children:
            iterate_nodes(n, space)
    iterate_nodes(root, max_dir_size)
    
    sum = 0
    for dir in dir_sizes:
        sum += dir.size
    print(sum)
    print("part two: " + str(sorted(dir_sizes, key=lambda x: x.size)[0].size))
