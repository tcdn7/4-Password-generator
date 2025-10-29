import secrets
from .charset import build_alphabet, character_classes


def _secure_shuffle(chars: list) -> None:
    for i in range(len(chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        chars[i], chars[j] = chars[j], chars[i]


def generate_password(
    length: int = 16,
    use_lower: bool = True,
    use_upper: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    exclude_lookalikes: bool = False,
    require_each_class: bool = True,
) -> str:
    if length < 1:
        raise ValueError("length must be >=1")

    classes = character_classes(
        use_lower=use_lower,
        use_upper=use_upper,
        use_digits=use_digits,
        use_symbols=use_symbols,
        exclude_lookalikes=exclude_lookalikes,
    )

    if not classes:
        raise ValueError("alphabet is empty; enable at least one character class")

    alphabet = build_alphabet(
        use_lower=use_lower,
        use_upper=use_upper,
        use_digits=use_digits,
        use_symbols=use_symbols,
        exclude_lookalikes=exclude_lookalikes,
    )

    password_chars = []

    if require_each_class:
        enabled_class_sets = list(classes.values())
        if length < len(enabled_class_sets):
            raise ValueError(
                f"length={length} is too short for {len(enabled_class_sets)} selected classes"
            )
        for cls in enabled_class_sets:
            password_chars.append(secrets.choice(cls))
    remaining = length - len(password_chars)
    for _ in range(remaining):
        password_chars.append(secrets.choice(alphabet))

    _secure_shuffle(password_chars)

    return "".join(password_chars)
