age = int(input("enter your age"))
has_report = input('yes or no')
level = int(input('enter the level'))
if 18 <= age <= 45:
    print('您的年龄符合要求')
    if has_report == 'yes':
        print('您已提交报告')
        print('可以参加比赛')
        if level == 1:
            print(f'尊贵的{level}级会员,你可以得到T恤')
        elif level == 2:
            print(f'尊贵的{level}级会员,你可以得到跑鞋')
        elif level == 3:
            print(f'尊贵的{level}级会员,你可以得到耳机')
    elif has_report == 'no':
        print('您未提交报告，不可参赛')
else:
    print('您的年龄不符合要求')
