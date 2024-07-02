# 專案簡介  

![專案圖片](https://i.imgur.com/TWSDocn.png)
[台灣銀行代碼查詢](https://interview-5xcamp-7c73676fe792.herokuapp.com/)是一個使用 Django 框架開發的網站，旨在提供用戶快速查詢台灣各銀行分行的代碼資訊。  
通過這個網站，用戶可以輕鬆地搜索並獲取所需的銀行代碼資訊，網站內也提供「複製代碼」、「複製頁面連結」等功能，節省紀錄時間並提高查詢效率。

## 目錄

- [專案簡介](#專案簡介)
  - [目錄](#目錄)
  - [功能](#功能)
  - [使用](#使用)
    - [查詢銀行代碼](#查詢銀行代碼)
    - [使用示例](#使用示例)
  - [安裝](#安裝)
    - [系統要求](#系統要求)
    - [安裝步驟](#安裝步驟)
  - [技術棧](#技術棧)
  - [其他](#其他)

## 功能

- 銀行代碼快速查詢
- 支持按銀行名稱或分行名稱搜索
- 顯示銀行分行的詳細信息

## 使用

在啟動開發伺服器後，打開瀏覽器並訪問 `http://127.0.0.1:8000` 查看並使用台灣銀行代碼查詢網站。

### 查詢銀行代碼

1. 進入首頁後，使用者會看到一個搜索欄。
2. 在搜索欄中輸入您想要查詢的銀行名稱或分行名稱。
3. 系統會根據輸入內容顯示符合條件的銀行及分行列表。
4. 您可以點擊列表中的銀行名稱查看該分行的詳細信息，包括分行代碼、地址和聯絡方式。
5. 使用者可以透過`複製代碼`的按鈕，輕鬆複製該分行代碼，也可以透過`複製此頁面連結`複製該分行網頁網址，並且使用該網址再次獲得分行資訊。
6. 點擊`重新查詢`後，將回到首頁進行新的搜尋。

### 使用示例

1. 在搜索欄中輸入「台灣銀行」並點擊「搜尋」。
2. 系統將顯示所有包含「台灣銀行」的分行及其代碼。
3. 點擊某個分行名稱即可查看詳細信息。

## 安裝

### 系統要求

- Python 3.12
- Django 5.0.6 或更高版本
- 其他依賴套件可參考 pyproject.toml 內容

### 安裝步驟

1. 克隆此 Repository 
```bash
$ git clone git@github.com:chienchuanw/5xcamp-interview.git
$ cd 5xcamp-interview
```

2. 建立虛擬環境並啟動  
如果還沒有安裝 Poetry，請先安裝：
```bash
$ pip install poetry
```
使用 Poetry 進入虛擬環境  
```bash
$ poetry shell
```

3. 使用 Poetry 安裝依賴套件  
```bash
$ poetry install
```

4. 設定環境變數  
於路徑 `/core` 內複製 `.env.example` 並重新命名為 `.env`，根據檔案內指引提示設定對應的環境變數。
```shell
# .env 文件範例
SECRET_KEY=Django-專案金鑰
BASE_URL=入口-URL（包含 http 或 https）
LOCALHOST=127.0.0.1
DOMAIN=入口-URL（不包含 http 或 https）
ADMIN_URL=後台管理入口-URL
```

5. 遷移資料庫  
```bash
$ python manage.py migrate
```

6. 匯入銀行相關數據至資料庫
```bash
$ python manage.py loaddata seed/0001_bank.json
```

7. 建立靜態樣式與腳本  
```bash
$ npm run build
```

8. 啟動開發伺服器  
```bash
$ python manage.py runserver
```

## 技術棧
本專案使用了以下技術和工具：
- 前端：HTML5、CSS3、Tailwind CSS、JavaScript、Alpine.js、Rollup
- 後端：Python、Django
- 資料庫：SQLite
- 部署：Heroku
- 版本控制：Git

## 其他

本網站開發參考五倍學院的[台灣銀行代碼查詢](https://bank.5xcamp.us/)網站，僅作為學習之用。  
如有其他建議，可以透過 Discord 搜尋 `chienchuan_w` 加好友並留言私訊，歡迎大家相互交流。
