#!/bin/sh
docker stop django-heroku
docker rm django-heroku
docker build . -t dockerheroku