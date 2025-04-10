import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from myapp.models import Book

Book.objects.bulk_create([
    Book(title="Django for Beginners"),
    Book(title="Two Scoops of Django"),
    Book(title="High Performance Django")
])
print("Sample data inserted.")
