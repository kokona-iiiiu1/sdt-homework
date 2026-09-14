import torch

x = torch.tensor(0.0, requires_grad=True)   # 要求对 x 记录梯度
lr = 0.1
for i in range(20):
    loss = (x - 3) ** 2                     # 目标：让 x 接近 3
    loss.backward()                         # 自动算 d(loss)/dx
    with torch.no_grad():                   # 更新时不要被记录进计算图
        x -= lr * x.grad                    # 梯度下降一步
        x.grad.zero_()                      # 清空梯度，防止累加
    if i % 5 == 0:
        print(f"step {i}: x={x.item():.3f} loss={loss.item():.3f}")

print("final x =", round(x.item(), 3))