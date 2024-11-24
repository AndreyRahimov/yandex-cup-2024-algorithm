def generate_hamming_code(data_bits: int) -> list[int]:
    code = [0] * 15
    data_positions = [i for i in range(15) if not (i & (i + 1)) == 0]
    # Assign data bits to their positions
    for i, pos in zip(range(4, 15), data_positions):
        code[pos] = (data_bits >> (14 - i)) & 1
    # Calculate parity bits
    for p in [0, 1, 3, 7]:
        parity = 0
        for i in range(15):
            if (i + 1) & (1 << p):
                parity ^= code[i]
        code[p] = parity
    return code
