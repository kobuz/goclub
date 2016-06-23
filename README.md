[![Build Status](https://travis-ci.org/kobuz/goclub.svg?branch=master)](https://travis-ci.org/kobuz/goclub)

# goclub

## Setup

Install docker and docker-compose (version >=1.6.0) first.
Run it with:

```bash
$> docker-compose up
```

It might be good idea to run migrations as well:

```bash
$> docker-compose run --rm web ./manage.py migrate
```
