def calc_total(*nums):
    return sum(nums)
def calc_avg(total,days):
    return total/days
def check_success(total,goals):
    if total > goals:
        return '恭喜你完成挑战'
    else:
        return '抱歉，挑战失败'
def main(title,duration,goals):
    print(f'[{title}] [{duration}]天挑战赛正式开始,目标为{goals}')
    num1 =int(input('第1天：'))
    num2 =int(input('第2天：'))
    num3 =int(input('第3天：'))
    total=calc_total(num1,num2,num3)
    avg=calc_avg(total,duration)
    result=check_success(total,goals)
    print(f'完成总数:{total},平均值:{avg:.1f}')
    print(result)
main('仰卧起坐',3,80)
