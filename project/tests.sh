#!/bin/bash

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "Error: pytest is not installed. Please run 'pip install pytest' to install it."
    exit 1
fi

current_directory=$(pwd)
echo "Current directory: $(pwd)"

# Run tests
pytest .