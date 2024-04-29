# Country Rest API

I did not include the currency of the countries as I was not able to get the data in an easy way, and didn't want to waist time on something where I can still demonstrate that am able to do what is required.

Meta Info:

- Python 3.12.3
- Django 5.0.4
- Sqlite DataStore

## Getting Up and Running

### ENV
- `python -m venv {env-name}` # Optional but recommended
- `$ python3 -m venv env`
- `$ source env/bin/activate`
- `$ deactivate` # exit

### Installing

- `$ pip install django`
- `$ pip install djangorestframework`
- `$ pip install django-extensions`
- `$ python -m django --version` # verify all is working

### Running (in project root)

- `$ python manage.py runserver`

---

## Data Migrations (optional as db and is included)

### Django Migrations

- `$ python manage.py migrate`
- `$python manage.py createsuperuser --username admin --email admin@example.com` # it will prompt for pass (Login http://127.0.0.1:8000/admin/)

### Countries Migrations (My App)

- `$ python manage.py makemigrations countries`
- `$ python manage.py migrate`

### Seeding

- `$ python manage.py seed_countries` # Management Command

---

## API Endpoints

(Postman Collection included: /Django Countries API.postman_collection.json)

```
#1 - List Countries
- GET http://127.0.0.1:8000/countries
- Optional Query Parameter Filters: alpha2, alpha3, include_deleted

#2 - Soft Delete Country
- DELETE http://localhost:8000/countries/:country_id/
- Required Path Parameter: country_id

#3 - Un-Delete Country (Technically an Update)
- PUT http://localhost:8000/countries/:country_id/undelete/
- Required Path Parameter: country_id
```

---

## Unit Tests

- `$ python manage.py test` # Global Tests
- `$ python manage.py test countries` # Countries only tests

- Test 1 - listing countries and filter by alpha's
- Test 2 - soft deleting country and un-soft deleting
