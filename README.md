SIMPLE DBTOOL INSERT INTO DATABASE WITH PYTHON
--DJANGO FRAMEWORK--

./venv/Scripts/active to run virtual environment

cd dbtool
pip install -r requirements.txt

py manage.py migrate
##ssetting db là 127.0.0.1 port 3306
##db name: test, user: root, pass: ''

command run
py manage.py do -f 'test.xlsx'
