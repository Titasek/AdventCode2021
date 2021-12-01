with open('data') as input_datas:
    datas = [int(line.strip()) for line in input_datas.readlines()]

answer = 0

for i in range(1, len(datas)):
    if datas[i]>datas[i-1]: answer += 1
    
print(answer)