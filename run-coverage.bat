@echo off
echo Running coverage on the whole project...

CALL python -m pytest --cov=../ --cov-report=term-missing ./tests
