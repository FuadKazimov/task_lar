schedule = {}
def add_subject(schedule, name, subject):
    if name not in schedule:
        schedule[name] = set()
    schedule[name].add(subject)

def remove_subject(schedule, name, subject):
    if name in schedule and subject in schedule[name]:
        schedule[name].remove(subject)
        if not schedule[name]:
            del schedule[name]
def get_subjects(schedule, name,):
    return schedule.get(name, set())

def get_all_students(schedule):
    return schedule

def count_subjects(schedule, name):
    return len(schedule.get(name, []))

add_subject(schedule, "Fuad", "Informatika")
add_subject(schedule, "Emin", "Riyaziyyat")
add_subject(schedule, "Fuad", "Fizika")

print(get_subjects(schedule, "Fuad"))
print(get_all_students(schedule))
print(count_subjects(schedule, "Fuad"))

remove_subject(schedule, "Fuad", "Riyaziyyat")
print(get_subjects(schedule, "Fuad"))

