score_list=[]
while True:
    data=input('请输入学生成绩：')
    if data=='结束':
        break
    else :
        score_list.append(int(data))
if score_list:
    avg=sum(score_list)/len(score_list)

    pass_list=0
    excellent_list=0
    for score in score_list:
        if score>=60:
            pass_list+=1
        if score>=90:
            excellent_list+=1

    passp=pass_list/len(score_list)*100
    excellentp=excellent_list/len(score_list)*100
    print(f'平均分为{avg}')
    print(f'优秀率为{excellentp:.1f}%')
    print(f'及格率为{passp:.1f}%')
else :
    print('成绩单为空')
