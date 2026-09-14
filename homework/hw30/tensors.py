import torch

a = torch.tensor([1, 2, 3, 4, 5, 6])
print("形状:", a.shape)          # 6 个元素 → torch.Size([6])

b = a.reshape(2, 3)              # 变成 2 行 3 列
print("reshape:\n", b)

print("逐元素 +10:", a + 10)      # 每个元素都加 10
print("求和:", a.sum().item())    # .item() 取出 Python 数字 → 21
print("第一行:", b[0])            # 索引取第 0 行