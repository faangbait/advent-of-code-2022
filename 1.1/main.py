with open("input") as infile:
    lines = infile.readlines()

    elf_index = 0
    elf_leader = elf_index
    max_calories = 0
    cur_calories = 0

    for line in lines:
        if len(line.strip()) == 0:
            elf_index += 1
            cur_calories = 0
        else:
            cur_calories += int(line.strip())
            if cur_calories > max_calories:
                elf_leader = elf_index
                max_calories = cur_calories

    print(f"Elf #{elf_leader + 1} is carrying the most calories: {max_calories}")
