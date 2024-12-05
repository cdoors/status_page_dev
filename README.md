-----
Status Page
Developed by Chad Doorley
v2.0.1

This is the self-service solution that I was talking about.
-----

## Setup

> uv init
> uv sync

## Update all packages
> uv run pip install -U $(uv run pip freeze | awk -F'==' '{print $1}')


## Usage
> cd mysite
> python manage.py runserver
