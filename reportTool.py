def log_filter():
    user_input = input("Please choose one of the following (User Sessions / Config Report / Daemon Exits):\n")
    options = ["user sessions", "config report", "daemon exits"]

    while user_input.lower() not in options:
        user_input = input("Uh Oh! Invalid input, select type (user sessions / config report / daemon exits):\n")
    else:

        if user_input.lower() in options[0].lower():
            print("Please wait while I fetch the data...")
            f = open("Lucid.log", "r", encoding="Latin-1")
            lines = f.readlines()
            service = "| UserSessionActor |"
            count = 0
            for string in lines:
                if service in string:
                    count += 1
                    print(string)
            print(f"Total number of user session events: {count}\n")

        elif user_input.lower() in options[1].lower():
            print("Please wait while I fetch the data...")
            f = open("Lucid.log", "r", encoding="Latin-1")
            lines = f.readlines()
            service = "New config stored "
            count = 0
            for string in lines:
                if service in string:
                    count += 1
                    print(string)
            print(f"Total number of config logs: {count}\n")

        elif user_input.lower() in options[2].lower():
            print("Please wait while I fetch the data...")
            f = open("app.log", "r", encoding="Latin-1")
            lines = f.readlines()
            service = "Lucid daemon exited with code 1"
            count = 0
            for string in lines:
                if service in string:
                    count += 1
                    print(string)
            print(f"Total number of daemon exits: {count}\n")
        input("Press any key to exit")
