with open('data') as input_datas:
    O2 = [line.strip() for line in input_datas.readlines()]

answer = 0
CO2 = O2

i = 0
while len(O2)>1:
    temp = []
    dict = {
        "0": 0,
        "1": 0
    }
    for data in O2:
        if data[i] == "0": dict["0"] += 1
        else: dict["1"] += 1

    if dict["0"]>dict["1"]:
        for data in O2:
            if data[i] == "0": temp.append(data)
    else:
        for data in O2:
            if data[i] == "1": temp.append(data)
    
    O2 = temp
    i += 1

i = 0
while len(CO2)>1:
    temp = []
    dict = {
        "0": 0,
        "1": 0
    }
    for data in CO2:
        if data[i] == "0": dict["0"] += 1
        else: dict["1"] += 1

    if dict["0"]>dict["1"]:
        for data in CO2:
            if data[i] == "1": temp.append(data)
    else:
        for data in CO2:
            if data[i] == "0": temp.append(data)
    
    CO2 = temp
    i += 1

print(int(O2[0],2) * int(CO2[0], 2))