import argparse
from .generator import generate_password


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="password-gen",
        description="Secure password generator powered by Python's secrets module.",
    )

    parser.add_argument(
        "--length", type=int, default=16, help="Password length (default: 16)"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="How many passwords to generate (default: 1)",
    )

    parser.add_argument(
        "--lower",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Use lowercase letters",
    )
    parser.add_argument(
        "--upper",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Use uppercase letters",
    )
    parser.add_argument(
        "--digits",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Use digits",
    )
    parser.add_argument(
        "--symbols",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Use symbols",
    )

    parser.add_argument(
        "--exclude-lookalikes", action="store_true", help="Exclude O,0,l,1,I"
    )
    parser.add_argument(
        "--require-each-class",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Require at least one character from each selected class",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    for _ in range(args.count):
        pwd = generate_password(
            length=args.length,
            use_lower=args.lower,
            use_upper=args.upper,
            use_digits=args.digits,
            use_symbols=args.symbols,
            exclude_lookalikes=args.exclude_lookalikes,
            require_each_class=args.require_each_class,
        )
        print(pwd)


if __name__ == "__main__":
    main()
