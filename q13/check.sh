#!/bin/bash
set -e
python3.8 -m ruff format --check .
python3.8 -m ruff check .
python3.8 -m pytest -v
