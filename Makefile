.PHONY: install local lint cfn-lint flake8 black black-fix isort isort-fix bandit safety test build lint-fix

install: poetry-config
	poetry env use 3.8.10
	poetry install

update:
	poetry update

local: install
	poetry run pre-commit install

lint: flake8 black isort newline-check

lint-fix: black-fix isort-fix

flake8:
	poetry run flake8

black:
	poetry run black --diff --check .

black-fix:
	poetry run black .

isort:
	poetry run isort --diff --check .

isort-fix:
	poetry run isort .

bandit:
	poetry run bandit -r src -q -n 3

safety:
	poetry export -f requirements.txt | poetry run safety check --stdin

newline-check:
	scripts/newline_check.sh

test:
	poetry run pytest \
		--cov-report term:skip-covered \
		--cov-report html:reports \
		--cov-report xml:reports/coverage.xml \
		--junitxml=reports/unit_test_report.xml \
		--cov-fail-under=95 \
		--cov=src tests/unit_tests -ra -s

test-v:
	poetry run pytest \
		--cov-report term:skip-covered \
		--cov-report html:reports \
		--cov-report xml:reports/coverage.xml \
		--junitxml=reports/unit_test_report.xml \
		--cov-fail-under=95 \
		--cov=src tests/unit_tests -ra -s
		--vv

coverage:
		open reports/index.html


