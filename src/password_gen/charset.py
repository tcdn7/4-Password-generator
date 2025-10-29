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
