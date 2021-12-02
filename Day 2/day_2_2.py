with open('data') as input_datas:
    datas = [line.strip() for line in input_datas.readlines()]

position = 0
depth = 0
aim = 0

for data in datas:
    mov, val = data.split(" ")
    
    if mov == "forward":
        position += int(val)
        depth += (aim * int(val))
    elif mov == "down":
        aim += int(val)
    elif mov == "up":
        aim -= int(val)

print(position*depth)