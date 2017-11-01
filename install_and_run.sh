apt update
apt install python3-pip postgresql nginx uwsgi supervisor uwsgi-plugin-python3


sudo -u postgres psql postgres
ALTER USER "postgres" WITH PASSWORD '1';
\q

psql -U postgres -c "CREATE DATABASE test_mail OWNER postgres;"

python3 manage.py migrate


sudo cp server/mail_test.conf /etc/nginx/sites-enabled/mail_test.conf
sudo nginx -s reload


nohup /usr/bin/uwsgi --ini server/uwsgi.ini > log.txt &