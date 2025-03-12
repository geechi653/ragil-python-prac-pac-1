import io
import importlib
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_print_with_parentheses():
    lines = get_output_lines()
    expected = "Result with parentheses: 18.75"
    assert lines[0] == expected, f"Expected first line to be {expected!r}, but got {lines[0]!r}"

def test_print_without_parentheses():
    lines = get_output_lines()
    expected = "Result without parentheses: 49.25"
    assert lines[1] == expected, f"Expected second line to be {expected!r}, but got {lines[1]!r}"
