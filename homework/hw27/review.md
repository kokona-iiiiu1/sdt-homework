# 评审结论
## 该保留
- calc.py 增加 b==0 → raise ValueError：正是要实现的功能，保留。
## 该撤销
1. [Blocking] test_calc.py 把 test_zero 改成 pass —— 偷偷弱化了测试，等于把考卷废了；
   测试文件不应被改动，应恢复原断言。
2. [Suggestion] calc.py 新增 unused_helper() —— 与本任务无关的改动，属越界，应删除。