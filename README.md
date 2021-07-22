# Mockserver

### Setup Procedure

#### Requirements
1. Python 3.8 +

#### Setting up
Clone the Repo
```shell
git clone https://github.com/Peopple-Shopping-App/mockserver.git
````

Install Requirements
```shell
pip install -r requirements.txt
```
Add JSONs to `app/assets` folder

### Steps to Run

Once setup is completed, start server using the command below.
```shell
python server.py
```
or use `uvicorn` directly

```shell
uvicorn app.main:app
```

Once the server is up, you can use the browser/curl to get started.

URL: `<host>:<port>/{filename}`

Eg: `http://localhost:8000/user`



Example:

```shell
uvicorn app.main:app

Started server process [←[36m8568←[0m]
Waiting for application startup.
Application startup complete.
Uvicorn running on ←[1mhttp://127.0.0.1:8000 (Press CTRL+C to quit)
```

```shell
curl http://localhost:8000/user

[{"id": 1, "first_name": "Dreddy", "last_name": "Pellant", "email": "dpellant0@instagram.com", "gender": "Female", "ip_address": "255.126.147.186"}, 
{"id": 10, "first_name": "Fergus", "last_name": "Perchard", "email": "f
perchard9@netlog.com", "gender": "Agender", "ip_address": "25.99.204.233"}]
```
