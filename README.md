./venv/Scripts/active để chạy môi trường ảo

cd dbtool
pip install -r requirements.txt

py manage.py migrate
##ssetting db là 127.0.0.1 port 3306
##db name: test, user: root, pass: ''

câu lệnh chạy thử command
py manage.py do -f 'test.xlsx'
