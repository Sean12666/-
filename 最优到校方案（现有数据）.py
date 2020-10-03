import numpy as np
import matplotlib.pyplot as plt
import csv
import json


def loadcsv(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        arr = []
        for row in reader:
            arr.append(row)
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if j == 0:
                    arr[i][j] = int(arr[i][j])
                else:
                    arr[i][j] = float(arr[i][j])
        return arr


def loadjson(filename):
    with open(filename) as file:
        load = json.load(file)
        return load


def gendata(stu, arr_time, scale):
    arr = np.random.normal(arr_time, scale, stu)
    # print(arr)
    return arr


def makeplan(plans):
    plans_arr = gendata(plans[0][0], plans[0][1], plans[0][2])
    for i in range(1, len(plans)):
        arr = gendata(plans[i][0], plans[i][1], plans[i][2])
        plans_arr = np.concatenate((plans_arr, arr))
    return plans_arr


def drawplan(plan, bins, title, xlab, ylab):
    plt.title(title, fontproperties='SimHei', fontsize=20)
    plt.xlabel(xlab, fontproperties='SimHei', fontsize=15)
    plt.ylabel(ylab, fontproperties='SimHei', fontsize=15)
    plt.hist(plan, bins)
    plt.show()


if __name__ == '__main__':
    arrData = loadcsv('planning data.csv')
    stuArr = makeplan(arrData)
    figSetting = loadjson('figure setting.json')
    title = figSetting['title']
    xlabel = figSetting['xlabel']
    ylabel = figSetting['ylabel']
    drawplan(stuArr, 6, title, xlabel, ylabel)
