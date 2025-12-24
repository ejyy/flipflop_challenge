part1 = 0
part2 = 0
part3 = 0

input = [line.strip() for line in open("puzzle_02_test.txt", 'r')][0]

height = 0

for char in input:
    if char == "^":
        height += 1
    elif char == "v":
        height -= 1
    part1 = max(height, part1)

height = 0
height_scalar = 0

for char in input:
    if char == "^":
        if height_scalar <= 0:
            height_scalar = 1
        else:
            height_scalar += 1
        height += height_scalar
    elif char == "v":
        if height_scalar >= 0:
            height_scalar = -1
        else:
            height_scalar -= 1
        height += height_scalar
    part2 = max(height, part2)

print("Part 1:", part1)
print("Part 2:", part2)
print("Part 3:", part3)
