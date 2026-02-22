# Simple Calculator Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test Cases

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("Addition test cases passed")

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 5) == 5
    print("Subtraction test cases passed")

if __name__ == "__main__":
    test_add()
    test_subtract()
