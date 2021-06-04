# Zillow API Challenge

## Requirements

1. Model the data using Django's ORM.
2. Write a Django command to ingest the data.
3. Use Django Rest Framework to provide an API to query the models.
4. *Bonus*: Allow new records in the API you build.

Please add API documentation that you would provide to another developer working to integrate your API into their client application.

## Project Summary

In the `root` directory, there are some extra files. `.editorconfig`, and `setup.cfg` are relevant for linting and formatting tools like: `flake8`, `isort` and `black`.

I like using `flake8` over `pylint` because I feel like `pylint` is more pedantic and tries to make assumptions more than it needs to. Normally I would write some unit tests with the standard library or with `pytest`, but I'm trying to complete this activity as quickly as possible.

Included `.dockerignore` and `Dockerfile` to get the project up and running with minimal effort.

In addition to a `requirements.txt`, I like to leverage version locking capabilities of `pipenv`. You can easily install use `pipenv` or `virtualenv` to get started... Or you can just build and run the docker container, which we'll get into a bit later.

## Thought Process

The `models.py` was written after analyzing the data from the `challenge_data.csv`. For the serializers, I used `HyperlinkedModelSerializer` because I love HATEOAS, being able to pivot the datasets easily is beautiful.

We could have abstracted the tables further and depending on how this data is accessed, a more ideal configuration would be likely. We're making an assumption that the data will primarily be accessed through `property` in a list view and then we can drill down where it's relevant: `detail`, `evaluation`, `zillow` and `location`.

All relevant operations (`GET`, `POST`, `PUT`, `DELETE`) are also supported across each viewset.

## Adding Existing Data

If you're running the application manually, you will probably want to import the existing data. You can do so with the following command:

``` sh
python manage.py add_data challenge_data.csv
```

The `contextualize` method is not ideal, as this is mapping and converting the data from CSV to its respective types before being consumed into records. We could have spent more time around this to make it more succinct, closer to a `struct` or `dataclass`.

## Building & Deploying

Great! If you're using `docker` ... You're in for a treat. You can easily get started by executing the following:

``` sh
docker build -t "zillow-api:test" .
docker run -it -p 8000:8000 zillow-api:test runserver 0.0.0.0:8000
```

If you're not using `docker` ... You can do it with or without `virtualenv` and install the project requirements.

``` sh
virtualenv -p python3 env
. ./env/bin/activate
pip3 install -r requirements.txt
python manage.py migrate
python manage.py add_data challenge_data.csv
python manage.py runserver
```

You should be able to start your browser and navigate to:

``` sh
localhost:8000/rest/v1/
```

Great! Now you can access the root page. If you wanted the `JSON` view only, that's easy: `http://localhost:8000/rest/v1/?format=json`

## Caveats & Gotchas

A fun little exercise, but the data itself needs a bit of attention. For example, for `price` .. This is currently being processed as a `str` but it would be more ideal to have as a `int`. We could iterate in the next version to correct that.

There's also a number of empty literals that would be more ideal to have represented as numeric values instead.

The data tested works, but variations in the data beyond the sample could cause NULL constraint failures. Another reason why it's important to have a data contract in-place.

Filtering and more specific viewsets are some examples of things to pursue in the future.