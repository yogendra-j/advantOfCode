response_table = {
    "A": {
        "X": "C",
        "Y": "A",
        "Z": "B"
    },
    "B": {
        "X": "A",
        "Y": "B",
        "Z": "C"
    },
    "C": {
        "X": "B",
        "Y": "C",
        "Z": "A"
    }
}
move_points_table = {
    "A": 1,
    "B": 2,
    "C": 3
}
result_point_table = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

with open("input.txt") as inp:
    points = 0
    for line in inp:
        opp, result = line.split()
        points += result_point_table[result]
        points += move_points_table[response_table[opp][result]]
    print(points)