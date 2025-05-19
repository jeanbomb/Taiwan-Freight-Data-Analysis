# 📦 Taiwan Freight Data Analysis / 台灣貨運數據分析

<a id="top"></a>

📌 [English Version](#english-version) | [日本語](#japanese-version) | [中文版](#中文版)


---

## **English Version** <a id="english-version"></a>

### 📌 Project Overview
I used **[Taiwan Government Open Data](https://data.gov.tw/dataset/6307)** to analyze Taiwan's **2023 freight data**, applying **Python for data preprocessing** and using **Power BI for visualization**.

### 📄 Files Included
- `data_dictionary.csv` → Logistics variable mapping  
- `cleaned_logistics_data.csv` → Preprocessed dataset  
- `logistics_data_renamed.csv` → Renamed columns dataset  
- `logistics_data_transformed.csv` → Transformed dataset with mapped values  

[🔺 Back to Top](#top)  

---

## 💡 **Step 1️⃣: Data Processing with Python**
I used **Python & Pandas** to clean and preprocess the logistics dataset.

### **1️⃣ Load Raw Data**
I loaded two datasets:
- **Variable Dictionary (`data_dictionary.csv`)** → Helps translate variable codes to readable names.
- **Freight Data (`logistics_data.csv`)** → Contains transport records for 2023.

```python
import pandas as pd

# Load datasets
df_dict = pd.read_csv("data_dictionary.csv", encoding="cp950")
df_data = pd.read_csv("logistics_data.csv", encoding="latin1")

# Preview data structure
print(df_dict.head())
print(df_data.head())
```

### **2️⃣ Handle Missing Values**
✅ **Drop columns with excessive missing data (over 90%)**  
✅ **Fill missing values using mean/mode for numerical and categorical features**  

```python
# Remove columns with too many missing values
df_data_cleaned = df_data.dropna(axis=1, how="all")

# Fill missing numeric values with mean
df_data_cleaned["distqty"] = df_data_cleaned["distqty"].fillna(df_data_cleaned["distqty"].mean())

# Fill missing categorical values with most frequent value
df_data_cleaned["dtcityt"] = df_data_cleaned["dtcityt"].fillna(df_data_cleaned["dtcityt"].mode()[0])
```

### **3️⃣ Rename Variables Using Data Dictionary**
Since the original dataset uses **coded variable names**, I replaced them using `data_dictionary.csv` mapping.

```python
# Create mapping from variable dictionary
variable_mapping = dict(zip(df_dict["變數名稱"], df_dict["變數內容"]))

# Rename columns using mapping
df_data_renamed = df_data_cleaned.rename(columns=variable_mapping)
```

### **4️⃣ Convert Numeric Codes to Meaningful Labels**
Some values in the dataset represent categories **using numeric codes** (e.g., city codes, product IDs). I mapped them to human-readable labels.

```python
# Map product codes to names
product_mapping = dict(zip(df_dict["商品編號數值"], df_dict["內容"]))
df_data_renamed["商品編號"] = df_data_renamed["商品編號"].map(product_mapping)

# Map city codes to actual locations
city_mapping = dict(zip(df_dict["裝卸貨地點數值"], df_dict["內容"]))
df_data_renamed["裝貨地點"] = df_data_renamed["裝貨地點"].map(city_mapping)
df_data_renamed["卸貨地點"] = df_data_renamed["卸貨地點"].map(city_mapping)
```

### **Final Step: Save Cleaned Data**
After preprocessing, I exported the cleaned dataset for Power BI visualization.

```python
df_data_renamed.to_csv("logistics_data_transformed.csv", index=False)
print("Data successfully saved to 'logistics_data_transformed.csv'")
```

[🔺 Back to Top](#top)  

---

## 📊 **Step 2️⃣: Freight Data Visualization with Power BI**
After cleaning the dataset, I used **Power BI** to visualize key trends:

✅ **Regional Freight Distribution** → A map displaying transportation flows  
✅ **Freight Hotspots** → Identifies high-volume transportation areas  
✅ **Transport Volume by Product Type** → Breakdown by different commodities  
✅ **Trends in Transport Distance and Freight Costs** → Analyzes cost variations  

🔹 **Screenshot of Power BI Visualization**:  
![Power BI Dashboard]
![image](https://github.com/user-attachments/assets/f0ccffbe-4172-4eb9-96c3-17eed4ce1874)
![image](https://github.com/user-attachments/assets/a846271b-08a3-4146-98d1-ae144e2ae54c)

[🔺 Back to Top](#top)  

---

## 📜 License & Contribution
I utilized **[Taiwan Government Open Data](https://data.gov.tw/dataset/6307)** for this project.  
Feel free to submit **issues** or **pull requests** for improvements!

[🔺 Back to Top](#top)  

---

# 🇯🇵 日本語版 <a id="japanese-version"></a>

### 📌 プロジェクト概要
**[台湾政府オープンデータ](https://data.gov.tw/dataset/6307)** を用いて、台湾の **2023年貨物データ** を分析しました。**Pythonでデータの前処理** を行い、**Power BIで可視化** しています。

### 📄 含まれるファイル
- `data_dictionary.csv` → 物流変数マッピング  
- `cleaned_logistics_data.csv` → 前処理済みデータセット  
- `logistics_data_renamed.csv` → 列名をリネームしたデータセット  
- `logistics_data_transformed.csv` → 値をマッピングした変換済みデータセット  

[🔺 一番上に戻る](#top)  

---

## 💡 **ステップ1️⃣: Pythonによるデータ前処理**
**Python & Pandas** を使用して物流データセットをクリーニングおよび前処理しました。

### **1️⃣ 生データの読み込み**
2つのデータセットを読み込みます:
- **変数辞書 (`data_dictionary.csv`)** → 変数コードを読みやすい名前に翻訳するために使用
- **貨物データ (`logistics_data.csv`)** → 2023年の輸送記録を含む

```python
import pandas as pd

# データセットの読み込み
df_dict = pd.read_csv("data_dictionary.csv", encoding="cp950")
df_data = pd.read_csv("logistics_data.csv", encoding="latin1")

# データ構造をプレビュー
print(df_dict.head())
print(df_data.head())
```

### **2️⃣ 欠損値の処理**
✅ **欠損値が90%以上の列を削除**  
✅ **数値型は平均値、カテゴリ型は最頻値で欠損値を補完**  

```python
# 欠損値が多い列を削除
df_data_cleaned = df_data.dropna(axis=1, how="all")

# 数値型の欠損値を平均値で補完
df_data_cleaned["distqty"] = df_data_cleaned["distqty"].fillna(df_data_cleaned["distqty"].mean())

# カテゴリ型の欠損値を最頻値で補完
df_data_cleaned["dtcityt"] = df_data_cleaned["dtcityt"].fillna(df_data_cleaned["dtcityt"].mode()[0])
```

### **3️⃣ 変数名をデータ辞書でリネーム**
元のデータセットはコード化された変数名を使用しているため、`data_dictionary.csv` のマッピングを使ってリネームしました。

```python
# 辞書からマッピングを作成
variable_mapping = dict(zip(df_dict["變數名稱"], df_dict["變數內容"]))

# 列名をリネーム
df_data_renamed = df_data_cleaned.rename(columns=variable_mapping)
```

### **4️⃣ 数値コードを意味のあるラベルに変換**
一部の値は数値コードでカテゴリを表しているため（例：都市コード、商品ID）、人間が読めるラベルにマッピングしました。

```python
# 商品コードを名称にマッピング
product_mapping = dict(zip(df_dict["商品編號數值"], df_dict["內容"]))
df_data_renamed["商品編號"] = df_data_renamed["商品編號"].map(product_mapping)

# 都市コードを実際の地名にマッピング
city_mapping = dict(zip(df_dict["裝卸貨地點數值"], df_dict["內容"]))
df_data_renamed["裝貨地點"] = df_data_renamed["裝貨地點"].map(city_mapping)
df_data_renamed["卸貨地點"] = df_data_renamed["卸貨地點"].map(city_mapping)
```

### **最終ステップ: 前処理データの保存**
前処理後、Power BIでの可視化のためにデータセットを書き出しました。

```python
df_data_renamed.to_csv("logistics_data_transformed.csv", index=False)
print("データを 'logistics_data_transformed.csv' に保存しました")
```

[🔺 一番上に戻る](#top)  

---

## 📊 **ステップ2️⃣: Power BIによる可視化**
データクリーニング後、**Power BI** を使って主な傾向を可視化しました:

✅ **地域別の貨物分布** → 運送フローの地図表示  
✅ **貨物ホットスポット** → 輸送量の多いエリアの特定  
✅ **商品タイプ別の輸送量** → 各商品の輸送内訳  
✅ **輸送距離と運賃の傾向** → コスト変動の分析  

🔹 **Power BI ダッシュボードのスクリーンショット**:  
![Power BI Dashboard]
![image](https://github.com/user-attachments/assets/f0ccffbe-4172-4eb9-96c3-17eed4ce1874)
![image](https://github.com/user-attachments/assets/a846271b-08a3-4146-98d1-ae144e2ae54c)

[🔺 一番上に戻る](#top)  

---

## 📜 ライセンス & コントリビューション
本プロジェクトは **[台湾政府オープンデータ](https://data.gov.tw/dataset/6307)** を利用しています。  
改善のための **Issue** や **Pull Request** を歓迎します！

[🔺 一番上に戻る](#top)  

---

# 📦 台灣貨運數據分析 <a id="中文版"></a>

### 📌 專案概述
使用 **[政府公開數據](https://data.gov.tw/dataset/6307)**，分析 **112 年台灣貨運數據**，運用 **Python 進行數據前處理**，並透過 **Power BI 呈現視覺化結果**。

### 📄 包含的文件
- `data_dictionary.csv` → 物流變數對應表  
- `cleaned_logistics_data.csv` → 數據清理結果  
- `logistics_data_renamed.csv` → 重新命名欄位的數據集  
- `logistics_data_transformed.csv` → 數據映射後的結果  

[🔺 返回最上面](#top)  

---

## 💡 **步驟 1️⃣：使用 Python 進行數據前處理**
使用 **Python & Pandas** 來清理和前處理台灣物流數據，確保數據適合分析和視覺化。

### **1️⃣ 載入原始數據**
載入兩個數據文件：
- **變數字典 (`data_dictionary.csv`)** → 用來翻譯變數代碼，使數據更易理解。
- **貨運數據 (`logistics_data.csv`)** → 包含 112 年（2023 年）的運輸記錄。

```python
import pandas as pd

# 載入數據集
df_dict = pd.read_csv("data_dictionary.csv", encoding="cp950")
df_data = pd.read_csv("logistics_data.csv", encoding="latin1")

# 預覽數據結構
print(df_dict.head())
print(df_data.head())
```

### **2️⃣ 處理缺失值**
✅ **刪除高缺失率欄位（超過 90% 缺失的欄位）**  
✅ **填補數值類型的缺失值（使用平均值）**  
✅ **填補類別類型的缺失值（使用最常見值）**

```python
# 移除過多缺失值的欄位
df_data_cleaned = df_data.dropna(axis=1, how="all")

# 填補數值類型缺失值（用平均值）
df_data_cleaned["distqty"] = df_data_cleaned["distqty"].fillna(df_data_cleaned["distqty"].mean())

# 填補類別類型缺失值（用眾數）
df_data_cleaned["dtcityt"] = df_data_cleaned["dtcityt"].fillna(df_data_cleaned["dtcityt"].mode()[0])
```

### **3️⃣ 根據數據字典替換變數名稱**
數據原始欄位名稱是 **代碼**，我使用 `data_dictionary.csv` 來替換為可讀的變數名稱。

```python
# 建立變數對應字典
variable_mapping = dict(zip(df_dict["變數名稱"], df_dict["變數內容"]))

# 重新命名欄位
df_data_renamed = df_data_cleaned.rename(columns=variable_mapping)
```

### **4️⃣ 轉換數值代碼為可讀標籤**
✅ **商品編號 → 映射為具體貨物類別（如「水果」、「電子產品」等）**  
✅ **地區代碼 → 映射為真實城市名稱（如 `dtcityf=201` → 宜蘭市）**

```python
# 映射商品編號為可讀名稱
product_mapping = dict(zip(df_dict["商品編號數值"], df_dict["內容"]))
df_data_renamed["商品編號"] = df_data_renamed["商品編號"].map(product_mapping)

# 映射地區代碼為真實地點
city_mapping = dict(zip(df_dict["裝卸貨地點數值"], df_dict["內容"]))
df_data_renamed["裝貨地點"] = df_data_renamed["裝貨地點"].map(city_mapping)
df_data_renamed["卸貨地點"] = df_data_renamed["卸貨地點"].map(city_mapping)
```

### **最終步驟：儲存清理後的數據**
數據清理完成後，我匯出清理結果，供 **Power BI 分析與視覺化**。

```python
df_data_renamed.to_csv("logistics_data_transformed.csv", index=False)
print("數據成功儲存為 'logistics_data_transformed.csv'")
```

[🔺 返回最上面](#top)  

---

### **步驟 2️⃣：使用 Power BI 進行數據可視化**
使用 **Power BI** 來視覺化數據趨勢：
✅ **地區貨運分布** → 台灣不同地區的運輸流向  
✅ **貨運熱點分析** → 高流量的運輸區域  
✅ **商品類型的運輸量** → 各類貨物的運輸佔比  
✅ **運輸距離與運費的變化趨勢** → 分析運費與距離變化  
![image](https://github.com/user-attachments/assets/42b7c9d1-fdfa-43b2-ba5c-6d2ba57064de)
![image](https://github.com/user-attachments/assets/bc28957c-fa1d-4ba4-8bbb-3d92db1c3299)


[🔺 返回最上面](#top)  

---

## 📜 版權 & 貢獻
本專案使用 **[政府公開數據](https://data.gov.tw/dataset/6307)**，歡迎提交 **Issue** 或 **Pull Request** 提供改進建議！

[🔺 返回最上面](#top)  

---
