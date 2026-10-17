print('欢迎来到答题闯关挑战赛')
rank1 = 1
for rank in range(1, 4):
    print(f'现在为第{rank}小题')

    answer = input('请输入答案：')

    if answer =='':
        while answer =='':
            print('输入不能为空，请重新作答(此次不计入作答次数)')
            answer = input('请重新输入答案：')
        while answer != '':
            break

    elif answer =='true':
        print(f'恭喜你回答正确，进入第{rank+1}小题')
        continue

    elif answer != 'true' and answer != '':
       while rank1<3:

            answer = input('回答错误，请重新请输入答案:')

            if answer != 'true' and answer != '':
                rank1 += 1

                if rank1 <=2:
                     continue

            elif answer == '':
                while answer == '':
                      print('输入不能为空，请重新作答(此次不计入作答次数)')
                      answer = input('请重新输入答案：')
                      if answer != 'true' and answer != '':
                          rank1 += 1
                          if rank1 > 2:
                              print('此题累计答错三次，游戏结束')

                      elif answer == 'true':
                           print(f'恭喜你回答正确，进入第{rank + 1}小题')
            break

    if rank1>2 :
        print('此题累计答错三次，游戏结束')
        break




