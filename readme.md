# Installation guide

This need supabase and cloudinary

Make venv
```
python3 -m venv .venv
```

change your source
```
source .venv/bin/activate
```

If that not working, you can try this <a href="https://docs.python.org/3/library/venv.html">DOCS</a>

install requirements 
```
pip install -r requirements.txt
```

Migrate database 
```
python3 manage.py makemigrations
python3 manage.py migrate
```

# Running server

```
python3 manage.py runserver
```

Your app run default in localhost:8000

# Create SuperUser

```
python3 manage.py createsuperuser
```

You can login your superuser at http://localhost:8000/admin/

# If you need static assets

```
python3 manage.py collectstatic
```