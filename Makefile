VENV_DIR := venv
REQUIREMENTS := requirements.txt

.PHONY: setup exercises solutions tests cleanup

# Target to set up the virtual environment and install dependencies
setup:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)

solutions:
	$(VENV_DIR)/bin/python scripts/compile_solutions_to_pdf.py

# Target to compile exercises using compile_exercises.py
exercises:
	$(VENV_DIR)/bin/python scripts/compile_exercises.py
	$(VENV_DIR)/bin/python scripts/remove_outputs.py
	$(VENV_DIR)/bin/python scripts/print_notebook_sizes.py


# Target to run unittests using tests.py
tests:
	$(VENV_DIR)/bin/python scripts/tests.py

# check the syntax
lint:
	$(VENV_DIR)/bin/nbqa pylint solutions

# Target to clean up generated folders
cleanup:
	$(VENV_DIR)/bin/python scripts/remove_outputs.py
	rm -rf exercises/*.ipynb
	rm -rf __pycache__
	rm -rf solutions/data
	rm -rf solutions/*.npz
	rm -rf solutions/*.jpg
	rm -rf solutions/*.png
	rm -rf solutions/*.txt
	rm -rf solutions/.ipynb_checkpoints

	$(VENV_DIR)/bin/python scripts/print_notebook_sizes.py

