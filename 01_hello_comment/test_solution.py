import io
import importlib
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_print_hello_world():
    lines = get_output_lines()
    expected = "\"That's Hello, World!\""
    assert lines[0] == expected, f"Expected first line to be {expected!r}, but got {lines[0]!r}"

def test_print_digit():
    lines = get_output_lines()
    expected = "100"
    assert lines[1] == expected, f"Expected second line to be {expected!r}, but got {lines[1]!r}"

def test_print_math_expression():
    lines = get_output_lines()
    expected = "10"
    assert lines[2] == expected, f"Expected third line to be {expected!r}, but got {lines[2]!r}"

def test_comment_presence():
    with open('solution.py', 'r', encoding='utf-8') as f:
        content = f.read()
    assert any(line.strip().startswith("#") for line in content.splitlines()), \
           "The solution.py file should contain at least one single-line comment."