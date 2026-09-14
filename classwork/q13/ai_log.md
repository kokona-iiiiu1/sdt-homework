# AI 修复记录
1. 提示：让 main 在 --name 只含空白时以 SystemExit(2) 结束；不改测试；用 pytest 验证。
2. 智能体改动：src/greetlab/cli.py 增加空白校验，空白时调用 p.error()。
3. 人工验证：检查 diff 仅改 cli.py 无越界；pytest 通过（1 passed，退出码 2 成立）。
