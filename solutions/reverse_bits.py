def reverse_bits(n):
    reverse_val = 0
    for i in range(32):
        reverse_val = reverse_val << 1
        if n & 1 == 1:
            reverse_val |= 1
        n = n >> 1
    return reverse_val
