import io
import importlib
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_print_integer():
    lines = get_output_lines()
    expected = "100 <class 'int'>"
    assert lines[0] == expected, f"Expected first line to be {expected!r}, but got {lines[0]!r}"

def test_print_float():
    lines = get_output_lines()
    expected = "3.14 <class 'float'>"
    assert lines[1] == expected, f"Expected second line to be {expected!r}, but got {lines[1]!r}"

def test_print_complex():
    lines = get_output_lines()
    expected = "(3+4j) <class 'complex'>"
    assert lines[2] == expected, f"Expected third line to be {expected!r}, but got {lines[2]!r}"

def test_print_boolean():
    lines = get_output_lines()
    expected = "True <class 'bool'>"
    assert lines[3] == expected, f"Expected fourth line to be {expected!r}, but got {lines[3]!r}"

def test_print_float_precision():
    lines = get_output_lines()
    expected = "0.1 + 0.2 == 0.3: False"
    assert lines[4] == expected, f"Expected fifth line to be {expected!r}, but got {lines[4]!r}"
