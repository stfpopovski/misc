user_input = input("What would you like to do? (Get certain reports/Copy files to cloud): \n")
options = ["get certain reports", "reports", "copy files to cloud", "copy"]

while user_input.lower() not in options:
    user_input = input("Uh Oh! Typo. Try again: \n")
else:
    if user_input.lower() in options[0 or 1].lower():
        from reportTool import log_filter
        log_filter()

    elif user_input.lower() in options[2 or 3].lower():
        from copyTool import file_copy
        file_copy()
