from um import count

def test_function():
      assert count("um") == 1
      assert count("yummy") == 0

def test_case():
      assert count("Um Um") == 2

def test_character():
      assert count("um?") == 1