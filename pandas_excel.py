import pandas as pd

# # 读取 data.xlsx 文件
df = pd.read_excel("runoob_pandas_data.xlsx", usecols="A:B")

# # 打印读取的 DataFrame
print(df)

# # 创建一个简单的 DataFrame
# df = pd.DataFrame({
# 'Name': ['Alice', 'Bob', 'Charlie'],
# 'Age': [25, 30, 35],
# 'City': ['New York', 'Los Angeles', 'Chicago']
# })

# # 将 DataFrame 写入 Excel 文件，写入 'Sheet1' 表单
# df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

# # 写入多个表单，使用 ExcelWriter
# with pd.ExcelWriter('output.xlsx') as writer:
#     df.to_excel(writer, sheet_name='Sheet1', index=False)
#     df.to_excel(writer, sheet_name='Sheet2', index=False)

# 单表写入 → 用 df.to_excel()

# 多表写入 / 追加写入 → 用 ExcelWriter
# 一般配合 with 语句使用，自动保存并关闭。