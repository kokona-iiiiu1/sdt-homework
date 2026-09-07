# hw14：后台任务 PID 与退出码

本实例使用 `$!` 自动取得后台任务 PID，并检查 SIGTERM 对应的退出码：

```bash
sleep 120 &
PID=$!
echo "PID=$PID"
kill "$PID"
wait "$PID"
echo "退出码=$?"
```

默认 `kill` 发送 SIGTERM（信号编号 15），因此被该信号终止后的退出码为 `128 + 15 = 143`。
