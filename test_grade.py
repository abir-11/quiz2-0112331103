from grade import get_grade


def test_grade_a():
    assert get_grade(80) == "A"


def test_grade_b():
    assert get_grade(70) == "B"


def test_grade_c():
    assert get_grade(60) == "C"


def test_grade_d():
    assert get_grade(50) == "D"


def test_grade_f():
    assert get_grade(40) == "F"