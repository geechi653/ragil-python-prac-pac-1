import io
import importlib
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_print_file_path():
    lines = get_output_lines()
    expected = "Path: C:\\new_folder\\test"
    assert lines[0] == expected, f"Expected first line to be {expected!r}, but got {lines[0]!r}"

def test_print_quoted_sentence():
    lines = get_output_lines()
    expected = 'He said, "Python is amazing!" and then paused.'
    assert lines[1] == expected, f"Expected second line to be {expected!r}, but got {lines[1]!r}"

def test_print_line1():
    lines = get_output_lines()
    expected = "Line1"
    assert lines[2] == expected, f"Expected third line to be {expected!r}, but got {lines[2]!r}"

def test_print_indented_line():
    lines = get_output_lines()
    expected = "\tLine2 indented"
    assert lines[3] == expected, f"Expected fourth line to be {expected!r}, but got {lines[3]!r}"
