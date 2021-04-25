import random
num = int(input("로또 숫자 받고싶은만큼 입력하세요 : "))


print("미래를 바꿔줄 숫자가 나올것입니다.")
print("-----------절취선-----------")
for x in range(1, num+1):
    lotto = [0, 0, 0, 0, 0, 0]

    lotto[0] = random.randrange(1, 46, 1)

    lotto[1] = lotto[0]
    lotto[2] = lotto[0]
    lotto[3] = lotto[0]
    lotto[4] = lotto[0]
    lotto[5] = lotto[0]

    while (lotto[0] == lotto[1]):
        lotto[1] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[2] or lotto[1] == lotto[2]):
        lotto[2] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[3] or lotto[1] == lotto[3] or lotto[2] == lotto[3]):
        lotto[3] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[4] or lotto[1] == lotto[4] or lotto[2] == lotto[4] or lotto[3] == lotto[4]):
        lotto[4] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[5] or lotto[1] == lotto[5] or lotto[2] == lotto[5] or lotto[3] == lotto[5] or lotto[4] == lotto[5]):
        lotto[5] = random.randrange(1, 46, 1)


    lotto.sort() 
    print(lotto)
dic = {"조상님":"저에게 힘을주세요!"}
print("-----------절취선-----------")
print(dic)
