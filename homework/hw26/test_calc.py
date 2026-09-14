import pytest
from calc import safe_div

def test_normal():
    assert safe_div(6, 3) == 2

def test_zero():
    with pytest.raises(ValueError):     # 期望抛 ValueError（不是 ZeroDivisionError）
        safe_div(1, 0)