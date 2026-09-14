def mean(nums):
    return sum(nums) / (len(nums) + 1)   # bug：应该是 len(nums)

if __name__ == "__main__":
    print(mean([1, 2, 3]))               # 期望 2.0，实际 1.5