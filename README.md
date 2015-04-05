# csc567-project-server
Server for the android clipboard sync application.

# Setup
- Clone the repo
- Run pip install -r requirements.txt
- Add a random string for the SECRET_KEY variable in a new file named settings_local.py
- Put settings_local.py in clipboardserver/
- Run python manage.py syncdb && python manage.py migrate && python manage.py runserver
