import random

print("💚 Exercice 1 – Group students by project")

def pick_random_name(list_names):
    return random.choice(list_names)

def group_students_by_project(students):
    projects = {"Project A": [], "Project B": []}
    for student in students:
        projects[student["choice"]].append(student["name"])

    def make_group(names):
        paires = []
        while len(names) > 1:
            name1 = pick_random_name(names)
            names.remove(name1)
            name2 = pick_random_name(names)
            names.remove(name2)
            paires.append([name1, name2])
        if names:  # If there's an odd one out
            paires.append([names[0]])
        return paires

    return make_group(projects["Project A"]) + make_group(projects["Project B"])

students = [
    {"name": "Jane", "choice": "Project B"},
    {"name": "Janet", "choice": "Project A"},
    {"name": "Jack", "choice": "Project A"},
    {"name": "Jimmy", "choice": "Project B"},
    {"name": "Jean", "choice": "Project A"},
    {"name": "Juan", "choice": "Project B"},
    {"name": "Juanita", "choice": "Project B"},
    {"name": "Janine", "choice": "Project A"},
    {"name": "Jill", "choice": "Project B"},
    {"name": "John", "choice": "Project B"},
]

groups = group_students_by_project(students)
for i, group in enumerate(groups, 1):
    print(f"Paire {i} : {group}")


print("\n💚 Exercice 4 – Mask credit card number")

sample_credit_card_number = '1234567890987654'
expected_credit_card_result = 'XXXXXXXXXXXX7654'

def mask_credit_card_number(credit_card_number):
    masked_credit_card_number = ''
    for i in range(len(credit_card_number)):
        if i < len(credit_card_number) - 4:
            masked_credit_card_number += 'X'
        else:
            masked_credit_card_number += credit_card_number[i]
    return masked_credit_card_number

print('Expected result: ', expected_credit_card_result)
result = mask_credit_card_number(sample_credit_card_number)
print('Your result:     ', result)


print("\n🔢 Bonus – Find the largest number")

list_of_numbers = [1, 7, 3, 8, 5, 0]
max_number = list_of_numbers[0]

for number in list_of_numbers:
    if number > max_number:
        max_number = number

print("The largest number is:", max_number)
