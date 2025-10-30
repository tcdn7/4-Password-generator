import pytest
from password_gen.generator import generate_password
from password_gen.charset import LOWER, UPPER, DIGITS, SYMBOLS, LOOKALIKES


def test_length_and_charset_basic():
    p = generate_password(length=20)
    assert len(p) == 20
    allowed = set(LOWER + UPPER + DIGITS + SYMBOLS)
    assert all(ch in allowed for ch in p)


def test_each_class_requirement():
    p = generate_password(
        length=12,
        use_lower=True,
        use_upper=True,
        use_digits=True,
        use_symbols=False,
    )
    assert any(ch in LOWER for ch in p)
    assert any(ch in UPPER for ch in p)
    assert any(ch in DIGITS for ch in p)


def test_exclude_lookalikes():
    p = generate_password(length=40, exclude_lookalikes=True)
    assert all(ch not in LOOKALIKES for ch in p)


def test_value_error_when_length_too_short():
    with pytest.raises(ValueError):
        generate_password(
            length=2,
            use_lower=True,
            use_upper=True,
            use_digits=True,
            require_each_class=True,
        )


def test_disable_requirement_allows_short_length():
    p = generate_password(
        length=2,
        use_lower=True,
        use_upper=True,
        use_digits=True,
        require_each_class=False,
    )
    assert len(p) == 2
