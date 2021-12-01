with open('data') as input_datas:
    datas = [int(line.strip()) for line in input_datas.readlines()]

answer = 0
sum_list = []

for i in range(len(datas)-2):
    sum_list.append(sum(datas[i:i+3]))

for i in range(1, len(sum_list)):
    if sum_list[i]>sum_list[i-1]: answer += 1
    
print(answer)