# Student Information App

This is a student information app written in Django. All data is populated in
the migrations so there is no need for SQL commands. Note that the Bootstrap
framework has been used for styling but the website is functional without it.

Do the following one at a time in order to setup this app

    git clone https://github.com/cbhayes47/student_info.git
    cd student_info

    python3 -m venv venv
    source ./venv/bin/activate
    pip install django
    python manage.py migrate
    python manage.py createsuperuser


    python manage.py runserver
