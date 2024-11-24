def generate_hamming_code(data_bits: int) -> list[int]:
    code = [0] * 15
    data_positions = [i for i in range(15) if not (i & (i + 1)) == 0]
    # Assign data bits to their positions
    for i, pos in zip(range(4, 15), data_positions):
        code[pos] = (data_bits >> (14 - i)) & 1

    return code


print(generate_hamming_code(2024))
