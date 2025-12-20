# URL Shortener Service

## Prerequisites

* **Python 3.8+**
* **pip** (Python package installer)

## Installation
**Create a Virtual Environment**
```
    python -m venv env
    env\Scripts\activate
```
**Install FastAPI**
```
    pip install fastapi[standard]
```

## Running the Server
'''
  fastapi dev
'''

## API Usage & Sample Curl Commands
```
    curl -X 'POST' \
      '[http://127.0.0.1:8000/shorten](http://127.0.0.1:8000/shorten)' \
      -H 'Content-Type: application/json' \
      -d '{
      "url": "[https://www.python.org/doc/versions/](https://www.python.org/doc/versions/)"
    }'
```
