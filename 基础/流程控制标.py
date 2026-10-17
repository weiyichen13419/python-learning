print('欢迎来到答题闯关挑战赛')
ques1,ans1 ="python中输出的函数是什么","print"
ques2,ans2 ="python中表示逻辑”并且的关键字是","and"
ques3,ans3 ="python属于解释型还是编译型","解释型"
in_playing=True
max_tries=3
total_levels=3

for level in range(1,total_levels+1):
    print(f'这是第{level}个问题')
    if level==1:
        question,answer=ques1,ans1
    elif level==2:
        question,answer=ques2,ans2
    else :
        question,answer=ques3,ans3


    tries=1
    while tries<=max_tries:
        user_input = input(question)
        if user_input == answer:
            print('回答正确！')
            break
        elif user_input=='':
            print('输入为空，请重新输入:')
            continue
        elif user_input == 'q':
           in_playing=False
           break
        else:
            leave=max_tries-tries
            if  leave>0:
                print(f'回答错误，您还有{max_tries-tries}次机会')
                tries+=1
                continue
            else:
                 print(f'😢挑战失败，本题的正确答案是：{answer}，游戏结束！')
                 in_playing = False
                 break

    if  in_playing==False:
        print('您已退出游戏')
        break
if in_playing==True:
    print('恭喜通关')






