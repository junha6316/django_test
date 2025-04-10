


```
docker-compose up -d
docker exec -it test_django_cache-django32-1 bash
PYTHONPATH=/app python manage.py makemigrations
PYTHONPATH=/app python manage.py migrate
PYTHONPATH=/app python initial_data.py

docker exec -it test_django_cache-django32-1 bash
PYTHONPATH=/app python scripts.py save

docker exec -it test_django_cache-django40-1 bash
PYTHONPATH=/app python scripts.py load
```