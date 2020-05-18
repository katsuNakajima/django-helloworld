# django-helloworld

## About

django web app with nginx on AWS EC2

## Udage

`$ pipenv sync`

` $ gunicorn helloworldproject.wsgi`

`$ ln -s helloworldproject.conf /etc/nginx/sites-enabled/helloworldproject`

`$ sudo systemctl restart nginx`
