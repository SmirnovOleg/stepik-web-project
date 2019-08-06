sudo rm -rf /etc/nginx/sites-*/*
sudo ln -s /home/box/web/etc/app-nginx.conf  /etc/nginx/sites-enabled/app-nginx.conf
sudo service nginx restart
cd /home/box/web/ask
sudo gunicorn --config=../etc/gunicorn.conf ask.wsgi
