# Advent of Code


My repository for Advent of Code 2022 solutions.


# Instructions

Requires

- Python 3.8
- [Poetry](https://github.com/python-poetry/poetry)
- [Just](https://github.com/casey/just)

## 1. Install dependencies

Using `just`:

```shell
just install
```

## 2. Add inputs and test inputs

Edit `../day01/tests/test_input.txt` and `../day01/input.txt`.

## 3. Write some code

Start at `../day01/solution1.py`.

## 4. Run the tests

To run the tests for only the first solution of day 1:

```shell
just test 1 1
```

To run for both solutions:

```shell
just test 1
```

## 5. Run the solution

To run the solution for day 1 part 1:

```shell
just day 1 1
```

## 6. Other useful commands

### Linting

```shell
just flake8
just black
just isort
```

Or run all three via

```shell
just lint
```

### Automated linting fixes

```shell
just black-fix
just isort-fix
```

Or run both via

```shell
just lint-fix
```

### Other

Static checking via `bandit`

```shell
just bandit
```

Check dependencies against the `safety` database of known vulnerabilities

```shell
just safety
```
