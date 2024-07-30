# Django API for import 
This little util uses Python Django with its virtual environment. The main purpose is to parse some data given to me by Whys as an assignment, save them in the database, and be able to load them back. 


Be careful, this application does not like duplicates. The next command should do the job of removing all the data from a database including users.
```bash 
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
``` 

# Run

This approach is for Linux-based systems and might differ on Windows and MacOS. First, open the directory, and enter. 

```bash 
virtualenv -p python3 .
```
Once your virtual environment is installed, use the next command to activate it.

```bash 
source bin/activate
```

Now you can use 
```bash 
python manage.py runserver
``` 
to run the server, or 
```bash
pip freeze
``` 
And check you have everything installed correctly.

# Sources 

For this application, I used different sources. Firstly, let it be said that this was the first time with Django. I am used to using the FASTapi framework, SQLAlchemy for data manipulation, and Alembic for migrations. With these at my disposal, the assignment would be much easier. I hope you will take that into consideration.

I watched this tutorial on YouTube to get insight, into how to use Django https://www.youtube.com/watch?v=F5mRW0jo-U4. 

More:
https://docs.djangoproject.com/en/5.0/topics/db/models/
https://www.django-rest-framework.org/api-guide/serializers/
https://www.w3schools.com/django/django_insert_data.php
https://docs.djangoproject.com/en/5.0/howto/custom-model-fields/
https://stackoverflow.com/questions/69071531/how-to-use-django-serializer-to-update-an-instance 
and much more stackoverflow

# TODO
There are also some flaws in this code. One of them is that secret keys should be stored in a .env file. Some of them are mentioned in the code like that, and because of the wrong format, I have decided to make a date text field.

There should be also tests added into CI/CD. 
Database as all other binaries should not be uploaded to GitHub and should be in .gitignore. 
I hope by mentioning all these problems highlight my abitily also to deal with them. 