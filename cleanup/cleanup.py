def overlapping_intervals(interval1: list[int], interval2: list[int]) -> bool:
    return not (interval1[0] > interval2[1] or interval1[1] < interval2[0])

with open("input.txt") as inp:
    count = 0
    for line in inp:
        interval1, interval2 = map(lambda x: list(map(int, x.split("-"))), line.split(","))
        if overlapping_intervals(interval1, interval2):
            count += 1
    print(count)
