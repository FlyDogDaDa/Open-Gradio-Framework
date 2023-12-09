# Kwenen-RVC-training

<div align="center">
    <svg height="100" width="100"> 
        <rect width="100" height="100" fill="#333333" rx="5" ry='5' /> 
        <image href="./WebUI/Kwenen-RVC-training_Icon.png" height="100px" width="100px"/>
        </svg> 
</div>

**Project introduction：**
A multi-integrated training tool that automatically adapts to your device, making training RVC models more convenient and simple.

---

# Basic interface program module to-do list

### 前端介面

- [ ] 跳出式詢問視窗
- [ ] 外部分頁格式規範格式
- [ ] 通過 Github 連結下載分頁功能
- [ ] 分頁依賴引用的連鎖下載
- [ ] 解除安裝分頁功能(需要詢問)
- [ ] 重新整理畫面按鈕(需要詢問)
- [ ] 儲存分頁狀態按鈕
- [ ] 已下載分頁重複檢測
- [ ] 已下載分頁更新檢測
- [ ] 單獨選擇分頁更新
- [ ] 全更新按鈕(需要詢問)
- [ ] 分頁版本控制功能
- [ ] 分頁環境儲存
- [ ] 分頁環境載入(需要詢問)
- [ ] 分頁環境刪除(需要詢問)
- [ ] 分頁環境控制器

### 代理人函式

**提醒：以「Facade Pattern」實現，功能為包裝各種"單一責任"函式，使其作整合一系列瑣碎動作。**

- [ ] 代理人函式載入(儲存)
- [ ] 代理人函式刪除
- [ ] 代理人函式依賴引用的連鎖下載

### 底層運算函式

- [ ] 函式載入
- [ ] 函式刪除
- [ ] 函式依賴引用的連鎖下載

### 系統式配性

- [ ] 分頁路徑規範
- [ ] 分頁環境規範
- [ ] 此專案內部路徑實作
- [ ] 此專案內部環境實作

### 硬體式配性

提醒：軟硬體式配性問題，期望以「strategy pattern」實現，在代理人函式中自動偵測、自動切換契合軟硬體。
