# Run even if up to date
.PHONY: clean install run test all lint test auto cron


# Variables
PYTHON=python3
PIP=pip
REQS_FILE=requirements.txt
TEST_LIB=pytest
LINT_LIB=pylint


# Default command
default: clean install run

# Clean up pycache
clean:
	rm -rf __pycache__/

# Install dependencies
install:
	$(PIP) install -r $(REQS_FILE)

# Run main
run:
	$(PYTHON) .

# Run lint
lint:
	$(PYTHON) -m $(LINT_LIB)

# Run test
test:
	$(PYTHON) -m $(TEST_LIB)

# Run lint and test
auto: lint test

# Install cron job
cron:
	./cron.sh