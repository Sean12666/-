import numpy as np
import matplotlib.pyplot as plt

def drawPlan(plans, stu, timeLen, statTime = 10, note = ''):
    for name, groups in plans.items():
        for i in range(groups):
            groupArrival = np.random.normal(timeLen / groups * (i + 1) - timeLen / groups / 3,
                                            timeLen / groups / 4, int(stu / groups))
            #plt.hist(groupArrival, int(timeLen / groups))
            #plt.show()
            if i == 0:
                arrival = groupArrival
            else:
                arrival = np.append(arrival, groupArrival)
            #print(np.random.normal(timeLen / groups * (i + 1) / 2, timeLen / groups / 4, int(students / groups)))

        #print(arrival)
        plt.title(name + note, fontproperties = 'SimHei', fontsize = 20)
        plt.xlabel('时间（分）（统计时长：' + str(statTime) + '分）', fontproperties = 'SimHei', fontsize = 15)
        plt.ylabel('学生（人）', fontproperties = 'SimHei', fontsize = 15)
        plt.hist(arrival, int(timeLen / statTime))
        plt.savefig(name + '（时长' + str(timeLen) + '分）')
        #plt.show()
        plt.close()

#原方案（时长30分）
stu = 1400
timeLen = 30
plans = {'原方案': 1}
drawPlan(plans, stu, timeLen, note = '（上学时间段：7:00 - 7:30）')

#新方案（时长60分）
timeLen = 60
plans = {'新方案—1组': 1, '新方案—2组': 2, '新方案—3组': 3, '新方案—4组': 4, '新方案—5组': 5}
drawPlan(plans, stu, timeLen, note = '（上学时间段：7:00 - 8:00）')

#新方案（时长90分）
timeLen = 90
drawPlan(plans, stu, timeLen, note = '（上学时间段：7:00 - 8:30）')
