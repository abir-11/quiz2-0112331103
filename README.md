# Grade Checker

![Grade Checker CI](https://github.com/abir-11/quiz2-0112331103/actions/workflows/ci.yml/badge.svg)

A simple Python Grade Checker project with automated testing using pytest and GitHub Actions.

## Project Description

This project contains a simple Python function that determines a student's grade based on their score.

The project also includes automated tests using pytest. GitHub Actions is configured to automatically run the tests whenever changes are pushed to the repository.

## Files

- `grade.py` — Contains the grade calculation function.
- `test_grade.py` — Contains automated pytest tests.
- `.github/workflows/ci.yml` — GitHub Actions CI workflow.
- `.gitignore` — Specifies files that should not be tracked by Git.

## Testing

Run the tests locally with:

```bash
python -m pytest test_grade.py -v