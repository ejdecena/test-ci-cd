[![Continous Integration.](https://github.com/ejdecena/test-ci-cd/actions/workflows/continuos_integration.yml/badge.svg?branch=master&event=push)](https://github.com/ejdecena/test-ci-cd/actions/workflows/continuos_integration.yml)
# test-ci-cd
Test continuos integration and deploying integration.

## Development.
Instructions for coding.

#### Build a Docker image:
```bash
docker build -t "<your tags>" .
```

#### Run the linter:
```bash
flake8 --config=flake8
```

#### Run the tests:
```bash
python3 -m unittest -v tests/*.py
```

#### Run the calculator in a Docker container:
adsad

## Production.
Instructions for production.