#!/usr/bin/env bash
pip install --upgrade setuptools
pip install --upgrade build
pip install --upgrade twine

python -m build

twine upload -r testpypi dist/* --verbose

