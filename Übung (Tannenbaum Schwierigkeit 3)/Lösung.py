import math

levels = 3
level_width = 31
level_step = 2

trunk_height = 3
trunk_width = 3

level_height = (level_width / (2 * level_step)) + 1
level_start_spaces = math.floor(level_width / 2)

for level in range(levels):
    signs = 1
    spaces = level_start_spaces

    while spaces >= 0:
        print(" " * spaces + "#" * signs)

        signs += level_step * 2
        spaces -= level_step

trunk_spaces = level_start_spaces - math.floor(trunk_width / 2)

for level in range(trunk_height):
    print(" " * trunk_spaces + "#" * trunk_width)
