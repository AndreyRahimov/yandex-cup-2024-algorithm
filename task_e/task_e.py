n, m = int(input()), int(input())
weights_per_bag = [int(a) for a in input().split() if int(a) <= n]
weights_per_bag.sort()

max_weight = 2**26
powers_n = 27

dp = [0] * (n + 1)

# Calculate all possible powers of 2 up to `n`
powers_of_two = [2**i for i in range(27) if 2**i <= n]

for weight in weights_per_bag:
    dp[weight] = 1

res = dp[-1]

for power in powers_of_two[1:]:
    if power > n:
        break

    new_numbers = [power * weight for weight in weights_per_bag if weight]
    new_dp = [0] * (n + 1)

    for ind, val in enumerate(dp[:]):
        if val:
            for num in new_numbers:
                if ind + num <= n:
                    if ind:
                        new_dp[ind + num] += val
                    else:
                        new_dp[ind + num] += 1
                else:
                    break

    if 0 in weights_per_bag:
        dp = [dp[i] + new_dp[i] for i in range(n + 1)]
        res = dp[-1]

    else:
        res += new_dp[-1]
        dp = new_dp

print(res % 1000000007)
