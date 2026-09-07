#!/usr/bin/env bash
trap 'echo BYE >> clean.log; exit 0' INT TERM   # 收到 INT/TERM → 写日志再退出
n=0
while true; do
  echo "$n"
  sleep 1
done
