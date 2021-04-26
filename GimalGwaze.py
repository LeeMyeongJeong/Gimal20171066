import random
num = int(input("로또 몇장드릴까요? : "))

print("-----------절취선-----------")
for x in range(1, num+1):
    l = [0, 0, 0, 0, 0, 0]

    l[0] = random.randrange(1, 46, 1)

    l[1] = l[0]
    l[2] = l[0]
    l[3] = l[0]
    l[4] = l[0]
    l[5] = l[0]

    while (l[0] == l[1]):
        l[1] = random.randrange(1, 46, 1)
    while (l[0] == l[2] or l[1] == l[2]):
        l[2] = random.randrange(1, 46, 1)
    while (l[0] == l[3] or l[1] == l[3] or l[2] == l[3]):
        l[3] = random.randrange(1, 46, 1)
    while (l[0] == l[4] or l[1] == l[4] or l[2] == l[4] or l[3] == l[4]):
        l[4] = random.randrange(1, 46, 1)
    while (l[0] == l[5] or l[1] == l[5] or l[2] == l[5] or l[3] == l[5] or l[4] == l[5]):
        l[5] = random.randrange(1, 46, 1)


    l.sort() 
    print(l)
print("----------절취선----------")
d = {'d1':'히히 딕셔너리 성공햇덩 ',
    'd2':'너무조왕 ',
    'd3':'아이조왕'}    
print(f'{d["d1"] + d["d2"] + d["d3"]}')    
print("----------절취선----------")
