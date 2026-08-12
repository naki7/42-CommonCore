VENV    := matrix
PYTHON  := $(VENV)/bin/python3
PIP     := $(VENV)/bin/pip
MAIN    := fly_in.py
FILE	:= ./maps/easy/test.txt
OUTPUT	:= ''

.PHONY: install run debug clean lint lint-strict

all: install

install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install pydantic pygame rich flake8 mypy
	tar -xf maps.tar

run:
	$(PYTHON) $(MAIN) $(FILE) $(OUTPUT)

debug:
	$(PYTHON) -m pdb $(MAIN) $(FILE) $(OUTPUT)

clean:
	rm -rf $(VENV) build dist *.egg-info .mypy_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores \
		--ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict
