# hw13：前台 / 后台 / 中断

本实例通过以下命令观察前台、后台和中断状态：

```bash
sleep 60
# 按 Ctrl-C 中断前台任务
sleep 60 &
jobs
fg
# 再按 Ctrl-C 结束任务
jobs
```

`&` 将任务放入后台，`jobs` 查看状态，`fg` 将任务拉回前台，Ctrl-C 发送 SIGINT。
