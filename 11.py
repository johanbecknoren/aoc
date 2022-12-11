import utils
import operator
from pathlib import Path
import numpy as np
from functools import reduce

sample_in = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

my_int_type = int

operators = {"*": operator.mul, "-": operator.sub, "+": operator.add, "/": operator.floordiv}
class Monkey:
    starting_items = list[my_int_type] # worry levels of each item
    operation_func = None # how my worry level changes as the monkey inspects starting_items
    operation_args = None
    test_func = None # how the monkey uses my worry level to decide what item to throw
    test_args = None
    true_monkey_idx: my_int_type = 0
    false_monkey_idx: my_int_type = 0
    num_inspected_items: my_int_type = 0

monkeys = []

def op(old: my_int_type, slask): 
    v = old if slask[1] == "old" else my_int_type(slask[1])
    return operators[slask[0]](old, v)

def test(nom, denom):
    return nom % denom == 0

if __name__ == "__main__":
    filename = (Path(__file__).parent / (__file__[:__file__.find(".")] + ".txt")).name
    print(filename)
    input_split = utils.split_lines(filename)
    input_split = sample_in.splitlines()

    for i in range(0, len(input_split), 7):
        parse_monkey_num        = input_split[i]
        parse_staring_items     = input_split[i+1]
        parse_operation         = input_split[i+2]
        parse_test              = input_split[i+3]
        parse_if_true           = input_split[i+4]
        parse_if_false          = input_split[i+5]
        monkey = Monkey()
        monkey.starting_items = [my_int_type(v) for v in parse_staring_items[18:].split(", ")]
        monkey.operation_func = op
        monkey.operation_args = parse_operation[22:].split()
        monkey.test_func = test
        monkey.test_args = my_int_type(parse_test.split()[-1])
        monkey.true_monkey_idx = my_int_type(parse_if_true.split()[-1])
        monkey.false_monkey_idx = my_int_type(parse_if_false.split()[-1])

        monkeys.append(monkey)
        # for items in 

    modulo = reduce(operator.mul, [m.test_args for m in monkeys]) # find common denominator of tests

    DEBUG_PRINT = False
    for turn in range(10000):
        count = 0
        for m in monkeys:
            if DEBUG_PRINT: print(f"### Monkey {count}: ###")
            for worry in m.starting_items:
                m.num_inspected_items += 1
                if DEBUG_PRINT: print(f"  Monkey inspects an item with a worry level of {worry}.")
                actual_worry = m.operation_func(worry, m.operation_args) # perform worry operation (inspect)
                actual_worry = actual_worry % modulo
                if DEBUG_PRINT: print(m.operation_args)
                if DEBUG_PRINT: print(actual_worry)
                # part one
                # actual_worry = int(actual_worry/3) # monkey bored with item
                test_result = m.test_func(actual_worry, m.test_args)
                if test_result:
                    if DEBUG_PRINT: print(f"    TRUE Item with worry level {actual_worry} is thrown to monkey {m.true_monkey_idx}")
                    monkeys[m.true_monkey_idx].starting_items.append(actual_worry)
                else:
                    if DEBUG_PRINT: print(f"    FALSE Item with worry level {actual_worry} is thrown to monkey {m.false_monkey_idx}")
                    monkeys[m.false_monkey_idx].starting_items.append(actual_worry)
            m.starting_items.clear()
            count += 1
        afsdads = 0
        print_turns = [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
        if (turn+1) in print_turns:
            print(f"== After round {turn+1} ==")
            for m in monkeys:
                # debug print per monkey
                # msg = f"Monkey {afsdads}: "
                # for worry in m.starting_items:
                #     msg = msg + str(my_int_type(worry)) + ", "
                # print(msg)
                print(f"Monkey {afsdads} inspected items {m.num_inspected_items} times.")
                afsdads += 1

        if turn == 19:
            sorted_monkeys = list(reversed(sorted(monkeys, key=lambda x: x.num_inspected_items)))
            print(f"Part one: {(sorted_monkeys[0].num_inspected_items * sorted_monkeys[1].num_inspected_items)}")

    sorted_monkeys = list(reversed(sorted(monkeys, key=lambda x: x.num_inspected_items)))
    print(f"Part two: {(sorted_monkeys[0].num_inspected_items * sorted_monkeys[1].num_inspected_items)}")
