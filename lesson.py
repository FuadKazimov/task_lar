
#Task1
# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# print("Adamin adi:", person["name"])
# print("Adamin yaşi:", person["age"])
#----------------------------------------------------------------------------------
#Task2
# student = {
#     "name": "John",
#     "grades": {
#         "math": 90,
#         "science": 85,
#         "history": 88
#     }
# }
# print("Telebenin elmi derecesi:", student["grades"]["science"])
#-----------------------------------------------------------------------------------
#Task3

# inventory = {
#     "apples": 10,
#     "bananas": 5,
#     "oranges": 8
# }
# for fruit, quantity in inventory.items():
#     print(fruit, quantity)
#----------------------------------------------------------------------------------
#Task4

# employees = [
#     {"name": "Alice", "role": "Developer", "age": 30},
#     {"name": "Bob", "role": "Designer", "age": 28},
#     {"name": "Charlie", "role": "Manager", "age": 35}
# ]
# for employee in employees:
#     if employee["age"] < 30:
#         print(employee["name"])
#---------------------------------------------------------------------------------
#Task5
# data = {
#     "company": "TechCorp",
#     "departments": {
#         "development": {
#             "employees": [
#                 {"name": "Alice", "role": "Developer", "projects": ["App1", "App2"]},
#                 {"name": "Bob", "role": "Developer", "projects": ["App3"]},
#                 {"name": "Mark", "role": "Lead", "projects": []}
#             ]
#         },
#         "design": {
#             "employees": [
#                 {"name": "Charlie", "role": "Designer", "projects": ["Design1"]},
#                 {"name": "Diana", "role": "Designer", "projects": []}
#             ]
#         }
#     }
# }
# for employee in data["departments"]["development"]["employees"]:
#     project_count = len(employee["projects"])
#     if project_count > 0:
#         print(f"{employee['name']} - Layihələr: {project_count}")
#     else:
#         print(f"{employee['name']} - Layihə yoxdur")