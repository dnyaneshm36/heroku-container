#!/bin/sh
docker run -d --name django-heroku -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 dockerheroku 
