# vrp-recognizer
==============================

Recognizes vehicle registration plates (vrp) and finds out to which country and city 
the vehicle belongs.

Project Organization
------------

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── pyproject.toml     <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with poetry
    ├── vrp_recognizer     <- Main Django module.
    │   └── __init__.py    <- Makes vrp_recognizer a Python module
    │
    └── vrp_assigner       <- Django app.
        └── __init__.py    <- Makes vrp_assigner a Python module
 

## important commands
- python manage.py loaddata data/interim//vrpCodesGermany.json  - to add the data utils/vrpCodesGermany.json into existing database of the same format based on model migrated
- python manage.py flush - to delete all existing data from database table based on model migrated

## to-dos
- refactor vrpAssigner.views so that VrpLocationSerializer is used more efficiently
- add data of all European vehicle registration plates into database
- add tests
- find a way to deploy django web server so that other devices can access it
- finally add a way to recognize vehicle registration plates from  pictures as a independent app/rest api
- add CI with Dockerfile

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a> and the <a target="_blank" href="https://github.com/khuyentran1401/data-science-template">cookiecutter data science project template by khuyentran1401</a>. #cookiecutterdatascience</small></p>