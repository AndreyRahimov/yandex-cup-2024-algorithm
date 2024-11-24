# n, m = int(input()), int(input())
# weights_per_bag = [int(a) for a in input().split() if int(a) <= n]
# weights_per_bag.sort()
#
# max_weight = 2**26
# powers_n = 27
#
# powers_of_two = [2**i for i in range(27) if 2**i <= n]
# zeros = True if 0 in weights_per_bag else False


def get_combinations_amount(power, num):
    weight = 2 ** power

    if weight > num:
        return 0

    if weight == num:
        return 1
