def count_bits(x:int) -> int:
    num_bits = 0
    while x: 
        num_bits += x & 1
        x >>= 1
        print(x)
    return num_bits

arg = 10
res = count_bits(1010101)
print(res)


def bit_diff(y):
    v = 0
    for i in range(len(y)):
        v = v^y[i]
        print(v)
    return v

