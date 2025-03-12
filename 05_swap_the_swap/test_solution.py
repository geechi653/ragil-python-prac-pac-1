import io
import importlib
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_print_before_swap():
    lines = get_output_lines()
    expected = "Before swap: x = 10, y = 20"
    assert lines[0] == expected, f"Expected first line to be {expected!r}, but got {lines[0]!r}"

def test_print_after_swap():
    lines = get_output_lines()
    expected = "After swap: x = 20, y = 10"
    assert lines[1] == expected, f"Expected second line to be {expected!r}, but got {lines[1]!r}"
