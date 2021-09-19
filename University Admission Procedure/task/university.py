import hashlib


def assign_to_department(choice, department):
    print(f"Process {choice}. department {department}")
    if department == "Physics":
        used_dict = physics_scores
        score_position = 1
    elif department == "Chemistry":
        used_dict = chemistry_scores
        score_position = 2
    elif department == "Biotech":
        used_dict = biotech_scores
        score_position = 5
    elif department == "Mathematics":
        used_dict = mathematics_scores
        score_position = 3
    else:
        used_dict = engineering_scores
        score_position = 4

    remove_candidates = []
    for id, candidate in used_dict.items():
        if candidate[choice + 6] == department and len(departments.get(department)) < number_applicants:
            departments[department].append([candidate[0], max(candidate[score_position], candidate[6])])
            remove_candidates.append(id)
    remove_applicant(remove_candidates)


def remove_applicant(remove_candidates):
    for id in remove_candidates:
        physics_scores.pop(id, None)
        chemistry_scores.pop(id, None)
        mathematics_scores.pop(id, None)
        engineering_scores.pop(id, None)
        biotech_scores.pop(id, None)


def read_applicants():
    global physics_scores
    global chemistry_scores
    global mathematics_scores
    global engineering_scores
    global biotech_scores

    with open("applicant_list.txt", "r") as file:
        for applicant in [line[:-1].split(" ") for line in file]:
            physic_score = float(applicant[2])
            chemistry_score = float(applicant[3])
            math_score = float(applicant[4])
            computer_score = float(applicant[5])
            mean_score = float(applicant[6])
            data = [
                f"{applicant[0]} {applicant[1]}", round((physic_score + math_score) / 2, 1), chemistry_score, math_score,
                round((computer_score + math_score) / 2, 1), round((physic_score + chemistry_score) / 2, 1),
                mean_score, applicant[7], applicant[8], applicant[9]
            ]
            id = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
            physics_scores[id] = data
            chemistry_scores[id] = data
            mathematics_scores[id] = data
            engineering_scores[id] = data
            biotech_scores[id] = data
        file.close()


def sort_dictionaries():
    global physics_scores
    global chemistry_scores
    global mathematics_scores
    global engineering_scores
    global biotech_scores

    physics_scores = dict(sorted(physics_scores.items(), key=lambda item: (-max(item[1][1], item[1][6]), item[1][0])))
    chemistry_scores = dict(sorted(chemistry_scores.items(), key=lambda item: (-max(item[1][2], item[1][6]), item[1][0])))
    mathematics_scores = dict(sorted(mathematics_scores.items(), key=lambda item: (-max(item[1][3], item[1][6]), item[1][0])))
    engineering_scores = dict(sorted(engineering_scores.items(), key=lambda item: (-max(item[1][4], item[1][6]), item[1][0])))
    biotech_scores = dict(sorted(engineering_scores.items(), key=lambda item: (-max(item[1][5], item[1][6]), item[1][0])))


number_applicants = int(input())
physics_scores = dict()
chemistry_scores = dict()
mathematics_scores = dict()
engineering_scores = dict()
biotech_scores = dict()
read_applicants()
sort_dictionaries()

departments_name = ["Physics", "Chemistry", "Mathematics", "Engineering", "Biotech"]
departments = dict()

for position in range(1, 4):
    for department_name in departments_name:
        if position == 1:
            departments[department_name] = []
        assign_to_department(position, department_name)

department_keys = sorted(departments.keys())

for department_name in departments_name:
    departments.get(department_name).sort(key=lambda admitted: (-admitted[1], admitted[0]))
    with open("{}.txt".format(department_name.lower()), "w") as file_results:
        for admitted_applicant in departments.get(department_name):
            file_results.write(f"{admitted_applicant[0]} {admitted_applicant[1]}")
            file_results.write('\n')
    file_results.close()
