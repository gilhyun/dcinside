#!/usr/bin/env bash
pushd ./
cd tests
pytest --cov=./ -s --cov-report term-missing
popd
