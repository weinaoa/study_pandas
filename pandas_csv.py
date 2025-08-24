import pandas as pd

df = pd.read_csv("nba.csv")

# print(df.to_string()) # 加载全部数据
print(df.head())  # 读取前五行
print(df.tail())  # 读取最后五行
print(df.info())  # info() 方法返回表格的一些基本信息


# # 三个字段 name, site, age
# nme = ["Google", "Runoob", "Taobao", "Wiki"]
# st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
# ag = [90, 40, 80, 98]

# # 字典
# dict = {"name": nme, "site": st, "age": ag}

# df = pd.DataFrame(dict)
# print(df)
# # 保存 dataframe
# df.to_csv("site.csv", index=False)
