with open('data') as input_datas:
    datas = [line.strip() for line in input_datas.readlines()]

position = 0
depth = 0
aim = 0

for data in datas:
    mov, val = data.split(" ")
    
    if mov == "forward":
        position += int(val)
    elif mov == "down":
        depth += int(val)
    elif mov == "up":
        depth -= int(val)

print(position*depth)