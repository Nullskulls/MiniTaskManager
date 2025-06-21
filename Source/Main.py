import datetime
import sys
import Manipulator


def placeholder(): print("W")

def main():
    settings = Manipulator.settings_loader()
    tasks = Manipulator.loader(settings["task_list"])
    filename = settings["task_list"]
    if settings["display"] == "t":
        Manipulator.displayer(tasks, settings["bias"])
    while True:

        user_input = input("[1] Add Task \n[2] Remove Task \n[3] Edit Task \n[4] Display\n[5] Settings\n[0] Exit \n$ ")
        match user_input:
            case "1":
                task_name = input("Enter Task Name: ")
                current_datetime = datetime.datetime.now()
                deadline = input("Enter Deadline: \nFormat YYYY-MM-DD-HH\n$ ")
                priority = input("Enter Priority: \nH: High.\nM: Medium.\nL: Low.\n$ ")
                tasks[task_name.lower()] = [str(current_datetime), deadline, priority[0]]
                Manipulator.saver(tasks, filename)
            case "2":
                task_name = input("Task name: ").lower()
                confirmation = input("Are you sure? (y/n) ")
                if confirmation[0].lower() == "y" and len(confirmation) < 20:
                    tasks.pop(task_name)
                    print("Task removed! \n")
                    Manipulator.saver(tasks, filename)
                else:
                    print("Canceling...")
                    continue
            case "3":
                task_name = input("Task name: ")
                confirmation = input("Are you sure? (y/n): ")
                while True:
                    if confirmation[0].lower() == "y" and len(confirmation) < 20:
                        edit_choice = input("What would you like to edit?\n[1] Task Name\n[2] Start Date\n[3] Deadline\n[4] Priority\n[0] Cancel\n$ ")
                        match edit_choice:
                            case "1":
                                tasks = Manipulator.loader(filename)
                                new_task_name = input("Enter New Task Name: ")
                                tasks[new_task_name.lower()] = tasks[task_name.lower()]
                                tasks.pop(task_name.lower())
                                Manipulator.saver(tasks, filename)
                                print("Name Changed! \n")
                            case "2":
                                tasks = Manipulator.loader(filename)
                                new_start_date = input("Enter New Start Date.\nFormat YYYY-MM-DD-HH Or Current For The Current Date And Time\n$ ")
                                if new_start_date.lower() == "current":
                                    new_start_date = datetime.datetime.now()
                                tasks[task_name.lower()][0] = new_start_date
                                Manipulator.saver(tasks, filename)
                                print("Start Date Modified! \n")
                            case "3":
                                tasks = Manipulator.loader(filename)
                                new_dead_line = input("Enter New Deadline.\nFormat YYYY-MM-DD-HH\n$ ")
                                tasks[task_name.lower()][1] = new_dead_line
                                Manipulator.saver(tasks, filename)
                                print("Start Date Modified! \n")
                            case "4":
                              tasks = Manipulator.loader(filename)
                              new_priority = input("New Priority?\nH: High.\nM: Medium.\nL: Low.\n$ ").lower()[0]
                              tasks[task_name.lower()][2] = new_priority
                            case "0":
                                print("Canceling...")
                                break
            case "4":
                Manipulator.displayer(tasks, settings["bias"])
            case "5":
                setting = input("Which Setting Would You Like To Change?\n[1] Sorting Bias\n[2] Display On Entry\n[3] Task Save List\n$ ")
                match setting:
                    case "1":
                        bias = input("What Would You Like To Sort Based Off Of?\n[P] Priority\n[T] Timeline\n**Note: Default Is Priority**\n$ ")
                        settings["bias"] = bias.lower()
                        Manipulator.saver(filename="preferences.json", data=settings)
                    case "2":
                        boolean_entry = input("Would You Like To Display On Entry?\n[T] True\n[F] False\n**Note: Default Is False**\n$ ")
                        settings["display"] = boolean_entry[0].lower()
                        Manipulator.saver(filename="preferences.json", data=settings)
                    case "3":
                        settings["task_list"] = input("New File Name?\nExample: Tasks.json/Assignments.json..\n$ ")
                        Manipulator.saver(filename="preferences.json", data=settings)
                        filename = settings["task_list"]
                        Manipulator.saver(filename=filename, data=tasks)
                        sys.exit("Please Restart the Task Tracker.")
            case "0":
                sys.exit("Exited successfully. \n")

if __name__ == "__main__":
    main()
