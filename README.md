[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/asottile.flake8-walrus?branchName=main)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=26&branchName=main)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/26/main.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=26&branchName=main)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/flake8-walrus/main.svg)](https://results.pre-commit.ci/latest/github/asottile/flake8-walrus/main)

flake8-walrus
================

flake8 plugin which forbids assignment expressions (the walrus operator)

## installation

`pip install flake8-walrus`

## flake8 codes

| Code   | Description                       |
|--------|-----------------------------------|
| ASN001 | do not use assignment expressions |

## rationale

lol

## as a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/pycqa/flake8
    rev: 3.8.1
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-walrus==1.1.0]
```
