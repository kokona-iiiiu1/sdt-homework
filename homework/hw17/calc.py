def is_positive(n):
    return n > 0

def classify(n):
    if is_positive(n):          # ← 故意拼错：is_positve 未定义
        return "positive"
    return "non-positive"
