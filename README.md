# 📦 台灣貨運數據分析（Taiwan Freight Data Analysis）

## 📌 介紹（Introduction）
本專案使用 **[政府公開數據](https://data.gov.tw/dataset/6307)**，分析 **112 年台灣貨運數據**，運用 **Python 進行數據前處理**，並透過 **Power BI 呈現視覺化結果**。

This project utilizes **[Taiwan Government Open Data](https://data.gov.tw/dataset/6307)** to analyze **Taiwan's 2023 freight data**, applying **Python for data preprocessing** and using **Power BI for visualization**.

---



## 📊 主要分析內容（Key Analysis Metrics）
| 變數名稱  | 內容說明 | Variable Name | Description |
|----------|---------|--------------|------------|
| yy       | 調查年度 | Survey Year | Freight survey year |
| mm       | 半年註記 | Half-Year Flag | 1=上半年, 2=下半年 |
| goodid   | 商品編號 | Product ID | Freight type |
| dtcityf  | 裝貨地點 | Loading Location | Departure location |
| dtcityt  | 卸貨地點 | Unloading Location | Destination location |
| distqty  | 單程區間公里數 | Trip Distance (km) | Distance per trip |
| drcnt    | 行車次數 | Trip Count | Number of trips |
| frzmk    | 是否為低溫車 | Refrigerated Vehicle Flag | 1=Yes, 0=No |
| lowprod  | 低溫商品運費收入占比 | Refrigerated Product Revenue % | Ratio of freight cost from cold-chain goods |
| lowprod2 | 低溫商品運量占比 | Refrigerated Product Volume % | Ratio of freight volume from cold-chain goods |

---

## 💡 使用方式（Usage）
### 📌 載入 CSV（Load CSV）
```python
import pandas as pd

# 讀取數據字典
data_dict = pd.read_csv("data_dictionary.csv")

# 檢視前幾列
print(data_dict.head())
```

### 📌 數據映射（Data Mapping）
```python
# 建立映射字典
product_mapping = dict(zip(data_dict["商品編號數值"].dropna(), data_dict["內容"].dropna()))
location_mapping = dict(zip(data_dict["裝卸貨地點數值"].dropna(), data_dict["內容"].dropna()))

# 替換 CSV 數值為易讀名稱
cleaned_data["商品編號"] = cleaned_data["商品編號"].map(product_mapping)
cleaned_data["裝貨地點"] = cleaned_data["裝貨地點"].map(location_mapping)
cleaned_data["卸貨地點"] = cleaned_data["卸貨地點"].map(location_mapping)
```

---

## 📊 Power BI 視覺化（Power BI Visualization）
### 📍 冷凍商品數據分析（Cold-Chain Logistics Analysis）
✅ **地圖分析** → 透過「裝貨地點」與「卸貨地點」呈現貨物流向  
✅ **長條圖** → 顯示各類冷凍商品的運輸成本與貨量  
✅ **折線圖** → 分析運輸距離與低溫車使用率的變化  

---

## 📍 Applications / 應用場景
✅ **Data Preprocessing / 數據前處理** → Cleaning logistics data and transforming variables for better readability.  
✅ **Power BI Visualization / Power BI 視覺化** → Enhancing logistic data visualization by converting codes into meaningful labels.  
✅ **AI/Machine Learning Analysis / AI/機器學習分析** → Using standardized data for predictive transportation modeling. 

---

## 📜 版權 & 貢獻（License & Contribution）
本專案使用 **[政府公開數據](https://data.gov.tw/dataset/6307)**，歡迎提交 **Issue** 或 **Pull Request** 提供改進建議！  

This project utilizes **[Taiwan Government Open Data](https://data.gov.tw/dataset/6307)**. Feel free to submit **issues** or **pull requests** for improvements!
