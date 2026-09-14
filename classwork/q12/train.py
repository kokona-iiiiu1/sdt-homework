import torch
from torch import nn
torch.manual_seed(20260907)
x = torch.linspace(-1, 1, 101).reshape(-1, 1)
y = 3 * x - 1
model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)
for _ in range(200):          # 重复 200 轮
    pred = model(x)           # ① 前向：用当前 w,b 对全部 x 做预测
    loss = loss_fn(pred, y)   # ② 算损失：预测离真实差多少
    opt.zero_grad()           # ③ 清空上次累计的梯度（否则会叠加）
    loss.backward()           # ④ 反向传播：自动算出"要降 loss，w,b 各该往哪挪"
    opt.step()                # ⑤ 更新参数：真的往那个方向挪一小步
model.eval()                       # 进入"评估模式"（本例无 dropout 等，主要是规范）
with torch.no_grad():              # 评估时不需要算梯度，省内存、也避免误改参数
    final_loss = loss_fn(model(x), y)
print("final loss =", final_loss.item())
print("weight =", model.weight.item())
print("bias =", model.bias.item())
# TODO：清空梯度、反向传播、更新参数
# TODO：进入评估模式并在 no_grad 中打印最终损失、weight 和 bias