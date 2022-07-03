[![Build and Deploy.](https://github.com/ejdecena/test-ci-cd/actions/workflows/build_and_deploy.yml/badge.svg?branch=master&event=push)](https://github.com/ejdecena/test-ci-cd/actions/workflows/build_and_deploy.yml)
[![Lint and Tests.](https://github.com/ejdecena/test-ci-cd/actions/workflows/lint_and_tests.yml/badge.svg?branch=develop&event=pull_request)](https://github.com/ejdecena/test-ci-cd/actions/workflows/lint_and_tests.yml)
# test-ci-cd
Test continuos integration and continuos delivery.

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
Instructions for run calculator in a Docker container...

## Production.
Instructions for production...