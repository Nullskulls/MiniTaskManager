import json

def reader(filename = "tasks.json"):
    with open(filename, "r") as file:
        return json.load(file)


def loader(filename = "tasks.json"):
    tasks = None
    try:
        tasks = reader(filename)
    except FileNotFoundError:
        with open("tasks.json", "w"):
            tasks = reader(filename)


    if tasks is not None:
        return tasks
    else:
        raise "Unable to create file, Please check permissions."

def saver(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def settings_loader(filename = "preferences.json"):
    try:
        with open("preferences.json", "r") as preferences:
            filename = json.load(preferences)["file_name"]
            return settings_loader(filename)
    except FileNotFoundError:
        print("No preferences.json")
        with open("preferences.json", "w") as preferences:
            holder = input("please select a preferred json file: ")
            settings = {
                "file_name": holder,
            }
            preferences.write(json.dumps(settings))