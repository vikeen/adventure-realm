# Melody Buddy

### Depencies

* [Python](http://install.python-guide.org)
* [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup)
* [Node](https://nodejs.org/en/download/)

```sh
$ npm install
$ npm install -g less
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

### Database

```sql
CREATE DATABASE adventure_realm;
CREATE ROLE adventure_realm_user with PASSWORD 'password';
ALTER ROLE adventure_realm_user with LOGIN;
ALTER ROLE adventure_realm_user WITH CREATEDB;
ALTER DATABASE adventure_realm OWNER TO adventure_realm_user;
```

```sh
$ python manage.py migrate
$ python manage.py collectstatic
```

### Development

* `python manage.py runserver` - Server
* `gulp` - Frontend Assets

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

```sh
$ git push heroku master
$ heroku run python manage.py collectstatic
$ heroku run python manage.py migrate
$ heroku open
```
or

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
