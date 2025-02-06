from flask import (
    Flask,
    request
)
from app.database import task

app = Flask(__name__)

# ReST - Representation State Transfer
# ReST is an architectural design pattern that helps design our APIs (services)

@app.get("/")
@app.get("/tasks")
def get_all_tasks():
    out = {
        "tasks": task.scan(),
        "ok": True
    }
    return out

@app.get("/tasks/<int:pk>")
def get_single_task(pk):
    out = {
        "task": task.select_by_id(pk),
        "ok": True
    }
    return out

# @app.put example

@app.put("/tasks/<int:pk>")
def update_task(pk):
    task_data = request.json
    task.update_by_id(task_data,pk)
    return "", 204
    

# @app.post

@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)

    return "", 204

#@app.delete

@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete_by_id(pk)
    return "", 204


# @app.post("/tasks") # This route should be mapped to a function that creates new tasks
# @app.put("/tasks/<int:pk>") # This route should be mapped to a function that update existing tasks
# @app.delete("/tasks/<int:pk>") # This route should be mapped to a function that deletes existing tasks

# You'll also, the request context object.
# You can retrieve the income JSON from the request body by using: request.json

"""
{
    "name": "task name",
    "summary": "task summary",
    "description": "task description"
}
"""