from src.operations import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(1, 2, 3, 4) == 10
    assert add(-1, -1) == -2
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(1, 2) == -1

