with open("input") as infile:
    lines = infile.readlines()

    calories_carried = []
    cur_calories = 0

    for line in lines:
        if len(line.strip()) == 0:
            calories_carried.append(cur_calories)
            cur_calories = 0
        else:
            cur_calories += int(line.strip())

    calories_carried.sort()

    print(
        "The sum of the calories carried by the top three elves is: "
        f"{calories_carried.pop() + calories_carried.pop() + calories_carried.pop()}"
    )
