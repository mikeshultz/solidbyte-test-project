# solidbyte-test-project
[![Build Status](https://travis-ci.org/mikeshultz/solidbyte-test-project.svg?branch=master)](https://travis-ci.org/mikeshultz/solidbyte-test-project)

Solidbyte version: `1.0.0`

A test project for [Solidbyte](https://github.com/mikeshultz/solidbyte).  Mostly
used for trying out features but can also be a reference for new users.

## Development

### Dependencies

To setup a virtual environment and install dependencies:

    python3 -m venv ~/.venvs/solidbyte-test-project
    source ~/.venvs/solidbyte-test-project/bin/activate
    pip install -r requirements.txt

### Linting Python Tests and Scripts

    flake8

### Linting Vyper

    flake8-vyper

### Test Contracts

Testing using the `test` network, which in our case is `eth_tester`.

    sb test test
