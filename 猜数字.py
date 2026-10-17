import random
print('欢迎来到猜数字挑战，接下来我会在1-100中随机挑选一个数字,你有七次机会去猜测')
num=random.randint(1,100)
chance=1
while True:
    word = int(input('请输入你猜测的数字：'))
    chance+=1
    print(f'你还有{7 - chance}次机会')
    if chance > 6:
        break

    if word>num:
        print('大了，请重新猜测')
        continue
    elif word<num:
        print('小了，请重新猜测')
        continue
    else:
        print('恭喜你！猜中了！')
        break
