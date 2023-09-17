```
conda create -n bigeye
conda activate bigeye

python manage.py makemigrations tickets
python manage.py migrate

python manage.py createsuperuser
>admin
>admin@domain.com
>admin

python manage.py runserver
```