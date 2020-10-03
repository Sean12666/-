import numpy as np
import matplotlib.pyplot as plt


def drawPlan(plans, stu, time_len, bins, stat_time=10, note=''):
    for name, groups in plans.items():
        for i in range(groups):
            group_arr = np.random.normal(time_len / groups * (i + 1) - time_len / groups / 3,
                                         time_len / groups / 4, int(stu / groups))
            # plt.hist(group_arr, int(timeLen / groups))
            # plt.show()
            if i == 0:
                arrival = group_arr
            else:
                arrival = np.append(arrival, group_arr)
            # print(np.random.normal(timeLen / groups * (i + 1) / 2, timeLen / groups / 4, int(students / groups)))

        # print(arrival)
        plt.title(name + note, fontproperties='SimHei', fontsize=20)
        plt.xlabel('时间（分）（统计时长：' + str(stat_time) + '分）', fontproperties='SimHei', fontsize=15)
        plt.ylabel('学生（人）', fontproperties='SimHei', fontsize=15)
        plt.hist(arrival, int(bins))
        plt.savefig(name + '（时长' + str(time_len) + '分）')
        # plt.show()
        plt.close()


# 原方案（时长30分）
stu = 1400
timeLen = 30
plans = {'原方案': 1}
bins = 4
drawPlan(plans, stu, timeLen, bins, note='（上学时间段：7:00 - 7:30）')

# 新方案（时长60分）
timeLen = 60
bins = timeLen / 10 * 1.75
plans = {'新方案—1组': 1, '新方案—2组': 2, '新方案—3组': 3, '新方案—4组': 4, '新方案—5组': 5}
drawPlan(plans, stu, timeLen, bins, note='（上学时间段：7:00 - 8:00）')

# 新方案（时长90分）
timeLen = 90
drawPlan(plans, stu, timeLen, bins, note='（上学时间段：7:00 - 8:30）')
