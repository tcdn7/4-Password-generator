import secrets
from .charset import build_alphabet


def generate_password(
    length: int = 16,
    use_lower: bool = True,
    use_upper: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    exclude_lookalikes: bool = False,
    require_each_type: bool = True,
) -> str:
    if length < 1:
        raise ValueError("length must be >=1")
    alphabet = build_alphabet(
        use_lower=use_lower,
        use_upper=use_upper,
        use_digits=use_digits,
        use_symbols=use_symbols,
        exclude_lookalikes=exclude_lookalikes,
    )
    if not alphabet:
        raise ValueError("alphabet is empty; enable at least one character class")

    return "".join(secrets.choice(alphabet) for _ in range(length))
