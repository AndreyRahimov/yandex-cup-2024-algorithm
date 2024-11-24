MOD = 1000000007

def count_ways(n, m, a):
    # Функция для подсчета всех возможных сумм для заданного множества степеней двойки
    def calculate_dp(powers, values):
        dp = {0: 1}  # Изначально один способ получить 0 (не брать ничего)
        for power in powers:
            new_dp = {}
            for weight, count in dp.items():
                for val in values:
                    new_weight = weight + power * val
                    if new_weight > n:
                        break  # Пропускаем веса больше n
                    if new_weight not in new_dp:
                        new_dp[new_weight] = 0
                    new_dp[new_weight] = (new_dp[new_weight] + count) % MOD
            dp = new_dp
        return dp

    # Разделяем степени двойки на две части
    powers = [2**i for i in range(27) if 2**i <= n]
    mid = len(powers) // 2
    left_powers, right_powers = powers[:mid], powers[mid:]

    # Вычисляем возможные веса для каждой части
    left_dp = calculate_dp(left_powers, a)
    right_dp = calculate_dp(right_powers, a)

    # Считаем общее число способов
    result = 0
    for left_weight, left_count in left_dp.items():
        complement = n - left_weight
        if complement in right_dp:
            result = (result + left_count * right_dp[complement]) % MOD

    return result

# Чтение данных
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))
    print(count_ways(n, m, a))
