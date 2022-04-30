#!/bin/bash
coverage run -m unittest tests.main -v
coverage html
coverage report
rm -r coverage.svg
coverage-badge -o coverage.svg