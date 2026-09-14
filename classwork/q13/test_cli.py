import pytest

from greetlab import cli


def test_normal_name_prints_greeting(capsys, monkeypatch):
    monkeypatch.setattr("sys.argv", ["sdt-greet", "--name", "姜又萌"])
    cli.main()
    assert capsys.readouterr().out == "Hello, 姜又萌!\n"


def test_blank_name_exits_2(monkeypatch):
    monkeypatch.setattr("sys.argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as e:
        cli.main()
    assert e.value.code == 2
