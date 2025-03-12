import io
import importlib
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_print_initial_full_name():
    lines = get_output_lines()
    expected = "Initial full_name: None"
    assert lines[0] == expected, f"Expected first line to be {expected!r}, but got {lines[0]!r}"

def test_print_updated_full_name():
    lines = get_output_lines()
    expected = "Updated full_name: Bob Dylan"
    assert lines[1] == expected, f"Expected second line to be {expected!r}, but got {lines[1]!r}"
