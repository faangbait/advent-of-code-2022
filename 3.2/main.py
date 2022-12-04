def item_to_priority(item: str) -> int:
    if ord(item) <= 90: # A - Z
        return ord(item) - 38
    else:
        return ord(item) - 96

with open("input") as infile:
    priority_sum = 0

    while True:
        elf_group = [
            set(infile.readline().strip()),
            set(infile.readline().strip()),
            set(infile.readline().strip())
        ]

        if len(elf_group[2]) == 0:
            break
        
        intersection = elf_group[0].intersection(*elf_group[1:])

        if len(intersection) != 1:
            raise Exception("Error intersecting: not 'one and only one' result")

        item = intersection.pop()

        print(f"Item: {item}\t\tPriority: {item_to_priority(item)}")
        priority_sum += item_to_priority(item)

    print(f"The sum of badge priorities is: {priority_sum}")
