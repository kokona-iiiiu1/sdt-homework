from calc import classify
def test_positive():
    assert classify(5) == "positive"
def test_zero():
    assert classify(0) == "non-positive"
def test_negative():
    assert classify(-3) == "non-positive"