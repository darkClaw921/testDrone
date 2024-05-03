#!/bin/bash

# Переменные
REPO_URL="https://github.com/darkClaw921/testDrone.git"
APP_NAME="your_app"
CONTAINER_NAME="your_container"
BRANCH="master" # Ветка, которая будет использоваться
PORT=3005 # Порт, на котором будет работать приложение

# Клонирование репозитория
# git pull $BRANCH $REPO_URL
git pull
# cd your_repository
docker stop $CONTAINER_NAME || true
docker rm -f $CONTAINER_NAME || true

docker rmi $APP_NAME:latest || true
# Сборка Docker-контейнера
docker build -t $APP_NAME .

# Остановка и удаление старого контейнера (если он существует)


# Запуск нового контейнера
docker run -d -p $PORT:$PORT --name $CONTAINER_NAME $APP_NAME
