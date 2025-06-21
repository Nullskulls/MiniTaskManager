import json
import datetime

def reader(filename = "tasks.json"):
    with open(filename, "r") as file:
        current = json.loads(file.read())
        if current is not None:
             return current
        else:
            return {}


def loader(filename = "tasks.json"):
    tasks = None
    try:
        tasks = reader(filename)
    except FileNotFoundError:
        with open("tasks.json", "w") as file:
            current_datetime = datetime.datetime.now()
            file.write(json.dumps({"Welcome Task" : [f"Created: {current_datetime}", f"Deadline: undefined", "Priority: undefined"]}))
            tasks = reader(filename)
    if tasks is not None:
        return tasks
    else:
        raise "Unable to create file, Please check permissions."

def saver(data, filename = "tasks.json"):
    with open(filename, "w") as file:
        json.dump(data, file)

def settings_loader(filename = "preferences.json"):
    try:
        settings = reader(filename)
        return settings
    except FileNotFoundError:
        with open("preferences.json", "w") as file:
            settings = {
                "task_list": "tasks.json",
            }
            json.dump(settings, file)
            return settings

time = datetime.datetime.now()
print(time)