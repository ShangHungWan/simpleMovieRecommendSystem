# 基於 Collaborative Filtering 之 Web 電影推薦系統

###### tags: `Discrete mathematics` `Collaborative Filtering` `python` `Recommender system` `pandas` 

## Collaborative Filtering 簡介
Collaborative Filtering 是利用有相同興趣的群體為樣本，去推薦使用者可能感興趣的資訊。
又分為 user-based、item-based 兩種，前者是以使用者資訊為基礎，先收集使用者A感興趣的資訊，再透過比較A與其他使用者的相似度，找到一些和他有相同興趣的使用者，把他們中出現頻率高但不在A興趣中的項目作為結果；後者是計算目前項目A跟其他項目的相似度，把與A相似度高的項目推薦給使用者。

## 專案描述
此專案為一個簡單的電影推薦系統，使用者只需選擇一部感興趣的電影，系統即會自動推薦相關的電影給使用者。

## 技術介紹
使用上述的 Item-based 為基礎算法，當使用者選擇一部電影時，根據所有用戶的評分判斷所有電影與這部電影的相似度，並將相似度高且評分高於平均值的電影推薦給使用者。

1. 使用flask套件架設伺服器
2. 使用pandas進行資料儲存、過濾、分析、相似度計算等操作

## 如何安裝

需先安裝 python3 及 pip3 套件。
另外此專案中使用到 pandas 及 flask package。

``` shell
$ python3 --version # Python 3.6.9
$ pip3 install pandas
$ pip3 install flask
$ python3 app.py # 伺服器即會開始執行
```
此時連上 http://127.0.0.1:5000/ 即可見到網站首頁。

## 操作說明
可以先嘗試使用此網址 http://a24230928.pythonanywhere.com/

若無法使用請見"如何安裝"

在網站首頁選擇電影名稱、欲顯示的推薦筆數，接著按下"Go"按鈕，即可看到推薦結果表格。

## 資料來源
此次專案資料來源為：MovieLens，一個電影推薦系統網站，其中收錄了大量的電影及用戶喜好資料等。

## Ref
 - [Pandas官網](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corrwith.html)
 - [Collaborative Filtering wiki](https://zh.wikipedia.org/wiki/%E5%8D%94%E5%90%8C%E9%81%8E%E6%BF%BE)
 - [MovieLens官網](https://movielens.org/)