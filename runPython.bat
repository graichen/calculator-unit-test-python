
set PYTHONPATH=c:\workspace\src:c:\workspace\tests
pip install pytest

#pytest -v --cov=. --cov-config .coveragerc --junitxml=xunit-reports/xunit-result.xml --cov-report xml:coverage-reports/coverage.xml --rootdir=.
python src/calculator.py
