def big_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

print(big_sum(10_000_000))     # 求 1..1000万 的和
