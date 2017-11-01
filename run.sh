cp server/mail_test.conf /etc/nginx/sites-enabled/mail_test.conf
nginx -s reload
nohup /usr/bin/uwsgi --ini server/uwsgi.ini > log.txt &
