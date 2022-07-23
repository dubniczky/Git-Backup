# Git Repository Auto Backup

Automatically clones and backs up all repositories specified in the given configuration file.

## Support ❤️

If you find the project useful, please consider supporting, or contributing.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/dubniczky)

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

### Misc Commands

Clean up pycache

```bash
make clean
```

Install app as a cronjob

> Edit `cron.sh` to specify run frequency and targets.

> Move the project to it's final location before installing the cronjob.

```bash
make cron
```