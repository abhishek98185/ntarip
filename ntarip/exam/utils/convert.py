import json 
def get_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
new_dict = {}
nemerical_dict = {}
physics = []
chemistry = []
maths = []

numerical_physics = []
numerical_chemistry = []
numerical_maths = []
data = get_json('ntarip/exam/static/json/test.json')
for paper in data:
    options = paper.get("options")
    if options:
        if paper["question_number"] <= 25:
            # new_dict["Maths"] = paper 
            maths.append(paper)
        elif paper["question_number"] <= 50:
            # new_dict["Physics"] = paper
            physics.append(paper)
        elif paper["question_number"] <= 75:
            # new_dict["Chemistry"] = paper
            chemistry.append(paper)
    else:
        if paper["question_number"] <= 25:
            # new_dict["Maths"] = paper 
            numerical_maths.append(paper)
        elif paper["question_number"] <= 50:
            # new_dict["Physics"] = paper
            numerical_physics.append(paper)
        elif paper["question_number"] <= 75:
            # new_dict["Chemistry"] = paper
            numerical_chemistry.append(paper)
new_dict["Maths"] = maths
new_dict["Physics"] = physics
new_dict["Chemistry"] = chemistry

nemerical_dict["Maths"] = numerical_maths
nemerical_dict["Physics"] = numerical_physics
nemerical_dict["Chemistry"] = numerical_chemistry
with open('ntarip/exam/static/json/jeemains28(2)jan2025_mcq.json', 'w', encoding='utf-8') as file:
    json.dump(new_dict, file, indent=4, ensure_ascii=False)
with open('ntarip/exam/static/json/jeemains28(2)jan2025_numerical.json', 'w', encoding='utf-8') as file:
    json.dump(nemerical_dict, file, indent=4, ensure_ascii=False)