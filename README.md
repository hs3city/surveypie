# Ordinal-Scale-Stats-py

Python package that helps you analyze ordinal data.

## Introduction

Ordinal scale data is common. Companies and governments can quickly perform large-scale research with surveys.
Usually, a survey output is placed on the Likert scale, where answers are ordered to describe a person's feelings about the survey's topic.
A typical example of a survey is when a person is asked to agree with a statement with answers on a five-level scale:

```text
Should the law protect your personal data?

1. Strongly disagree.
2. Rather disagree.
3. I don't know.
4. Rather agree.
5. Strongly agree.
```

The order between categories makes analysis complex, and the fact that answers are polarized between opposing states. Moreover, a border between categories is subjective and depends on the person's experiences, feelings, and knowledge about a surveying topic.

Classical measurements of central tendency do not fit well with ordinal data [ADD BIBLIOGRAPHY]. We encourage you to use the `ordinal-scale-stats` package to analyze survey responses.
With `ordinal-scale-stats`, you can:

- visualize differences between surveyed groups,
- measure polarization *within* a group,
- measure polarization *between* groups,
- measure ...

## Example use case

## Setup

## Requirements

## API

## Vignettes

## Tests and Contribution

**Critical**: 
- First - CREATE YOUR OWN FORK OF THE REPOSITORY.
- Second - PULL REQUESTS ARE ALWAYS PUSHED INTO `dev` BRANCH OF THE MAIN REPOSITORY. But don't worry, even if you push it directly to `main` branch then repository admin will switch branches.

### Project setup

1. Install poetry in your system: https://python-poetry.org/docs/
2. Type `poetry install` in the package repository. You should see the new environment where you can work on your scripts. Or you can create virtualenv using pip or conda BEFORE runnig command `poetry install`, activate your environment and then run `poetry install`.
3. Install optional (`dev`) dependencies `poetry install --extras dev`

### Code

1. Use `black` and `flake8` to format and lint code, follow `PEP 8`, and write docstrings. Remember about type annotations.
2. Line length in our repository is set to 120 characters (PEP8 has 79 characters, but in our opinion it makes docstrings messy).

### Running tests

1. First, format and lint the code (in the `src` directory): `poetry run black src`, `poetry run flake8 src`.
2. When you create new functions and classes always write and run unit tests in `tests` directory, even if your code does not face users. 
3. When you debug functions, or enhance codebase always run tests when your work is done `poetry run pytest`.
4. All tests are passing? Great, it's time for Pull (Merge) Request.

### Pushing changes to repo

1. Push changes into your fork.
2. From your fork push changes into the `dev` branch. Wait till all tests are done, and then for the review. At this step some linting/code formatting/unit tests might go wrong. In this case, review doesn't start until all tests and code checks are valid, so you need to work a little bit longer with your code, and do commit with the new changes.
3. Reviewers may ask you to work on something, probably docstrings to user-facing functions or unit tests.

## Community

## Citation

```
@software{surveypie_2024,
author = {Moliński, Szymon and Jonatowska, Marta and Grabowski, Filip},
license = {MIT},
month = apr,
title = {{surveypie}},
url = {https://github.com/hs3city/surveypie},
version = {0.0.1},
year = {2024}
}
```
