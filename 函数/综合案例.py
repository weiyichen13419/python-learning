
def calc_total(*nums):
   """
   计算总运动量（个）
   :param nums:每一天的运动量 
   :return: 总运动量（个）
   """
   return sum(nums)

def calc_avg(total,days=7):
    """
    计算平均值
    :param total:总运动量(个) 
    :param days: 天数（默认为7）
    :return: 平均值
    """
    return total/days

def check_success(total,goal=120):
    """
    判断挑战是否成功
    :param total:总运动量
    :param goal: 目标运动量
    :return:判定
    """
    if total > goal:
        return '恭喜！挑战成功！'
    else:
        return'抱歉，挑战失败！'

def main(title,duration):
    """

    :param title: 比赛项目
    :param duration: 比赛天数
    :return: 
    """
    print(f'[{title}] [{duration}]天挑战赛，请输入每天的数量')
    num1=int(input('第1天:'))
    num2 = int(input('第2天:'))
    num3 = int(input('第3天:'))
    num4 = int(input('第4天:'))
    num5 = int(input('第5天:'))
    num6 = int(input('第6天:'))
    num7 = int(input('第7天:'))

    total=calc_total(num1,num2,num3,num4,num5,num6,num7)
    avg=calc_avg(total)
    result = check_success(total)
    print(f'[{title}] [{duration}]健身总结')
    # print('总数:%d,平均值:%.1f' %(total,avg))
    print(f'总数：{total},平均值：{avg:.1f}')
    print(result)

main('仰卧起坐',7)