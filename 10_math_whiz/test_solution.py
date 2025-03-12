import io
import importlib
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_print_absolute_value():
    lines = get_output_lines()
    expected = "50"
    assert lines[0] == expected, f"Expected first line (absolute value) to be {expected!r}, but got {lines[0]!r}"

def test_print_rounded_value():
    lines = get_output_lines()
    expected = "3.14"
    assert lines[1] == expected, f"Expected second line (rounded value) to be {expected!r}, but got {lines[1]!r}"

def test_print_maximum():
    lines = get_output_lines()
    expected = "33"
    assert lines[2] == expected, f"Expected third line (maximum) to be {expected!r}, but got {lines[2]!r}"

def test_print_minimum():
    lines = get_output_lines()
    expected = "-90"
    assert lines[3] == expected, f"Expected fourth line (minimum) to be {expected!r}, but got {lines[3]!r}"

def test_print_sum():
    lines = get_output_lines()
    expected = "-28"
    assert lines[4] == expected, f"Expected fifth line (sum) to be {expected!r}, but got {lines[4]!r}"
