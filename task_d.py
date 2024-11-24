maximum = float("inf")
h = 1
minimum = 1
print(h, flush=True)

while True:
    response = input()

    if response == "fail":
        break

    elif minimum == maximum:
        print(f"! {h}", flush=True)
        break

    elif response == "wet" and maximum == float("inf"):
        minimum = h
        h = h * 2
        print(h, flush=True)

    elif response == "ok":
        maximum = h
        h = (minimum + h) // 2
        print(h, flush=True)

    elif response == "wet":
        minimum = h + 1
        h = (minimum + maximum) // 2
        print(h, flush=True)
