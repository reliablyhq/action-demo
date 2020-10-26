# action-demo
Repository demo for Reliably workflow with GitHub Action

## Python Starlete Web App

Simple stateless web application using [Starlette][https://www.starlette.io/]

## To run the app locally with Python

```bash
$ python app.py
```
### Test the application is running

When the image is running you should be able to access the running server  from  curl

`curl http://localhost:8000/msg` - should give a json response of {"message":"Hello world! From Starlette running on Uvicorn with Gunicorn in Alpine. Using Python 3.7"}

`curl http://localhost:8000/dt` - should give a json response of {"hello":"world","now":"2019-10-03 09:31:22.163548"}

The app home page can also be seen in a browser [App link](http://localhost:8000)

### Docker Build & Run

Build the image using the following command

```bash
$ docker build -t action-demo-service:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 8000:8000 action-demo-service
```

Pushed to docker hub with:


docker tag <image_id> gtfisher/action-demo-service:v01
docker push gtfisher/action-demo-service


deploy on minikube

kubectl create deployment action-demo --image=gtfisher/action-demo-service:v01

kubectl expose deployment action-demo --type=LoadBalancer --port=8000

kubectl get services

minikube service action-demo

