# Code linting and formatting

We use `black` for code formatting and `flake8` as a code linter. When you push a PR into the core repository then both services are automatically invoked by GitHub Actions. If everything passes, your code is formatted properly, and it has valid structure, then it's great! But sometimes `black` or `flake8` validation might block merging.
That's why you should run both on your local machine BEFORE you make a PR. You will know faster what's wrong with the code.

## `black`

`poetry run black src`

### Sample output - correct

```shell
All done! ✨ 🍰 ✨
7 files left unchanged.
```

### Sample output - code has been changed

```shell
reformatted .../src/surveypie/allison_foster.py

All done! ✨ 🍰 ✨
1 file reformatted, 6 files left unchanged.

```

## `flake8`

`poetry run flake8 src`

### Sample output - wrong structure, unused import

```shell
src/surveypie/allison_foster.py:16:1: F401 'uuid' imported but unused

```
