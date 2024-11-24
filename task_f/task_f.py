t = int(input())
k = 16
print(k)

# Define constants at the start
TOTAL_RANGE = range(2025)
HALF = 1012
QUARTER = 506

first = {i for i in TOTAL_RANGE if i < HALF}
second = {i for i in TOTAL_RANGE if i >= HALF}
third = {i for i in TOTAL_RANGE if i % 2 == 0}
fourth = {i for i in TOTAL_RANGE if i % 2 == 1}
fifth = {i for i in TOTAL_RANGE if i % 4 in (0, 1)}
sixth = {i for i in TOTAL_RANGE if i % 4 in (2, 3)}
seventh = {i for i in TOTAL_RANGE if i % 4 in (0, 3)}
eighth = {i for i in TOTAL_RANGE if i % 4 in (1, 2)}
ninth = {i for i in TOTAL_RANGE if i in range(QUARTER) or i in range(1519, 2025)}
tenth = {
    i for i in TOTAL_RANGE if i not in range(QUARTER) and i not in range(1519, 2025)
}
eleventh = {i for i in TOTAL_RANGE if i in range(507, 1518)}
twelfth = {i for i in TOTAL_RANGE if i not in range(507, 1518)}
thirteenth = {
    i for i in TOTAL_RANGE if (i % 3 == 0) or (i % 3 == 1 and i < HALF)
}  # Unique pattern based on modulo 3
fourteenth = {
    i for i in TOTAL_RANGE if (i % 3 == 2) or (i % 3 == 1 and i >= HALF)
}  # Complementary to thirteenth
fifteenth = {
    i
    for i in TOTAL_RANGE
    if i in range(0, 253)
    or i in range(506, 759)
    or i in range(1012, 1265)
    or i in range(1518, 1771)
}
sixteenth = {
    i
    for i in TOTAL_RANGE
    if i not in range(0, 253)
    and i not in range(506, 759)
    and i not in range(1012, 1265)
    and i not in range(1518, 1771)
}  # Complementary to fifteenth


numbers_sets = (
    first,
    second,
    third,
    fourth,
    fifth,
    sixth,
    seventh,
    eighth,
    ninth,
    tenth,
    eleventh,
    twelfth,
    thirteenth,
    fourteenth,
    fifteenth,
    sixteenth,
)

for numbers_set in numbers_sets:
    print(*numbers_set)

result = []
too_many_questions = False

for _ in range(t):
    answers = list(map(int, input().split()))

    if -1 in answers:
        too_many_questions = True
        break

    for number in TOTAL_RANGE:
        contradictions = 0
        for number_set, answer in zip(numbers_sets, answers):
            if (number in number_set) != (answer == 1):
                contradictions += 1
            if contradictions > 1:
                break
        if contradictions <= 1:
            result.append(number)
            break

if not too_many_questions:
    print(*result)
