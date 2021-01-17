# Locust Stress Test

## Create Environment

```bash
$ virtualenv locust-srv
```

## Activate Virtual Environment

```bash
$ cd locust-srv/
$ source bin/activate
```

## Get list requirements

```bash
$ pip freeze > requirements.txt
```

## Install Requirements

```bash
$ pip install -r requirements.txt
```

## Clone repository 

```bash
$ git clone git@github.com:fcchn4/locust-srv.git
```

## Run locust project

```bash
## First option
$ locust
## or 
locust -f locustfile.py
```