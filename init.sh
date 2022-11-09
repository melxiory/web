  #!/bin/bash
  
  sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
  sudo rm -rf /etc/nginx/sites-enabled/default
  sudo /etc/init.d/nginx restart
  
  cd ask/
  sudo gunicorn --bind 0.0.0.0:8000 ask.wsgi:application&
  cd ..
