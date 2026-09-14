import pytest
from greetlab import cli

def test_blank_name_exits_2(monkeypatch):
    monkeypatch.setattr("sys.argv", ["sdt-greet", "--name", "   "])  # 假装命令行只给了空白名字
    with pytest.raises(SystemExit) as e:     # 期望 main 以 SystemExit 结束
        cli.main()
    assert e.value.code == 2                  # 且退出码是 2