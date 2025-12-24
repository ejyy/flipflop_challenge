part1 = 0
part2 = 0
part3 = 0

input = [line.strip() for line in open("puzzle_01_input.txt", "r")]

for line in input:
    line_ne_na = line.replace("ne", "na")
    ba_na_count = line_ne_na.count("na") + line_ne_na.count("ba")

    part1 += ba_na_count

    if ba_na_count % 2:
        part2 += ba_na_count

    if "ne" not in line:
        part3 += ba_na_count

print("Part 1:", part1)
print("Part 2:", part2)
print("Part 3:", part3)
