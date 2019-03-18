def parity_bit(sbin):
    return sum([int(c) for c in sbin.replace("0b", "")]) % 2