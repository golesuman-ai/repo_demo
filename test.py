import pytest

def add(x, y):
  return x + y

@pytest.mark.paramaterize("a, b, expected", 
                          [(3, 5, 8), 
                           (2, 7, 9)
                          ])
def test_add(a, b, expected):
  assert add(a, b) == expected
