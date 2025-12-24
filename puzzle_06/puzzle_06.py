input = [line.strip() for line in open("puzzle_06_input.txt", "r")]

num_steps = 100
sky_width, sky_height = 1000, 1000
frame_width, frame_height = 500, 500

frame_x0 = (sky_width - frame_width) // 2
frame_y0 = (sky_height - frame_height) // 2

grid = [[[] for i in range(sky_width)] for j in range(sky_height)]

for bird_idx, speeds in enumerate(input):
    dx, dy = speeds.split(",")

    x = (int(dx) * num_steps) % sky_width
    y = (int(dy) * num_steps) % sky_height

    grid[y][x].append(bird_idx)

within_box = []

for y_idx, y in enumerate(grid):
    for x_idx, x in enumerate(y):
        for bird_idx in x:
            if (
                frame_x0 <= x_idx < frame_x0 + frame_width
                and frame_y0 <= y_idx < frame_y0 + frame_height
            ):
                within_box.append(bird_idx)

print("Part 1:", len(within_box))
