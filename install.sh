apt update
apt install python3-pip postgresql nginx uwsgi uwsgi-plugin-python3

pip3 install -r requirements.txt

psql -U postgres -c "ALTER USER postgres WITH PASSWORD '1';"

psql -U postgres -c "CREATE DATABASE test_mail OWNER postgres;"

python3 manage.py migrate
