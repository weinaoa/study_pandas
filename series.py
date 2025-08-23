import pandas as pd

# 创建一个Series对象，指定名称为'A'，值分别为1, 2, 3, 4
# 默认索引为0, 1, 2, 3
series = pd.Series([1, 2, 3, 4], name="A")

# 显示Series对象
print(series)
print("=======================")

# 如果你想要显式地设置索引，可以这样做：
custom_index = [1, 2, 3, 4]  # 自定义索引
series_with_index = pd.Series([1, 2, 3, 4], index=custom_index, name="A")

# 显示带有自定义索引的Series对象
print(series_with_index)
print("=======================")

# 使用 key/value 对象，类似字典来创建 Series
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites, index=[1, 2], name="RUNOOB-Series-TEST")
print(myvar)

print("=======================")
# 创建 Series
data = [2, 6, 3, 5, 4, 1]
index = ["a", "b", "c", "d", "e", "f"]
s = pd.Series(data, index=index)

# 查看基本信息
print("索引：\n", s.index)
print("数据：\n", s.values)
print("数据类型：\n", s.dtype)
print("前两行数据：\n", s.head(2))

# 使用 map 函数将每个元素加倍
s_doubled = s.map(lambda x: x * 2)
print("元素加倍后：\n", s_doubled)

# 计算累计和
cumsum_s = s.cumsum()
print("累计求和：\n", cumsum_s)

# 查找缺失值（这里没有缺失值，所以返回的全是 False）
print("缺失值判断：\n", s.isnull())

# 排序
sorted_s = s.sort_values()
print("排序后的 Series：\n", sorted_s)

print(s["b":"d"])
print(s[:3])
# 使用 drop 方法删除一个或多个索引标签，并返回一个新的 Series。
s_dropped = s.drop(["b", "f"])  # 返回一个删除了索引标签 'b' 的新 Series
print("删除索引 'b' 后的 Series：\n", s_dropped)
print("=======================")
# 算术运算
result1 = s * 2  # 所有元素乘以2
print("所有元素乘以2：\n", result1)
# 过滤
filtered_series = s[s > 2]  # 选择大于2的元素
print("大于2的元素：\n", filtered_series)
# 数学函数
import numpy as np

result2 = np.sqrt(s)  # 对每个元素取平方根
print("每个元素的平方根：\n", result2)
print("=======================")
print(s.sum())  # 输出 Series 的总和
print(s.mean())  # 输出 Series 的平均值
print(s.max())  # 输出 Series 的最大值
print(s.min())  # 输出 Series 的最小值
print(s.std())  # 输出 Series 的标准差
print(s.var())  # 输出 Series 的方差
print("=====================")
# 获取索引
index = s.index

# 获取值数组
values = s.values

# 获取描述统计信息
stats = s.describe()

# 获取最大值和最小值的索引
max_index = s.idxmax()
min_index = s.idxmin()

# 其他属性和方法
print(s.dtype)  # 数据类型
print(s.shape)  # 形状
print(s.size)  # 元素个数
print(s.head())  # 前几个元素，默认是前 5 个
print(s.tail())  # 后几个元素，默认是后 5 个
print(s.sample(2))  # 随机抽样 2 个元素
print(s[s > 2])  # 选择大于2的元素
print(s > 2)  # 返回一个布尔 Series，其中的元素值大于 2
s = s.astype("float64")  # 将 Series 中的所有元素转换为 float64 类型
print(s)

""" 
# 使用列表创建 Series
s = pd.Series([1, 2, 3, 4])

# 使用 NumPy 数组创建 Series
s = pd.Series(np.array([1, 2, 3, 4]))

# 使用字典创建 Series
s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4}) 
"""
