import json
from dateutil import parser

from datetime import datetime, timedelta


def sort_chronologically(objects):
    # Create a list of tuples containing the object and its corresponding date
    dates = []
    bad = []
    for obj in objects:
        if "days ago" in obj["last_updated"]:
            # If the date string contains "days ago", try to parse the number of days and subtract it from the current date to get the equivalent date
            try:
                num_days = int(obj["last_updated"].split(" ")[0])
                equivalent_date = datetime.now() - timedelta(days=num_days)
                dates.append((obj, equivalent_date))
            except ValueError:
                # If the number of days is not a valid integer, skip this object
                continue
        else:
            # If the date string is a regular date, try to parse it and add it to the list
            try:
                regular_date = parser.parse(obj["last_updated"])
                dates.append((obj, regular_date))
            except ValueError:
                # If the date string is not in a recognized format, skip this object
                bad.append((obj, "-"))
                continue

    # Sort the list of tuples by the date

    sorted_dates = sorted(dates, key=lambda x: x[1], reverse=True)

    formatted_dates = []

    for date in sorted_dates:
        formatted = date[1].strftime("%d %B, %Y")
        formatted_dates.append((date[0], formatted))

    # Change bad objects to tuples 
    for date in bad:
        try:
            title = date[0]
            date = "-"
            formatted_dates.append((title, date))
        except:
            traceback.print_exc()
            print(f"Failed to pull from object{date}")

    return formatted_dates

# # Read the JSON file and update the objects with the values from the file
# try:
#     with open("data.json") as f:
#         data = json.load(f)
#         sorted_timestamps = sort_chronologically(data)
#         print("######################################")
#         print("################UNSORTED##############")
#         print("######################################")
#         for i, obj in enumerate(data):
#             title = obj["title"]
#             date = obj["last_updated"]
#             print(f"{i}. Title: {title}\n   L.U.: {date}")
#         print("######################################")
#         print("#################SORTED###############")
#         print("######################################")
#         for i, obj in enumerate(sorted_timestamps):
#             try:
#                 title = obj[0]["title"]
#                 date = obj[1]
#                 print(f"{i}. Title: {title}\n   L.U.: {date}")
#             except:
#                 print(i)
#                 print(obj)
# except FileNotFoundError:
#     # If the file does not exist, use the default values from the objects
#     print("file not found")
#     pass
