import io
import importlib
from contextlib import redirect_stdout

def get_output_lines():
    import solution
    f = io.StringIO()
    with redirect_stdout(f):
        importlib.reload(solution)
    return f.getvalue().splitlines()

def test_addition():
    lines = get_output_lines()
    expected = "19"
    assert lines[0] == expected, f"Expected first line (addition) to be {expected!r}, but got {lines[0]!r}"

def test_subtraction():
    lines = get_output_lines()
    expected = "11"
    assert lines[1] == expected, f"Expected second line (subtraction) to be {expected!r}, but got {lines[1]!r}"

def test_multiplication():
    lines = get_output_lines()
    expected = "60"
    assert lines[2] == expected, f"Expected third line (multiplication) to be {expected!r}, but got {lines[2]!r}"

def test_division():
    lines = get_output_lines()
    expected = "3.75"
    assert lines[3] == expected, f"Expected fourth line (division) to be {expected!r}, but got {lines[3]!r}"

def test_floor_division():
    lines = get_output_lines()
    expected = "3"
    assert lines[4] == expected, f"Expected fifth line (floor division) to be {expected!r}, but got {lines[4]!r}"

def test_modulus():
    lines = get_output_lines()
    expected = "3"
    assert lines[5] == expected, f"Expected sixth line (modulus) to be {expected!r}, but got {lines[5]!r}"

def test_exponentiation():
    lines = get_output_lines()
    expected = "50625"
    assert lines[6] == expected, f"Expected seventh line (exponentiation) to be {expected!r}, but got {lines[6]!r}"

def test_operator_precedence():
    lines = get_output_lines()
    expected = "20"
    assert lines[7] == expected, f"Expected eighth line (operator precedence) to be {expected!r}, but got {lines[7]!r}"
