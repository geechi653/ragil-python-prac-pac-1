import io 
import importlib
from contextlib import redirect_stdout
import solution

def get_output_lines():
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
        return f.getvalue().splitlines()

def test_print_greeting_line():
    lines = get_output_lines()
    expected = "Good Morning-Python-Programmers!!!"
    assert lines[0] == expected, f"Expected first line to be {expected!r}, but got {lines[0]!r}"

def test_print_fstring_greeting():
    lines = get_output_lines()
    expected = "Hello, my name is Alice and I love Python."
    assert lines[1] == expected, f"Expected second line to be {expected!r}, but got {lines[1]!r}"
