import io
import importlib
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_print_single_quotes():
    lines = get_output_lines()
    expected = "Single quotes: I'm in single quotes."
    assert lines[0] == expected, f"Expected first line to be {expected!r}, but got {lines[0]!r}"

def test_print_double_quotes():
    lines = get_output_lines()
    expected = "Double quotes: I'm in double quotes."
    assert lines[1] == expected, f"Expected second line to be {expected!r}, but got {lines[1]!r}"

def test_print_triple_quotes():
    lines = get_output_lines()
    expected = "Triple quotes: This is a multi-line string."
    assert lines[2] == expected, f"Expected third line to be {expected!r}, but got {lines[2]!r}"

def test_print_raw_string():
    lines = get_output_lines()
    expected = "Raw string: C:\\Users\\User\\Documents"
    assert lines[3] == expected, f"Expected fourth line to be {expected!r}, but got {lines[3]!r}"

def test_print_constructor_string():
    lines = get_output_lines()
    expected = "Constructor string: New String Here"
    assert lines[4] == expected, f"Expected fifth line to be {expected!r}, but got {lines[4]!r}"
