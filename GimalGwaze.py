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
print("----------절취선----------")
print('조상님 저에게 힘을주세요!')

print("딕쇼나리")
dic = {'test1':'사과',
       'test2':'배',
       'test3':'사자'}
keys = list(dic.keys())
random.shuffle(keys)

count = 0
for test in keys:
    keword = dic[test]
    g = input('{} 몇번을 테스트할건치 치세요:')
    if g == keword:
        print('입니다')
    else:
        print('이상한거 하지마세요')
print("끝났습니다.")        
#딕쇼나리 어렵덩...