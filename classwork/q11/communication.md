# communication.md

## Issue：空白 --name 未被拒绝，仍输出问候语
- 环境：Windows 10，Python 3.11，greetlab 0.1.0（wheel 安装）。
- 复现：`sdt-greet --name "   "`。
- 期望：视为参数无效，打印 usage 并以退出码 2 报错。
- 实际：打印 `Hello,    !` 并以 0 退出。
- 待确认：空白是否只含空格与制表符（不含换行）。

## 提交信息
标题：让空白的 --name 触发参数校验并以退出码 2 退出
正文：问题：--name 未做空白校验，错误调用被当成成功返回 0。
方案：打印前调用 p.error()，由 argparse 输出 usage 并退出 2。

## 评审意见
- [Blocking] 打印前未 strip 校验 --name，空值仍返回 0，掩盖调用错误；请改 p.error() 并补回归测试。
- [Suggestion] 校验逻辑建议封装为 _validate(name)，便于测试。
- [Nit] 提示语可补充"请传入非空姓名"。