def clamp(x, lo, hi):
    if lo > hi:
        raise ValueError("lo 不能大于 hi")
    return max(lo, min(x, hi))
