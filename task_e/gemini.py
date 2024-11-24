def solve():
    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))

    mod = 1000000007

    max_power = 0
    while (1 << max_power) <= n:
        max_power += 1
    max_power = min(max_power, 27)

    def calculate_dp(start_power, end_power, prev_dp=None):
        dp = {}
        dp[0] = 1

        for power in range(start_power, end_power):
            new_dp = {}
            for prev_sum in dp:
                for count in a:
                    new_sum = prev_sum + count * (1 << power)
                    if new_sum <= n:
                        if prev_dp is not None and power == start_power and count == 0 and prev_sum > 0 and (
                                n - new_sum) in prev_dp:
                            continue
                        if prev_dp is not None and power == start_power and (n - new_sum) not in prev_dp:
                            continue

                        new_dp[new_sum] = (new_dp.get(new_sum, 0) + dp[prev_sum]) % mod
            dp = new_dp
        return dp

    mid_power = max_power // 2

    left_dp = calculate_dp(0, mid_power)
    right_dp = calculate_dp(mid_power, max_power, left_dp)

    ans = 0
    for k in range(max_power + 1):
        current_dp = right_dp if k > mid_power else left_dp

        if n in current_dp:
            ans = (ans + current_dp[n]) % mod

    print(ans)


solve()