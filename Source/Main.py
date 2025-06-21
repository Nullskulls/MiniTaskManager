import json
import sys
import Manipulator

def placeholder(): print("W")

def main():
    settings = Manipulator.settings_loader()
    tasks = Manipulator.loader(settings["file_name"])
    while True:

        user_input = input("[1] Add Task \n[2] Remove Task \n[3] Edit Task \n[0] Exit ")
        match user_input:
            case "1":
                placeholder()
                #To Do
            case "2":
                placeholder()
                #To Do
            case "3":
                placeholder()
                #To do
            case "4":
                sys.exit("Exited successfully. \n")

if __name__ == "__main__":
    main()