import io
import importlib
import ast
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_random_float():
    lines = get_output_lines()
    try:
        value = float(lines[0])
    except ValueError:
        assert False, f"First output is not a float: {lines[0]!r}"
    assert 0 <= value <= 1, f"Expected first output between 0 and 1, but got {value}"

def test_random_int():
    lines = get_output_lines()
    try:
        value = int(lines[1])
    except ValueError:
        assert False, f"Second output is not an integer: {lines[1]!r}"
    assert 1 <= value <= 50, f"Expected second output between 1 and 50, but got {value}"

def test_random_color():
    lines = get_output_lines()
    valid_colors = {"red", "blue", "green", "black", "yellow"}
    assert lines[2] in valid_colors, f"Third output {lines[2]!r} is not one of {valid_colors}"

def test_shuffled_fruits():
    lines = get_output_lines()
    try:
        fruits = ast.literal_eval(lines[3])
    except Exception:
        assert False, f"Fourth output is not a valid list: {lines[3]!r}"
    expected_fruits = {"apple", "banana", "plum", "orange"}
    assert set(fruits) == expected_fruits, f"Expected fruits {expected_fruits}, but got {set(fruits)}"
