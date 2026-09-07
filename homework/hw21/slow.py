import random
random.seed(1)

def single_sum(a):          # O(n)：只扫一遍
    return sum(a)

def double_sum(a):          # O(n^2)：两层循环
    total = 0
    for i in a:
        for j in a:
            total += i * j
    return total

nums = [random.randint(1, 100) for _ in range(500)]
print(single_sum(nums))
print(double_sum(nums))
