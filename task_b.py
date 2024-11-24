t = int(input())

for i in range(t):
    n = int(input())
    heights = map(int, input().split())

    if n < 3:
        print(0)
        continue

    mountains = to_mountain = 0
    descent = False
    prev = next(heights)

    for height in heights:
        if height > prev and descent:
            to_mountain = 1
            descent = False

        elif height > prev:
            to_mountain += 1

        elif height < prev and 0 < to_mountain:
            mountains += to_mountain
            descent = True

        else:
            to_mountain = 0

        prev = height

    print(mountains)
