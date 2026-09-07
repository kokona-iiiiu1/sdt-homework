def sum_squares(n):
    total = 0
    for i in range(n+1):        # bug：range(n) = 0..n-1，漏了 n 还加了 0
        total += i * i
    return total

print(sum_squares(3))         # 期望 1+4+9=14，但输出 5 → 错！
