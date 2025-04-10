import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")  # ← settings 경로 확인
django.setup()

from myapp.models import Book
from django.core.cache import cache

def save_list():
    cache.set("books", list(Book.objects.values()), timeout=None)

def save_qs():
    cache.set("books", Book.objects.all(), timeout=None)

def load():
    print(cache.get("books"))

if __name__ == "__main__":
    import sys
    if sys.argv[1] == "save_list":
        save_list()
    elif sys.argv[1] == "save_qs":
        save_qs()
    elif sys.argv[1] == "load":
        load()