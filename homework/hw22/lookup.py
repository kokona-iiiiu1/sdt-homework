import random, time
random.seed(3)
N = 30000
pool = list(range(N))              # 一份数据，先存成 list
as_set = set(pool)                 # 同样内容再存成 set
queries = [random.randint(0, N * 2) for _ in range(1500)]  # 1500 次查询

def count_hits(container):
    hit = 0
    for q in queries:
        if q in container:
            hit += 1
    return hit

t0 = time.perf_counter(); hits1 = count_hits(pool);   t1 = time.perf_counter()
t2 = time.perf_counter(); hits2 = count_hits(as_set); t3 = time.perf_counter()

dt_list = t1 - t0
dt_set  = t3 - t2
print("命中数 list=", hits1, " set=", hits2, "（应相等）")
print(f"list 查询耗时: {dt_list:.4f}s")
print(f"set  查询耗时: {dt_set:.4f}s")
print(f"加速比 = {dt_list / dt_set:.1f} 倍")
