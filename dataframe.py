# import pandas as pd

# # 字典 → 列优先，列表 → 行优先。
# data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

# # 创建DataFrame
# df = pd.DataFrame(data, columns=['Site', 'Age'])

# # 使用astype方法设置每列的数据类型
# df['Site'] = df['Site'].astype(str)
# df['Age'] = df['Age'].astype(float)

# print(df)

# # 创建 DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, None, 40],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }
# df = pd.DataFrame(data)
# print(df)
# # 查看前两行数据
# print(df.head(2))

# # 查看 DataFrame 的基本信息
# print(df.info())
# print("=====================")
# # 获取描述统计信息
# print(df.describe())
# print("=====================")
# # 按年龄排序
# df_sorted = df.sort_values(by='Age', ascending=False)
# print(df_sorted)

# # 选择指定列
# print(df[['Name', 'Age']])
# print()
# # 按索引选择行
# print(df.iloc[1:3])  # 选择第二到第三行（按位置）
# print()
# # 按标签选择行
# print(df.loc[1:2])  # 选择第二到第三行（按标签）
# print()
# # 计算分组统计（按城市分组，计算平均年龄）
# print(df.groupby('City')['Age'].mean())
# print()
# # 处理缺失值（填充缺失值）
# df['Age'] = df['Age'].fillna(30)

# print("=====================")
# print(df)
# print(df['Age'])
# print()
# print(df.iloc[2])
# print()
# print(df.loc[2])
# print()
# print(df.Name)
# print()
# print(df["Name"][1])
# # 通过行标签访问
# print(df.loc[0, 'Name'])
# # 导出为 CSV 文件
# # df.to_csv('output.csv', index=False)

import pandas as pd

# # 使用concat添加新行
# data = {"A": [1, 2, 3], "B": [4, 5, 6]}
# df = pd.DataFrame(data)
# print(df)
# new_row = pd.DataFrame([[4, 7]], columns=["A", "B"])  # 创建一个只包含新行的DataFrame
# print(new_row)
# df = pd.concat([df, new_row], ignore_index=True)  # 将新行添加到原始DataFrame
# print("====================")
# # 删除
# df_dropped1 = df.drop("B", axis=1)
# df_dropped2 = df.drop(0)  # 删除索引为 0 的行
# print(df)
# print(df_dropped1)
# print(df_dropped2)
# print("====================")
# print(df)
# df_set = df.set_index("A")  # 设置 'A' 列为索引
# print(df_set)
# df_set.reset_index(inplace=True)  # 重置索引
# print(df_set)
# print("====================")
# # 过滤
# df_filtered = df[df["A"] > 2]
# print(df)
# print(df_filtered)
# print("====================")
# print(df.dtypes)
# df["A"] = df["A"].astype("float64")
# print(df)
# print("====================")
# # 合并与分割
# df1 = pd.DataFrame({"姓名": ["张三", "李四", "王五"], "语文": [85, 90, 78]})
# df2 = pd.DataFrame({"姓名": ["张三", "李四", "赵六"], "数学": [92, 85, 95]})
# print()
# # 纵向合并
# df_vertical_merger = pd.concat([df1, df2], ignore_index=True)
# print(df_vertical_merger)
# print()
# # 横向合并
# df_horizontal_merger = pd.concat([df1, df2], axis=1)
# print(df_horizontal_merger)
# print(df1)
# print(df2)
# df_merge = pd.merge(df1, df2, on="姓名", how="inner")
# print(df_merge)
# print("====================")
# 分割
import pandas as pd

df = pd.DataFrame(
    {
        "日期": ["2025-08-01", "2025-08-01", "2025-08-02", "2025-08-02"],
        "城市": ["北京", "上海", "北京", "上海"],
        "温度": [30, 32, 31, 33],
    }
)

print(df)
print()

# pivot：长 → 宽
df_wide = df.pivot(index="日期", columns="城市", values="温度")
print(df_wide)
# df.pivot(index='行索引列', columns='列名列', values='值列')
# index → 你想让哪一列作为 行的标签
# 生活化记忆：每一行的名字，比如学生名字、日期。

# columns → 你想把哪一列的值展开成 列名
# 生活化记忆：原来是一列，现在变成多列，比如科目、城市。

# values → 表格里填充的 具体数值
# 生活化记忆：成绩、温度等具体数据。

print()
# melt：宽 → 长
df_wide = pd.DataFrame(
    {"日期": ["2025-08-01", "2025-08-02"], "北京": [30, 31], "上海": [32, 33]}
)
print(df_wide)

df_long = df_wide.melt(
    id_vars="日期", value_vars=["北京", "上海"], var_name="城市", value_name="温度"
)
print(df_long)
# df.melt(id_vars='保留列', value_vars=['要转长的列'],
#         var_name='新列名', value_name='新值名')

# id_vars → 保留的列，不会被压平
# 例：学生、日期

# value_vars → 要压成一列的列
# 例：科目、城市

# var_name → 压下来的列的名字
# 例：原来的列名变成“科目”列

# value_name → 压下来的列的值的名字
# 例：原来的数值列变成“分数”列
