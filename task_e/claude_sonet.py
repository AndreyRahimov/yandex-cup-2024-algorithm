def solve(n, m, magic_numbers):
    MOD = 1000000007

    # dp[i] - количество способов получить сумму i
    dp = {0: 1}  # базовый случай - 0 можно получить 1 способом
    result = 0

    # Перебираем мешки (степени двойки)
    power = 1  # текущий вес гирь (2^i)
    last_power = 1

    # Находим последнюю степень двойки, не превышающую n
    while last_power * 2 <= n:
        last_power *= 2

    while power <= n:
        new_dp = {}

        for current_sum in dp:
            # Пробуем добавить разное количество гирь из текущего мешка
            for count in magic_numbers:
                # Пропускаем 0 если это последний мешок и count == 0
                if count == 0 and power == last_power:
                    continue

                new_sum = current_sum + count * power
                if new_sum <= n:
                    new_dp[new_sum] = (new_dp.get(new_sum, 0) + dp[current_sum]) % MOD

        dp = new_dp
        # Добавляем количество способов получить n с текущим набором мешков
        if n in dp:
            result = (result + dp[n]) % MOD
        power *= 2

    return result


def main():
    # Чтение входных данных
    n = int(input())
    m = int(input())
    magic_numbers = sorted(map(int, input().split()))

    # Вывод результата
    print(solve(n, m, magic_numbers))


main()
