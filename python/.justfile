RED := '\033[0;31m'
RESET := '\033[0m'

@_default:
  just --list

_echo_err +msg:
  #!/usr/bin/env bash
  echo -e >&2 "{{ RED }}ERROR{{ RESET }}: {{ msg }}"

# Install dependencies
install:
  poetry install

_get_day d:
  #!/usr/bin/env bash
  [[ ! "{{ d }}" =~ ^(0?[1-9]|1[0-9]|2[0-5])$ ]] && just _echo_err "Invalid day: {{ d }}" && exit
  DAY=$([[ {{ d }} =~ ^[1-9]$ ]] && echo "0{{ d }}" || echo "{{ d }}")
  [[ ! -d "day${DAY}" ]] && just _echo_err "Dir does not exist: day${DAY}/" && exit

  echo "$DAY"

# Execute specified solution for the given day
day d s="all":
  #!/usr/bin/env bash
  DAY="$(just _get_day {{ d }})" && [[ -z "$DAY" ]] && exit

  if [[ "{{ s }}" = "all" ]]; then
    echo "Solution 1 for day $DAY..."
    poetry run python -m day${DAY}.solution1

    echo -e "\nSolution 2 for day $DAY..."
    poetry run python -m day${DAY}.solution2
  else
    [[ ! "{{ s }}" =~ ^[1-2]$ ]] && just _echo_err "Invalid solution number: {{ s }}" && exit

    echo "Solution {{ s }} for day $DAY..."
    poetry run python -m day${DAY}.solution{{ s }}
  fi


# Execute tests (or specified solutions' tests) for the given day
# Usage: just test [day] [solution]
# replace day with 'all' to run tests for all days
test d s="all":
  #!/usr/bin/env bash
  if [[ "{{ d }}" = "shared" ]]; then
    echo "Running tests for shared code..."
    if ! poetry run pytest shared; then
      exit 1
    fi
    exit 0
  fi

  if [[ "{{ d }}" = "all" ]]; then
    # Iterate over the range of valid day numbers
    for i in {1..25}; do
      # Pad the day number with a leading zero if necessary
      day=$([[ $i -lt 10 ]] && echo "0$i" || echo "$i")
      # Check if the day exists
      DAY="$(just _get_day ${day})" && [[ -z "$DAY" ]] && exit
      echo "Running tests for day $day..."
      if ! poetry run pytest day${day}; then
        exit 1
      fi
    done
  else
    DAY="$(just _get_day {{ d }})" && [[ -z "$DAY" ]] && exit

    if [[ "{{ s }}" = "all" ]]; then
      echo "Running tests for day $DAY..."
      if ! poetry run pytest day${DAY}; then
        exit 1
      fi
    else
      [[ ! "{{ s }}" =~ ^[1-2]$ ]] && just _echo_err "Invalid solution number: {{ s }}" && exit
      echo "Running tests for day $DAY solution {{ s }}..."
      if ! poetry run pytest day${DAY}/tests/test_solution{{ s }}.py; then
        exit 1
      fi
    fi
  fi


# Run all linters
@lint: flake8 black isort

# Run all auto formatting
@lint-fix: black-fix isort-fix

# Lint with flake8
@flake8:
  poetry run flake8

# Lint with black
@black:
  poetry run black --diff --check .

# Auto format with black
@black-fix:
  poetry run black .

# Lint with isort
@isort:
  poetry run isort --diff --check .

# Auto format with isort
@isort-fix:
  poetry run isort .

# Run bandit static checking
@bandit:
  poetry run bandit -r . -q -n 3 -x '**/tests/*'

# Run safety against dependencies
@safety:
  poetry export -f requirements.txt | poetry run safety check --stdin
