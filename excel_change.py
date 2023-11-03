import pandas as pd

# 读取原始表格
df = pd.read_excel('原始表格.xlsx')

# 创建新的数据框
new_df = pd.DataFrame(columns=['Value'])

# 遍历原始表格中的每一行
for _, row in df.iterrows():
    for value in row.values:
        if pd.notnull(value):  # 检查是否为非空值
            new_df = new_df.append({'Value': value}, ignore_index=True)
        else:
            # 获取下一列的首个非空单元格的值
            next_value = row[row.first_valid_index()]
            if pd.notnull(next_value):  # 检查是否为非空值
                new_df = new_df.append({'Value': next_value}, ignore_index=True)

# 将数据保存到新的表格
new_df.to_excel('新表格.xlsx', index=False)