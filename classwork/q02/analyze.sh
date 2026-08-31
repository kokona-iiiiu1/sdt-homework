#!/bin/bash
set -euo pipefail

if [ $# -ne 1 ]; then
    echo "用法: $0 <CSV文件路径>" >&2
    exit 1
fi

CSV="$1"

if [ ! -f "$CSV" ]; then
    echo "错误: 文件 $CSV 不存在" >&2
    exit 1
fi

awk -F, 'NR>1 && $4 ~ /^5/ {print $3}' "$CSV" \
  | sort \
  | uniq -c \
  | sort -k1,1nr -k2,2 \
  | head -2 \
  | awk '{print $2, $1}'

awk -F, 'NR>1 {sum += $5; count++} END {printf "%.2f\n", sum/count}' "$CSV"