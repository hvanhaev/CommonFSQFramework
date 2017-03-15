#!/bin/bash

echo "creating __init__.py"
echo "" > __init__.py

echo "creating Skim/__init__.py"
echo "__path__.append('${PWD}/Skim/python')" > Skim/__init__.py

echo "creating Core/__init__.py"
echo "__path__.append('${PWD}/Core/python')" > Core/__init__.py
