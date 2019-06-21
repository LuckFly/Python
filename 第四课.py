print("------------开始游戏-------------------------")
import  random
sec = random.randint(1,10)
print (sec)
temp = input('请输入一个我心目中的数字：')
guess =  int (temp)
i = 3
while (guess != sec) and (i >= 1):
    i = i - 1
    temp = input('错了，请重新输入：')
    guess = int(temp)
    if guess == sec:
        print('猜对了！')
        print("不玩了！")
        i = i - 1
    else:
        if guess > sec:
            print('大了大了')
            i = i - 1
        else:
            print('小了小了')
            i = i - 1
    print('你还有，%d 机会，请珍惜！' % i)
if guess == sec:
    print ("输入正确！一次pass")
else:
    print("游戏结束！")

