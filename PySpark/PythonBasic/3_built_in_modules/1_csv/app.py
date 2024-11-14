# import csv

# myData = [
#     ["fname", "lname", "city"],
#     ["Manish", "Sharma", "Pune"],
#     ["Abhijeet", "Gole", "Pune"],
#     ["Pravin", "Dabade", "Mumbai"],
#     ["Sumeet", "Wajpe", "Mumbai"],
# ]

# myFile = open("test.csv", "w", newline="")

# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)

# print("CSV file created....")

# -------------------------------- Read
import csv
import collections
from pprint import pprint as pp

# with open("test.csv") as file:
#     reader = csv.reader(file, delimiter=",")

#     for row in reader:
#         print(row)

# with open("test.csv") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row)


results = []

with open("test.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        results.append(row)

# print(results)
grouped = collections.defaultdict(list)
# print(grouped)

for item in results:
    grouped[item["city"]].append(item)

pp(grouped)
