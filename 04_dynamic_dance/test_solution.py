import io
import importlib
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_print_integer_type():
    lines = get_output_lines()
    expected = "100 <class 'int'>"
    assert lines[0] == expected, f"Expected first line to be {expected!r}, but got {lines[0]!r}"

def test_print_string_type():
    lines = get_output_lines()
    expected = "Hello <class 'str'>"
    assert lines[1] == expected, f"Expected second line to be {expected!r}, but got {lines[1]!r}"

def test_print_boolean_type():
    lines = get_output_lines()
    expected = "True <class 'bool'>"
    assert lines[2] == expected, f"Expected third line to be {expected!r}, but got {lines[2]!r}"
