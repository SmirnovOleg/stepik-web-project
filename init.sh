sudo rm -rf /etc/nginx/sites-*/*
sudo ﻿ln -s /home/box/web/etc/app-nginx.conf  /etc/nginx/sites-enabled/app-nginx.conf
sudo /etc/init.d/nginx restart
