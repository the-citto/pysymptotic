
.PHONY: dependencies
.PHONY: git
.PHONY: init
.PHONY: mypy
.PHONY: project
.PHONY: project-struct
.PHONY: pyright
.PHONY: pytest
.PHONY: ruff
.PHONY: test
.PHONY: venv


COLUMNS = ${COLUUMNS}


all: init

init: git venv project dependencies


git: .git .gitignore 

.git:
	git init .

.gitignore:
	wget "https://github.com/github/gitignore/raw/refs/heads/main/Python.gitignore" -O .gitignore -q


venv: .venv/bin/pip-compile

.python-version:
	@read -p "Set python version: " ; pyenv local $$REPLY

.venv/bin/activate: .python-version
	python -m venv .venv

.venv/bin/pip-compile: .venv/bin/activate
	.venv/bin/python -m pip install --upgrade pip -q
	.venv/bin/python -m pip install pip-tools -q


project: requirements.in pyproject.toml project-struct

requirements.in:
	touch requirements.in

pyproject.toml:
	wget "https://github.com/the-citto/culting/raw/refs/heads/old/pyproject.toml" -q

project-struct: src/pysymptotic/__init__.py src/pysymptotic/__main__.py src/pysymptotic/py.typed tests/__init__.py

src/pysymptotic:
	mkdir -p src/pysymptotic

src/pysymptotic/__init__.py: src/pysymptotic
	touch src/pysymptotic/__init__.py

src/pysymptotic/__main__.py: src/pysymptotic
	touch src/pysymptotic/__main__.py

src/pysymptotic/py.typed: src/pysymptotic
	touch src/pysymptotic/py.typed

tests/__init__.py:
	mkdir -p tests
	touch tests/__init__.py


dependencies: venv git project dev

requirements.txt: requirements.in
	.venv/bin/python -m pip install --upgrade pip -q
	.venv/bin/python -m piptools compile -o requirements.txt requirements.in --no-strip-extras -q
	.venv/bin/python -m piptools sync requirements.txt -q

dev: requirements.txt
	.venv/bin/python -m pip install -e .[dev] -q


test: complexipy pytest mypy ruff pyright

pytest:
	@.venv/bin/pytest || true
	@echo

mypy:
	@\
		printf "\033[0;36m" ;\
		echo "-mypy-" | sed -e :a -e "s/^.\{1,$$(tput cols)\}$$/ & /;ta" | tr ' ' = | tr - ' ' | head -c $$(tput cols) ;\
		printf "\033[0m\n"
	@.venv/bin/mypy . || true
	@printf "\033[0;36m" ; printf '%*s\n' "$${COLUMNS:-$$(tput cols)}" '' | tr ' ' = ; printf "\033[0m\n"

ruff:
	@\
		printf "\033[0;35m" ;\
		echo "-ruff-" | sed -e :a -e "s/^.\{1,$$(tput cols)\}$$/ & /;ta" | tr ' ' = | tr - ' ' | head -c $$(tput cols) ;\
		printf "\033[0m\n"
	@.venv/bin/ruff check || true
	@printf "\033[0;35m" ; printf '%*s\n' "$${COLUMNS:-$$(tput cols)}" '' | tr ' ' = ; printf "\033[0m\n"

pyright:
	@\
		printf "\033[0;33m" ;\
		echo "-pyright-" | sed -e :a -e "s/^.\{1,$$(tput cols)\}$$/ & /;ta" | tr ' ' = | tr - ' ' | head -c $$(tput cols) ;\
		printf "\033[0m\n"
	@.venv/bin/pyright || true
	@printf "\033[0;33m" ; printf '%*s\n' "$${COLUMNS:-$$(tput cols)}" '' | tr ' ' = ; printf "\033[0m\n"

complexipy:
	@.venv/bin/complexipy .
	@echo







