import utils
from pathlib import Path

sample_in = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    print(filename)
    input_split = utils.split_lines(filename)
    #input_split = sample_in.splitlines()
    data = input_split.pop()

    cursor = 3
    # packet_len = 4 # part one
    packet_len = 14 # part two
    while cursor < len(data)-1:
        packet = set()
        for i in range(packet_len):
            packet.add(data[cursor-i])
        cursor += 1
        if len(packet) == packet_len:
            break
        
    print("cursor: " + str(cursor))
