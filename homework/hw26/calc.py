def safe_div(a, b):
    if b == 0:
        raise ValueError("b 不能为 0")
    return a / b