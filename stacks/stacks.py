def make_stacks(stacks: list[list[str]], rows: list[str]):
    for row in rows[::-1]:
        i = 0
        for item in row[1: : 4]:
            if (not item.isspace()):
                stacks[i].append(item)
            i += 1

def shift_items_one_at_a_time(from_stack: int, to_stack: int, count: int, stacks: list[list[str]]):
    for _ in range(count):
        stacks[to_stack].append(stacks[from_stack].pop())

def shift_items_all_at_once(from_stack: int, to_stack: int, count: int, stacks: list[list[str]]):
    buffer = []
    for _ in range(count):
        buffer.append(stacks[from_stack].pop())
    for _ in range(count):
        stacks[to_stack].append(buffer.pop())

with open("input.txt") as inp:
    stacks: list[list[str]] = []
    rows = []
    for line in inp:
        if line.isspace(): break
        if line[1].isdigit():
            stacks = [[] for _ in range(len(line.split()))]
        else:
            rows.append(line)
    make_stacks(stacks, rows)

    for line in inp:
        _, count, _, from_stack, _, to_stack = line.split()
        shift_items_all_at_once(int(from_stack) - 1, int(to_stack) - 1, int(count), stacks)
    print("".join([stack[-1] for stack in stacks]))

        