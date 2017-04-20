git push heroku master &&
heroku run python manage.py collectstatic --noinput &&
heroku run python manage.py migrate;
