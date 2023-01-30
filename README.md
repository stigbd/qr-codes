# qr-codes

This is a simple command line (CLI) QR code generator and decoder.

## Installation

```bash
pipx install git+https://github.com/stigbd/qr-codes.git
```

## Usage

```bash
qr-codes --help
```

## Development

### Prerequisites

- [poetry](https://python-poetry.org/docs/#installation)
- [nox](https://nox.thea.codes/en/stable/)
- [nox-poetry](https://nox-poetry.readthedocs.io/en/stable/)

### Setup

```bash
git clone https://github.com/stigbd/qr-codes.git
cd qr-codes
poetry install
```

### Run linter and tests

```bash
nox
```

### Run locally

```bash
poetry run qr-codes --help
```
