import argparse  # argparse = 解析命令行参数的库


def main():  # 程序的"入口函数"
    p = argparse.ArgumentParser()  # 建一个参数解析器
    p.add_argument("--name", required=True)  # 声明要接收 --name，且必须给
    a = p.parse_args()  # 真正去读命令行参数
    if not a.name.strip():  # strip 去首尾空白；为空说明 --name 只含空白
        p.error(
            "--name 不能为空白"
        )  # p.error：argparse 打印 usage+错误，并以退出码 2 结束
    print(f"Hello, {a.name}!")  # f-string：把 a.name 的值填进字符串
