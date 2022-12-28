# Advent of Code

A repo for keeping my Advent of Code solutions in

## Local Development

-- I couldn't get just to work properly (:c so for now just use 'make')

The following [`just`](<https://just.systems/man/en/chapter_1.html>) recipes can be used to install the project for local development, and run tests, linting and formatting tools.

To install `just`, run the following command:

- ```brew install just```

### Install

To install the project, it's dependencies and [pre-commit hooks](https://pre-commit.com/), run:

- `just local`

### Test

To run the test suite, run:

- `just test`

verbosely:

- `just test-v`

To check the test coverage report, run:

- `just coverage`

### Linting and code formatting

To check the linting and code formatting, run:

- `just lint`

To fix it, run:

- `just lint-fix`
