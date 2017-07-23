web: gunicorn P3.wsgi
worker: celery worker --app=tasks.app

worker: celery -A P3 worker -l info