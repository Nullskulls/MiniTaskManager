import json
import datetime
import sys

def reader(filename = "tasks.json"):
    with open(filename, "r") as file:
        try:
            current = json.loads(file.read())
            if current is not None:
                 return current
            else:
                return {}
        except json.decoder.JSONDecodeError:
            sys.exit("Files Created Please Run Application Again.")


def loader(filename = "tasks.json"):
    tasks = None
    try:
        tasks = reader(filename)
    except FileNotFoundError:
        with open(filename, "w") as file:
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
                "display": "f",
                "bias": "p",
            }
            json.dump(settings, file)
            return settings

def displayer(tasks, bias):
    if bias == "p":
        temp = tasks
        n = 1
        print("    Format: Name, Start date, Deadline, Priority")
        for task in list(temp.keys()):
            if tasks[task][2] == "h":
                print(f"{n} | {task}, {temp[task][0]}, {temp[task][1]}, High ")
                temp.pop(task)
                n += 1
        for task in list(temp.keys()):
            if tasks[task][2] == "m":
                print(f"{n} | {task}, {temp[task][0]}, {temp[task][1]}, Medium ")
                temp.pop(task)
                n += 1
        for task in list(temp.keys()):
            if tasks[task][2] == "l":
                print(f"{n} | {task}, {temp[task][0]}, {temp[task][1]}, Low ")
                temp.pop(task)
                n += 1
        for task in list(temp.keys()):
            print(f"{n} | {task}, {temp[task][0]}, {temp[task][1]}, {temp[task][2]}.upper() ")
            temp.pop(task)
            n +=1
        input("Press Enter to continue...")
    elif bias == "t":
        holder = 20000
        temp = tasks
        current_formatted_time = datetime.datetime.now().strftime("%Y-%m-%d-%H")
        for _ in enumerate(tasks):
            for task in list(tasks.keys()):
                deadline_formatted = datetime.datetime.strptime(tasks[task][1],"%Y-%m-%d-%H")
                delta = deadline_formatted - current_formatted_time
                if delta > holder:
                    delta = holder
                    print(delta)


