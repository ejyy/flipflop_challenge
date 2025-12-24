from collections import Counter

part1 = 0
part2 = 0
part3 = 0

input = [line.strip() for line in open("puzzle_03_input.txt", "r")]

part1 = Counter(input).most_common(1)[0][0]

for line in input:
    r, g, b = map(int, line.split(","))
    if r == g or r == b or g == b:  # Special
        part3 += 10
    elif r > g and r > b:  # Red
        part3 += 5
    elif g > r and g > b:  # Green
        part2 += 1
        part3 += 2
    elif b > r and b > g:  # Blue
        part3 += 4

print("Part 1:", part1)
print("Part 2:", part2)
print("Part 3:", part3)
