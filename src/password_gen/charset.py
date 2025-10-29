LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+[]{}|;:',.<>?/"

LOOKALIKES = set("O0l1I")


def build_alphabet(
    use_lower=True,
    use_upper=True,
    use_digits=True,
    use_symbols=True,
    exclude_lookalikes=False,
):
    alphabet = ""
    if use_lower:
        alphabet += LOWER
    if use_upper:
        alphabet += UPPER
    if use_digits:
        alphabet += DIGITS
    if use_symbols:
        alphabet += SYMBOLS

    if exclude_lookalikes:
        alphabet = "".join(ch for ch in alphabet if ch not in LOOKALIKES)

    return alphabet


def character_classes(
    use_lower=True,
    use_upper=True,
    use_digits=True,
    use_symbols=True,
    exclude_lookalikes=False,
):
    def _maybe_exclude(s: str) -> str:
        return (
            "".join(ch for ch in s if ch not in LOOKALIKES) if exclude_lookalikes else s
        )

    classes = {}
    if use_lower:
        classes["lower"] = _maybe_exclude(LOWER)
    if use_upper:
        classes["upper"] = _maybe_exclude(UPPER)
    if use_digits:
        classes["digits"] = _maybe_exclude(DIGITS)
    if use_symbols:
        classes["symbols"] = _maybe_exclude(SYMBOLS)

    classes = {k: v for k, v in classes.items() if v}
    return classes
