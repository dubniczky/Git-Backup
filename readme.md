# Git Repository Auto Backup

Automatically clones and backs up all repositories specified in the given configuration file.

## Usage

### Installing dependencies

Run pre-written bash script

```bash
bash ./install.sh
```

Install manually using pip

```bash
pip install -r ./requirements.txt
```

### Run script

> First, edit edit: `/config.yml`

Run script from terminal

```bash
python .
```

### Using virtual environment

Load

```bash
source ./venv.sh
venv load
```

Run

```bash
python .
```

Exit

```bash
venv exit
```

### Run tests

```bash
python -m pytest
```