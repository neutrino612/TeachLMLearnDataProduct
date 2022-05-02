from collections import OrderedDict   #有序字典
import pandas as pd

# 建立数据集
examDict = {'学习时间':[0.50,0.75,1.00,1.25,1.50,1.75,1.75,2.00,2.25,
            2.50,2.75,3.00,3.25,3.50,4.00,4.25,4.50,4.75,5.00,5.50],
            '分数':[10,  22,  13,  43,  20,  22,  33,  50,  62,
              48,  55,  75,  62,  73,  81,  76,  64,  82,  90,  93]}
examOrderDict = OrderedDict(examDict)
examDf = pd.DataFrame(examOrderDict)
print(examDf.head())

# 提取特征features
exam_X = examDf.loc[:,'学习时间']
# 提取标签labels
exam_y = examDf.loc[:,'分数']

# 绘制散点图
import matplotlib.pyplot as plt
plt.scatter(exam_X,exam_y,color='b',label='exam data')
plt.xlabel('Hours')
plt.ylabel('Score')
plt.show()

# 计算相关系数,corr  相关系数矩阵
rDf = examDf.corr()
print('相关系数矩阵：')
print(rDf)
