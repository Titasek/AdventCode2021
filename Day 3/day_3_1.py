with open('data') as input_datas:
    datas = [line.strip() for line in input_datas.readlines()]

answer = 0
gamma = ""
epsilon = ""

for i in range(len(datas[0])):
    dict = {
        "0": 0,
        "1": 0
    }
    for data in datas:
        if data[i] == "0": dict["0"] += 1
        else: dict["1"] += 1

    if dict["0"]>dict["1"]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))