# Python REST API

A basic Python REST API using FastAPI.

## Requirements

Python 3.11.4 

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testing 

```shell
python -m unittest discover
coverage run -m unittest discover
coverage report -m
autopep8 --in-place --aggressive --aggressive src/*.py test/*.py
pylint --recursive=y ./src ./test
```

## Running

```shell
uvicorn app:app --reload
```