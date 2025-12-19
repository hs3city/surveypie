# Tests

Every user-facing function, and functions that are abstractions over some equations or data processing steps should be tested. We define two types of tests:

1. Unit tests. Unit tests should cover almost whole codebase.
2. Integration tests. Our integration tests are `special` because we treat notebooks as integration tests that users might copy & paste into their workflows! Only the most relevant functions and classes fall into this category of tests.

## Unit test

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
- 