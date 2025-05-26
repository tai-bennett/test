#!/usr/bin/env bash

source venv/bin/activate &&
python3 main.py configs/example_config.json &&
deactivate
