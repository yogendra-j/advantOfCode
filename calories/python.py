import os
cwd = os.getcwd()
print(cwd)
with open("input.txt") as input:
    cur_cal = 0
    max_cal = 0
    for line in input:
        line = line.strip()
        if not line:
            max_cal = max(max_cal, cur_cal)
            cur_cal = 0
        else:
            cur_cal += int(line)
    print(max_cal)