In order to run file.

1- Load file in vsCode

2- Download requirements.txt using "pip install -r requirements.txt"

3- Make sure django-rest-framework is downloaded by running "pip show djangorestframework", if not downloaded, run "pip install django-rest-framework" and rerun the "show" command.

4- Additionally run "pip install django-cors-headers" and "pip install Pillow"

Once this is done, create a virtual environment using "python -m venv <env-name>", launch the environment using "<env-name>/scripts/activate", and run "python manage.py runserver" and connect to your localhost web server!
