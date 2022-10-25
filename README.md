![Tests](https://github.com/ngoiz/plant-classification/actions/workflows/ci.yaml/badge.svg)
# plant-classification

Plant classification using Neural Networks

# Work in progress!

## Installation

Requirements:

* Python v3.9+

A packaged version is not yet available. Currently there is the option to install from
source code.

### Source code install

This project uses [poetry](https://python-poetry.org/) to handle its dependencies.

To install the source code please ensure that `poetry` is installed on your system
and that 
```bash
poetry --version
```
runs without issues.

Clone the directory:
```bash
git clone http://github.com/ngoiz/plant-classification
```

Move to the newly created directory and run
```bash
poetry install
```
which should install all the required dependencies. 

There are several ways to run the package with `poetry`. A simple way of seeing that 
the installation has been performed correctly is to run the project tests.
```bash
poetry run python -m unittest
```

## Initial training flower dataset
The initial dataset is gathered from Olga Belitskaya's repo and gratefully acknowledged
https://www.kaggle.com/datasets/olgabelitskaya/flower-color-images?select=flower_images