def calc_total(*nums):
    return sum(nums)
def calc_avg(total,duration):
    return total/duration
def check_success(total,goals):
    if total>goals:
        return'恭喜你完成挑战'
    else:
        return'很遗憾，挑战失败'
def main(title,duration,goals):
    nums=[]
    for index in range(duration):
        nums.append(int(input(f'第{index+1}天的个数是:')))
    total=calc_total(*nums)
    avg=calc_avg(total,duration)
    result=check_success(total,goals)

    print(f'【{title}】【{duration}天】健身总结')
    print(f'总数：{total}，平均值：{avg:.1f}')
    print(result)

main('俯卧撑', 3, 40)