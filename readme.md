# Deep Learning GRS-34806

![Badge](https://github.com/marccoru/WUR_DL/actions/workflows/tests.yaml/badge.svg)

## Getting Started

* `make setup` installs python and dependencies
* `make exercises` creates exercise notebooks. I.e., removes text between `SOLUTIONSTART` and `SOLUTIONEND` keywords
* `make solutions` compiles solution PDFs
* `make tests` tests the solution notebooks
* `make cleanup` removes temporary files and clear outputs

for scripts, check the `Makefile`. Backup data located in `data`.

## Detailed Setup
The command `make setup` will execute the following steps:
1. clone this repository locally
2. install a local python environment in `venv` with `python -m venv venv`
3. install required packages with `pip install -r requirements.txt`

## Authors

for organization of this repo, ask M.Russwurm