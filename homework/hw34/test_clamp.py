import pytest

from clamp import clamp


def test_below():
    assert clamp(-5, 0, 10) == 0      # 低于下界 → 被抬到 lo


def test_above():
    assert clamp(99, 0, 10) == 10     # 高于上界 → 被压到 hi


def test_inside():
    assert clamp(4, 0, 10) == 4       # 区间内 → 原样返回


def test_bad_range():
    with pytest.raises(ValueError):   # 非法区间 → 应抛 ValueError
        clamp(1, 10, 0)
