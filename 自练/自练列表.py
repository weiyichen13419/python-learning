print('请开始输入成绩：')

score_list=[]
while True:
    scores=input('学生成绩为：')
    if scores=='结束':
        break
    else :
        score_list.append(int(scores))

if len(score_list)>0:
    print('学生成绩输入完毕')
    pass_list=[]
    excellent_list=[]
    for score in score_list:
        if 60<score<90:
            pass_list.append(score)
        elif score>90:
            excellent_list.append(score)
    print(f'总人数为{len(score_list)}')
    print(f'平均分为{sum(score_list)/len(score_list)}')
    print(f'优秀率{len(excellent_list)/len(score_list)*100:.1f}%')
    print(f'及格率{len(pass_list)/len(score_list)*100:.1f} ')
else:
    print('您暂未输入任何成绩')