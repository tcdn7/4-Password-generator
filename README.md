# 🔐 Password Generator

A secure, flexible, and easy-to-use password generator built in Python using the `secrets` module for cryptographic-grade randomness.

---

## 🚀 Features

✅ Generate strong random passwords  
✅ Adjustable length and character types  
✅ Option to exclude look-alike characters (O, 0, l, 1, I)  
✅ Ensures each selected class (lower/upper/digit/symbol) appears at least once  
✅ Fully tested with `pytest`  
✅ CLI and Python module support

---

## 📦 Installation

Clone this repository and install it in editable (development) mode:

```bash
git clone https://github.com/tcdn7/4-Password-generator.git
cd 4-password-generator
pip install -e .


🧠 Usage
🔸 From command line

# Generate one 16-character password
password-gen --length 16

# Generate five 20-character passwords excluding lookalikes
password-gen --length 20 --count 5 --exclude-lookalikes

# Only lowercase and digits, no symbols or uppercase
password-gen --no-upper --no-symbols

# Allow short password without class enforcement
password-gen --length 6 --no-require-each-class


🔸 From Python code

from password_gen.generator import generate_password

p = generate_password(length=16, exclude_lookalikes=True)
print(p)


🔸 As a module

python -m password_gen --length 20


🧪 Tests

All functionalities are covered with pytest:
pytest -v

Expected output:
5 passed in <0.1s>


🧰 Project Structure

```

password-generator/
├─ src/
│  └─ password_gen/
│     ├─ __init__.py
│     ├─ __main__.py
│     ├─ charset.py
│     ├─ cli.py
│     └─ generator.py
├─ tests/
│  ├─ conftest.py
│  └─ test_generator.py
├─ pyproject.toml
└─ README.md
```

🧑‍💻 Development Notes

- Built with Python 3.12

- Uses secrets for cryptographic randomness (more secure than random)

- Packaged with PEP 621 (pyproject.toml) structure

- Supports editable install, pytest, and argparse CLI


🏷️ Version

v0.1.0 – Initial release


👤 Author
Tacdin Özmen
💻 [GitHub Profile](https://github.com/tcdn7)