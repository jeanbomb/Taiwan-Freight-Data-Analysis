import pandas as pd

# 載入數據
df1 = pd.read_csv("112年汽車貨運調查-變數名稱.csv", encoding="cp950")
df2 = pd.read_csv("112年汽車貨運調查資料.csv", encoding="latin1")

# 檢視數據基本資訊
print(df1.head())  # 查看前五筆數據
print(df1.info())  # 查看欄位資訊
print(df2.head())  # 查看前五筆數據
print(df2.info())  # 查看欄位資訊
print("=====================檢查缺失值==============================")
print(df1.isnull().sum())  # 檢查缺失值
print("===================================================")
df1_cleaned = df1[["變數名稱", "變數內容"]]
print(df1_cleaned.head())
print("===================================================")
df1_cleaned.to_csv("data_dictionary.csv", index=False)
print("已儲存數據字典為 data_dictionary.csv")
print("=====================顯示df2每個欄位的缺失值數量==============================")
print(df2.isnull().sum())  # 顯示每個欄位的缺失值數量
'''
刪除缺失值較多的欄位（如果某個欄位有 90% 以上缺失，可能可以直接移除）
df2 = df2.drop(columns=["可能不必要的欄位"])

或者，如果某些欄位完全無數據：
df2 = df2.dropna(axis=1, how="all")  # 移除整個空欄位


刪除包含缺失值的行
- 如果只有少部分數據有遺漏，可以直接刪除：df2_cleaned = df2.dropna()


填補缺失值
- 用 平均值 填補數字類型：df2["teu"] = df2["teu"].fillna(df2["teu"].mean())

- 用 最常出現值（mode） 填補類別型數據：df2["dtcityt"] = df2["dtcityt"].fillna(df2["dtcityt"].mode()[0])


填補特定數據
- 如果是 貨運量 (distqty) 缺失，可以填補 0：df2["distqty"] = df2["distqty"].fillna(0)
'''
print("=====================顯示前 10 個貨運量最大的城市==============================")
city_transport = df2.groupby("dtcityt")["distqty"].sum().sort_values(ascending=False)
print(city_transport.head(10))  # 顯示前 10 個貨運量最大的城市
print("====================顯示每個月份的貨運量總和===============================")
monthly_trend = df2.groupby("mm")["distqty"].sum()
print(monthly_trend)    # 顯示每個月份的貨運量總和
print("===================================================")
df2.to_csv("cleaned_logistics_data.csv", index=False)
print("已儲存清理後的數據為 cleaned_logistics_data.csv")
print("====================自動切割 CSV 中多個表格===============================")
# 讀取主要數據文件
cleaned_data = pd.read_csv("cleaned_logistics_data.csv")

# 讀取數據字典
raw_dict = pd.read_csv("data_dictionary.csv", header=None)

# 找出全為 NaN 的空白列 index，用來分隔表格
split_indices = raw_dict[raw_dict.isnull().all(axis=1)].index.tolist()
split_indices.append(len(raw_dict))  # 加入最後一個區段的結尾

# 分割成多個子表格
tables = []
start = 0
for end in split_indices:
    sub_table = raw_dict.iloc[start:end].dropna(how="all")
    if not sub_table.empty:
        sub_table.columns = sub_table.iloc[0]  # 第一列作為欄位名稱
        sub_table = sub_table[1:]              # 移除欄位列
        tables.append(sub_table.reset_index(drop=True))
    start = end + 1

# 顯示每個表格的欄位與前幾列資料
for i, table in enumerate(tables):
    print(f"\n--- 表格 {i + 1} ---")
    print(table.head())
print("====================更改變數===============================")
# 取得第一個表格，這是變數對照表
variables_table = tables[0]

# 建立變數名稱映射字典 (從代碼到中文說明)
variable_mapping = dict(zip(variables_table['變數名稱'], variables_table['變數內容']))

# 應用映射，重新命名數據框的列
cleaned_data_renamed = cleaned_data.rename(columns=variable_mapping)

# 建立代碼映射字典 (針對分類變數)
code_mappings = {}

# 表格2：半年註記
half_year_map = dict(zip(tables[1]['半年註記數值'].astype(str), tables[1]['內容']))
code_mappings['半年註記'] = half_year_map

# 表格3：商品編號
product_map = dict(zip(tables[2]['商品編號數值'].astype(str), tables[2]['內容']))
code_mappings['商品編號'] = product_map

# 表格4：裝卸貨地點
location_map = dict(zip(tables[3]['裝卸貨地點數值'].astype(str), tables[3]['內容']))
code_mappings['裝貨地點'] = location_map
code_mappings['卸貨地點'] = location_map

# 表格5：商品來源別
origin_map = dict(zip(tables[4]['商品來源別數值'].astype(str), tables[4]['內容']))
code_mappings['商品來源別'] = origin_map

# 表格6：低溫商品運費收入比率
# 確保第一欄位是索引，第二欄位是值
if '低溫商品運費收入占總運費收入之比率' in tables[5].columns:
    col_name = '低溫商品運費收入占總運費收入之比率'
    value_col = tables[5].columns[1] if len(tables[5].columns) > 1 else 'NaN'
    income_ratio_map = dict(zip(tables[5][col_name].astype(str), tables[5][value_col]))
    # 檢查在原始數據中的確切欄位名稱
    if '低溫商品運費收入占總運費收入之比率' in cleaned_data_renamed.columns:
        code_mappings['低溫商品運費收入占總運費收入之比率'] = income_ratio_map
    else:
        # 可能需要檢查原始數據中是否有相似的欄位
        similar_cols = [col for col in cleaned_data_renamed.columns if '低溫' in col and '運費' in col]
        for col in similar_cols:
            code_mappings[col] = income_ratio_map

# 表格7：低溫商品運量比率
if '低溫商品運量占總運量之比率' in tables[6].columns:
    col_name = '低溫商品運量占總運量之比率'
    value_col = tables[6].columns[1] if len(tables[6].columns) > 1 else 'NaN'
    volume_ratio_map = dict(zip(tables[6][col_name].astype(str), tables[6][value_col]))
    # 檢查在原始數據中的確切欄位名稱
    if '低溫商品運量占總運量之比率' in cleaned_data_renamed.columns:
        code_mappings['低溫商品運量占總運量之比率'] = volume_ratio_map
    else:
        # 可能需要檢查原始數據中是否有相似的欄位
        similar_cols = [col for col in cleaned_data_renamed.columns if '低溫' in col and '運量' in col]
        for col in similar_cols:
            code_mappings[col] = volume_ratio_map

# 表格8：平均每公升可行駛里程數
if '平均每公升可行駛里程數' in tables[7].columns:
    col_name = '平均每公升可行駛里程數'
    value_col = tables[7].columns[1] if len(tables[7].columns) > 1 else 'NaN'
    mileage_map = dict(zip(tables[7][col_name].astype(str), tables[7][value_col]))
    # 檢查在原始數據中的確切欄位名稱
    if '平均每公升可行駛里程數' in cleaned_data_renamed.columns:
        code_mappings['平均每公升可行駛里程數'] = mileage_map
    else:
        # 可能需要檢查原始數據中是否有相似的欄位
        similar_cols = [col for col in cleaned_data_renamed.columns if '公升' in col or '里程' in col]
        for col in similar_cols:
            code_mappings[col] = mileage_map

# 直接用說明替換數值
transformed_data = cleaned_data_renamed.copy()

# 為每個分類變數替換值
for var_name, mapping in code_mappings.items():
    if var_name in transformed_data.columns:
        # 使用映射替換值，對於缺失的映射保留原始值
        transformed_data[var_name] = transformed_data[var_name].astype(str).apply(
            lambda x: mapping.get(x, x) if x != 'nan' else x
        )
        
# 顯示哪些欄位被轉換了
print("\n以下欄位的數值已被轉換為說明文字:")
for var_name in code_mappings.keys():
    if var_name in transformed_data.columns:
        print(f" - {var_name}")
    else:
        print(f" - {var_name} (未在數據中找到對應欄位)")

# 檢查數據框中是否存在這些特定欄位
special_columns = ['低溫商品運費收入占總運費收入之比率', '低溫商品運量占總運量之比率', '平均每公升可行駛里程數']
found_columns = [col for col in special_columns if col in cleaned_data_renamed.columns]

if found_columns:
    print("\n特殊欄位出現在數據中:")
    for col in found_columns:
        print(f" - {col}")
        # 顯示該欄位的唯一值和出現次數
        value_counts = cleaned_data_renamed[col].value_counts().head(10)
        print(f"   前10個最常見值: \n{value_counts}")
else:
    print("\n注意: 未在數據中找到表格6、7、8對應的欄位")
    
    # 查看所有欄位名稱以找到可能相關的欄位
    print("\n數據中所有欄位名稱:")
    for col in cleaned_data_renamed.columns:
        print(f" - {col}")

# 顯示結果
print("\n原始數據前5列:")
print(cleaned_data.head())

print("\n重命名後數據前5列:")
print(cleaned_data_renamed.head())

print("\n數值替換後數據前5列:")
print(transformed_data.head())

# 將結果保存到CSV文件
cleaned_data_renamed.to_csv("logistics_data_renamed.csv", index=False)
transformed_data.to_csv("logistics_data_transformed.csv", index=False)

print("\n數據已保存至 'logistics_data_renamed.csv' 和 'logistics_data_transformed.csv'")

