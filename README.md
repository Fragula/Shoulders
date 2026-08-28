# Shoulders

# THE README & PYPROJECT FILES ARE KIND OUTDATED. IT ONLY BE UPDATED WHEN V0.2 COME OUT.

> If I have seen further, it is by standing on the shoulders of giants.

Shoulders is an open-source project focused on aiding engineers.

The philosophy of the library is:

> Trying to make engineers' lives easier.

## Current status

### v0.1

> The first version focuses on dimensional analysis.

```pythongit status
from shoulders.fundamental import LENGTH, MASS, TIME

# Dimension order:
# (T, L, M, I, Θ, N, J)
# LENGTH = (0, 1, 0, 0, 0, 0, 0)

velocity = LENGTH / TIME
acceleration = LENGTH / TIME**2
force = MASS * acceleration
```
## Project structure

```md
shoulders/
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── src/
│   └── shoulders/
│       ├── __init__.py
│       ├── derived.py
│       ├── dimension.py
│       ├── fundamental.py
│       └── symbol.py
└── tests/
    └── test_derived.py
    └── test_dimension.py
    └── test_fundamental.py
    └── test_symbol.py
```

## Development

Clone the repo and install it in editable mode:

```bash
python -m pip install -e .
```

Run the test suite:

```bash
python -m pytest
```

## Future

The project is expected to grow toward a broader 
scientific and engineering computing library.

## License

Shoulders is free software licensed under the
GNU Lesser General Public License v3.0 or later
(LGPL-3.0-or-later).
