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