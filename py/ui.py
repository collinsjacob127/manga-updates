import json
print("All manga positions")
print("#########################################################################")

try:
    with open("data.json") as f:
        data = json.load(f)
        for obj in data:
            title = obj["title"]
            last_updated = obj["last_updated"]
            current_chapter = obj["current_chapter"]
            print("----------------------------------------------------------------------")
            print(f"{title} \nLast updated: {last_updated} \n{current_chapter} ")
except FileNotFoundError:
    # If the file does not exist, use the default values from the objects
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Encountered a file not found error")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    pass
