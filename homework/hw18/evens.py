def count_evens(nums):
    cnt = 0
    for x in nums:
        if x % 2 == 0:
            cnt += 1
    return cnt

print(count_evens([1, 2, 3, 4, 5, 6]))
