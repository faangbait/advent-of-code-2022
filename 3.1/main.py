def item_to_priority(item: str) -> int:
    if ord(item) <= 90: # A - Z
        return ord(item) - 38
    else:
        return ord(item) - 96

with open("input") as infile:
    lines = infile.readlines()
    
    priority_sum = 0

    for line in lines:
        midpoint = len(line) // 2
        part_1 = set(line[:midpoint])
        part_2 = set(line[midpoint:])

        intersection = part_1.intersection(part_2)
        
        if len(intersection) != 1:
            raise Exception("Error intersecting: not 'one and only one' result")

        item = intersection.pop()

        print(f"Item: {item}\t\tPriority: {item_to_priority(item)}")
        priority_sum += item_to_priority(item)

    print(f"The sum of priorities of duplicate items is: {priority_sum}")
