@echo off
echo Running coverage on the whole project...

CALL python -m pytest --cov=./backend --cov-report=term-missing ./tests
