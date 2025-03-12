import io
import importlib
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_print_square_root():
    lines = get_output_lines()
    expected = "7.0"
    assert lines[0] == expected, f"Expected first line (square root) to be {expected!r}, but got {lines[0]!r}"

def test_print_floor():
    lines = get_output_lines()
    expected = "3"
    assert lines[1] == expected, f"Expected second line (floor) to be {expected!r}, but got {lines[1]!r}"

def test_print_ceiling():
    lines = get_output_lines()
    expected = "4"
    assert lines[2] == expected, f"Expected third line (ceiling) to be {expected!r}, but got {lines[2]!r}"

def test_print_power():
    lines = get_output_lines()
    expected = "32.0"
    assert lines[3] == expected, f"Expected fourth line (power) to be {expected!r}, but got {lines[3]!r}"
