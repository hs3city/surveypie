# Tests

Every user-facing function, and functions that are abstractions over some equations or data processing steps should be tested. We define two types of tests:

1. Unit tests. Unit tests should cover almost whole codebase.
2. Integration tests. Our integration tests are `special` because we treat notebooks as integration tests that users might copy & paste into their workflows! Only the most relevant functions and classes fall into this category of tests.

## Unit tests

- First of all, it doesn't matter if you write tests before or after writing your function.
- Tests must be present if you make PR into the `dev` branch of the repository.
- For mathematical functions:
  - define limits when function might fall and test against those limits,
  - at least one basic test must pick random numbers,
  - be careful with comparisons to floating-point numbers.
- Classes with multiple methods should have all public methods tested, it is recommended to test also private methods.
- Data containers and functions processing array-like structures or dict-like structures should be tested against multiple data structures (array-like: lists, tuples, numpy arrays; dict-like: dictionaries, pandas Series, pandas DataFrames).
- Functions and classes throwing exceptions should have tests covering those exceptions (`with pytest.raises ...`).
- Unit tests are obligatory.
- The simplest way to write unit test is to copy & paste existing test, and tweak it into your code.
- You can use AI for writing unit tests, but remember about the golden rule: use it or lose it. Yes, it's about your brain. And check AI-generated tests.

## Integration tests

Integration tests are also demonstrations what can be achieved with the package. That's why we write integration tests in Jupyter Notebooks. They follow a specific pattern, described in the file about notebooks structure.
By testing those files we mean:
- running ALL notebooks after code changes to check if there are breaking changes that have slipped through unit tests
- checking outputs in the notebook, validating scientific software with graphs and plots gives us additional opportunity for finding logical errors (e.g. returned distribution plot shows nothing similar to expected distribution)