def calculate_floor(string):
    floor = 0
    for i in range(4):
        if string[i].lower() == "d":
            floor -= 1
        elif string[i].lower() == "u":
            floor += 1
    return floor

print(calculate_floor("DDDD"))