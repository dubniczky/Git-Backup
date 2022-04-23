# Git Repository Auto Backup

Automatically clones and backs up all repositories specified in the given configuration file.

## Usage

Using this project requires python3 and pip to be installed.

Automake GNU is recommended, otherwise enter the commands detailed in `Makefile` manually.

### Quick Start

```bash
make
```

### Manual Installation

Install dependencies

```bash
make install
```

### Run script

> First, edit: `/config.yml`

Run script from terminal

```bash
make run
```

### Run tests

Run python linter

```bash
make lint
```

Run python tester

```bash
make test
```

Run lint and test
```bash
make auto
```