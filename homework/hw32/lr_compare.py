import torch
from torch import nn

def train(lr):
    torch.manual_seed(0)                    # 固定种子，保证三次起点一致、可比
    x = torch.linspace(-1, 1, 101).reshape(-1, 1)
    y = 3 * x - 1
    model = nn.Linear(1, 1)
    loss_fn = nn.MSELoss()
    opt = torch.optim.SGD(model.parameters(), lr=lr)
    for _ in range(200):
        opt.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward()
        opt.step()
    return loss.item()

for lr in (0.01, 0.1, 1.0):
    print(f"lr={lr}: final loss = {train(lr):.6f}")