# API Project | Todo

## Technology stack:
- Python 3.8.5
- Django 3.2.7
- PostgreSQL 5.2

## Сommands to start the service:
- python -m venv
- .\todo\Scripts\activate
- pip install -r requirements.txt
- python manage.py runserver
- create admin: python manage.py createsuperuser

## Database:
- Create database todo

## Enviroment variables: 
```
PORT=8000

# variables for DB connection:
DB_DATABASE=todo
DB_USER=replace_me
DB_PASSWORD=replace_me
DB_HOST=localhost
DB_PORT=5432
```

## Endpoints

#### Add a new task

```
curl --request POST \
  --url http://127.0.0.1:8000/api/todo/ \
  --header 'Content-Type: application/json' \
  --data '  {
		"unit": "Home",
    "title": "New task",
    "description": "Write description"
  }'
```

#### Get list of tasks

```
curl --request GET \
  --url http://127.0.0.1:8000/api/todo/
```

#### Get a task

```
curl --request GET \
  --url http://127.0.0.1:8000/api/todo/[todo_id]
```
### Filter by done and unit:  
![Link](https://github.com/uzhegovaelena/todo-api/blob/main/todo%20list.PNG)
