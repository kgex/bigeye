```
conda create -n bigeye
conda activate bigeye

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
>admin
>admin@domain.com
>admin

python manage.py runserver


# when you make a change in the model

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```