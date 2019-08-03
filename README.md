[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/asottile.flake8-walrus?branchName=master)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=26&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/26/master.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=26&branchName=master)

flake8-walrus
================

flake8 plugin which forbids the walrus operator

## installation

`pip install flake8-walrus`

## rationale

lol

## as a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.7.8
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-walrus==1.0.0]
```
