import pandas as pd

# 读取原始表格
df = pd.read_excel('input.xlsx')

# 创建新的数据框
new_df = pd.DataFrame(columns=['Value'])

# 遍历原始表格中的每一行
for _, row in df.iterrows():
    start_new_row = True  # 标志变量，用于判断是否在新行中开始添加开头

    for value in row.values:
        if start_new_row:  # 在新行中添加开头
            new_df = new_df._append({'Value': 'A: '}, ignore_index=True)
            new_df = new_df._append({'Value': 'B: '}, ignore_index=True)
            new_df = new_df._append({'Value': 'C: '}, ignore_index=True)
            new_df = new_df._append({'Value': 'D: '}, ignore_index=True)
            new_df = new_df._append({'Value': '答案: '}, ignore_index=True)
            start_new_row = False  # 设置标志变量为 False，避免重复添加开头

        if pd.notnull(value):  # 检查是否为非空值
            new_df = new_df._append({'Value': value}, ignore_index=True)
        else:
            start_new_row = True  # 在空单元格处设置标志变量为 True，以便在下一行中开始添加开头

# 将数据保存到新的表格
new_df.to_excel('output2.xlsx', index=False)