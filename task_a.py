import math


def lcm(x, y):
	return x * y // math.gcd(x, y)


def count_divisible(x, lcm_ab, lcm_ac, lcm_bc, lcm_abc):
	is_divided_by_ab = x // lcm_ab
	is_divided_by_ac = x // lcm_ac
	is_divided_by_bc = x // lcm_bc
	is_divided_by_abc = x // lcm_abc

	return (is_divided_by_ab + is_divided_by_ac + is_divided_by_bc) - (3 * is_divided_by_abc)


def find_nth_number(a, b, c, n):
	lcm_ab, lcm_ac, lcm_bc, lcm_abc = lcm(a, b), lcm(a, c), lcm(b, c), lcm(a, lcm(b, c))

	left, right = 1, 10 ** 18 + 1

	while left < right:
		mid = (left + right) // 2

		if count_divisible(mid, lcm_ab, lcm_ac, lcm_bc, lcm_abc) < n:
			left = mid + 1

			if left > 10 ** 18:
				return -1

		else:
			right = mid

	return left


a, b, c = map(int, input().split())
n = int(input())

print(find_nth_number(a, b, c, n))
