# birdbook
Tensorflow powered bird recognition web application in Django

# Requirements

- Python 3
--------------------
pip install -r requirements

- Env variables
--------------------
DB_NAME
DB_PASS
DB_USER
DJ_SECRET

- Tensorflow stuff
----------------------
birdy/birdy/intelligence/output_labels.txt
birdy/birdy/intelligence/output_graph.pb

- Postgresql

# Setting up

- Use a virtualenv
- python birdy/manage.py makemigrations

# How to run

- python birdy/manage.py runserver
- Browse to the http://127.0.0.1:8000

# License

- Apache
    Don't use the name 'birdbook'
    Document the changes you do to the code
    Keep the same license
    https://choosealicense.com/licenses/apache-2.0/