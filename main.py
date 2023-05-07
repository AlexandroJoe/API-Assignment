from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Activity(BaseModel):
    name : str
    status : bool

activities = {
    1: {
        "name" : "Study",
        "description" : "Learn chapter 1-2",
        "status" : True
    }
}

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.get("/get-activity/{activity_id}")
def get_activity(activity_id:int):
    return activities[activity_id]

@app.get("/get-activity-by-name")
def get_activity_by_name(name:str):
    for activity_id in activities:
        if activities[activity_id]["name"] == name:
            return activities[activity_id]

@app.post ("/add-activity/{activity_id}")
def add_activity(activity_id:int,activity:Activity):
    if activity_id in activities:
        return {"Activity is already on the list"}
    activities[activity_id] = activity
    return activities[activity_id]

@app.delete ("/remove-activity/{activity_id}")
def delete_activity(activity_id:int):
    if activity_id in activities:
        activities["status"] = False
        del activities[activity_id]
        return activities["status"]

