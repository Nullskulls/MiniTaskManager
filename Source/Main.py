import datetime
import sys
import Manipulator


def placeholder(): print("W")

def main():
    settings = Manipulator.settings_loader()
    tasks = Manipulator.loader(settings["task_list"])
    while True:

        user_input = input("[1] Add Task \n[2] Remove Task \n[3] Edit Task \n[4] Display\n[0] Exit \n$")
        match user_input:
            case "1":
                task_name = input("Enter Task Name: ")
                current_datetime = datetime.datetime.now()
                deadline = input("Enter Deadline: \nFormat YYYY-MM-DD-HH\n$")
                priority = input("Enter Priority: \nH: High.\nM: Medium.\nL: Low.\n$")
                tasks[task_name.lower()] = [str(current_datetime), deadline, priority[0]]
                Manipulator.saver(tasks)
            case "2":
                task_name = input("Task name: ").lower()
                confirmation = input("Are you sure? (y/n) ")
                if confirmation[0].lower() == "y" and len(confirmation) < 20:
                    tasks.pop(task_name)
                    print("Task removed! \n")
                    Manipulator.saver(tasks)
                else:
                    print("Canceling...")
                    continue
            case "3":
                task_name = input("Task name: ")
                confirmation = input("Are you sure? (y/n) ")
                while True:
                    if confirmation[0].lower() == "y" and len(confirmation) < 20:
                        edit_choice = input("What would you like to edit?\n[1] Task Name\n[2] Start Date\n[3] Deadline\n[4] Priority\n[5] Settings\n[0] Cancel\n$ ")
                        match edit_choice:
                            case "1":
                                new_task_name = input("Enter New Task Name: ")
                                tasks[new_task_name.lower()] = tasks[task_name.lower()]
                                tasks.pop(task_name.lower())
                                Manipulator.saver(tasks)
                                print("Name Changed! \n")
                            case "2":
                                new_start_date = input("Enter New Start Date.\nFormat YYYY-MM-DD-HH Or Current For The Current Date And Time\n$ ")
                                if new_start_date.lower() == "current":
                                    new_start_date = datetime.datetime.now()
                                tasks[task_name.lower()][0] = new_start_date
                                Manipulator.saver(tasks)
                                print("Start Date Modified! \n")
                            case "3":
                                new_dead_line = input("Enter New Deadline.\nFormat YYYY-MM-DD-HH\n$ ")
                                tasks[task_name.lower()][0] = new_dead_line
                                Manipulator.saver(tasks)
                                print("Start Date Modified! \n")
                            case "4":
                              new_priority = input("New Priority?\nH: High.\nM: Medium.\nL: Low.\n$ ").lower()[0]
                              tasks[task_name.lower()][2] = new_priority
                            case "0":
                                print("Canceling...")
                                break
            case "4":
                placeholder()
            case "6":
                setting = input("Which Setting Would You Like To Change?\n[1] Sorting Bias\n[2] Display On Entry")
                match setting:
                    case "1":
                        bias = input("What Would You Like To Sort Based Off Of?\n[1] Priority\n [2] Timeline\n**Note: Default Is Priority**")
                placeholder()
            case "0":
                sys.exit("Exited successfully. \n")

if __name__ == "__main__":
    main()
