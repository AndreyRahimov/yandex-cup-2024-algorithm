dance = input()
all_right = dance.replace("?", "R")
all_left = dance.replace("?", "L")

minimum = maximum = count = 0

for step in all_right:
    if step == "R":
        count += 1
        maximum = max(maximum, count)

    else:
        count -= 1
        minimum = min(minimum, count)

all_right_res = maximum + abs(minimum)

minimum = maximum = count = 0

for step in all_left:
    if step == "R":
        count += 1
        maximum = max(maximum, count)

    else:
        count -= 1
        minimum = min(minimum, count)

all_left_res = maximum + abs(minimum)

print(max(all_right_res, all_left_res))
