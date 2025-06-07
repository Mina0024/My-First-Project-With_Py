import json
import os

# Load user data
if os.path.exists("users.json"):
    with open("users.json", "r") as file:
        Data = json.load(file)
else:
    Data = {}

# Load tasks
if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        All_tasks = json.load(file)
else:
    All_tasks = {}


print('''=============================
    Task Manager App
=============================

1. Register 
2. Login
3. Exit

=============================''')

Turn_on = True




email = ""
user_To_Do_list = {

}


while Turn_on is True:
    choice = input("choose an option: ")
    if choice == "1":
        print("you chose: Register ")
        email = input("Enter username: ")
        if email.strip() == "":
            print("You Must Write words")

        else:
           password = input("Enter password (Character 8) : ")

           if len(password) < 8:
               print("Password must be more than 8 Character")

           else:
                confirm_password = input("Confirm password: ")

                if confirm_password == password:
                     print("user registered successfully!")
                     Data.update({email: confirm_password})
                     with open("users.json", "w") as file:
                         json.dump(Data, file)


                else:
                       print("confirm password is wrong, Try again")
                       password = input("Enter password: ")
                       confirm_password = input("Confirm password:")
                       Data.update({email: confirm_password})
                       with open("users.json", "w") as file:
                           json.dump(Data, file)

                       if confirm_password == password:
                            print("user registered successfully!")

                       else:
                         print("something went wrong, try again")


    elif choice == "2":
        print("you chose: Login")
        log = input("Enter username: ")
        pass_w = input("Enter password: ")

        if  log in Data and Data[log] == pass_w:
                print("login successful!")
                print(''' === Task Organizer ===
                1. Add Task
                2. View Tasks
                3. Delete Task
                4. Log out''')
                Turn_on = True
                Task_list = All_tasks.get(log, [])
                user_To_Do_list.update({email: Task_list})
                while Turn_on is True:
                    choice = input("Choose an option: ")
                    if choice == "1":
                        Task = input("Enter Your Task Name: ").capitalize()
                        Task_list.append(Task)
                        All_tasks[log] = Task_list
                        with open("tasks.json", "w") as file:
                            json.dump(All_tasks, file)

                        print("Task Saved!")
                    elif choice == "2":
                        if Task_list:
                            for Task in Task_list:
                                print("- " + Task)
                        else:
                            print("no tasks yet.")
                    elif choice == "3":
                        Delete = input("Enter Name Task: ").capitalize()
                        if Delete in Task_list:
                            Task_list.remove(Delete)
                            with open("tasks.json", "w") as file:
                                json.dump(All_tasks, file)

                            print("Task Deleted.")
                        else:
                            print("Task not found.")


                    elif choice == "4":
                        print("log out")
                        break


                    else:
                        print("I Don't understand")



        else:
                print("wrong Name or Password, try again.")



    elif choice == "3":
        print("App Exit")
        Turn_on = False
        with open("users.json", "w") as file:
            json.dump(Data, file)

        with open("tasks.json", "w") as file:
            json.dump(All_tasks, file)

    elif choice == "admin":
        turn_on = True



        PassWord = input("Enter The PassKey: ")
        if PassWord == "master":
            print("Hello Master")
            print('''1. View All Users 
2.Search for User
3.Exit
''')
            while turn_on is True:
                 CHoice = input("Choose an option:")

                 if CHoice == "1":
                      for email in Data:
                         print("-" + email)

                 elif CHoice == "2":
                       search = input("enter username: ")
                       if search in Data:
                            print("user found")
                       else:
                         print("user not found")

                 elif CHoice == "3":
                     print("Goodbye Master")
                     break
        else:
                print("You aren't The Master")


    else:
        print("Sorry I Don't understand")

