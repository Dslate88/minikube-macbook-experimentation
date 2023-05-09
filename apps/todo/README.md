# to-do application
- simple python flask to-do application for minikube deployment exploration

## build image
docker build -t todo-app .
docker run -p 8000:8000 todo-app (to run outside of minikube)

## push to hub
docker tag todo-app dslate88/todo-app:v1
docker push dslate88/todo-app:v1
