python3 manage.py collectstatic --no-input
python3 manage.py migrate
exec gunicorn -c gunicorn.py zolaris.wsgi


#python3 manage.py runserver 0.0.0.0:5000
