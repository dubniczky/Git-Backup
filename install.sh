#!/bin/bash

python --version
if [ $? -neq 0 ]; then
    echo "Error: Python is not installed."
    exit 1
fi

pip --version
if [ $? -neq 0 ]; then
    echo "Error: Pip is not installed."
    exit 1
fi

git --version
if [ $? -neq 0 ]; then
    echo "Error: Git is not installed."
    exit 1
fi

pip install -r ./requirements.txt