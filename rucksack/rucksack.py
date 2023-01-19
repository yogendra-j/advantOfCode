with open("input.txt") as inp:
    priority = 0
    member_count = 0
    common_item = set() 
    for rucksack in inp:
        member_count += 1
        if common_item:
            common_item = common_item.intersection(set(rucksack.strip()))
        else:
            common_item = set(rucksack.strip())
        if member_count == 3:
            for item in common_item:
                priority += ord(item.lower()) - ord("a") + 1
                priority += 26 * item.isupper()
            member_count = 0
            common_item.clear()
    print(priority)
