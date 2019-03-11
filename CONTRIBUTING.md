# Contributing

Feel free to send Pull Requests my way to add to the possible locations and method
to find java.

# Deploy

Deploying a built to pypi can be done with:

```bash
pip install setuptools wheel
python setup.py sdist bdist_wheel
ls dist/

pip install twine
twine upload dist/*
```
