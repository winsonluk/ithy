# Ithy — 小型混合專家研究

選擇少數專家，會如何改變混合結果？多個代理若犯同一個錯誤，多數決還可信嗎？這個專案用可直接執行的小型範例探索這些問題。

所有範例均為教學用途，只使用 Python 標準函式庫、數學函數及虛構答案，不會連線，也不需要帳號或付費模型。這裡沒有 Ithy 線上服務的實作、正式提示詞、模型配置、搜尋配置、發布系統或營運資料。

## 執行方式

需要 Python 3.10 或更新版本。

```sh
python main.py
python -m unittest discover -s tests -v
```

程式比較相同輸入在 top-1、top-2 與全部三個專家參與時的結果，列出選擇、權重、負載及專家函數的執行次數。這些次數不是實測效能提升，也不是語言模型的費用估算。

## 區分兩個概念

- **混合專家（MoE）**：模型內的子網路由閘控機制選擇。本專案以三個數學函數及固定距離閘控示範 top-k 選擇，沒有神經網路訓練或分散式運算。
- **混合代理（MoA）**：在應用層組合不同代理的答案。本專案只處理預先記錄的虛構答案，示範平手、棄權及共同錯誤，不呼叫真正的模型。

詳見[研究筆記](docs/study.md)。附錄中的[引用與點擊](research/ai-citations-search-clicks)及[爬蟲觀測](research/ai-search-observations)也只使用合成資料；它們不是匿名化的真實營運資料，不能重現任何發布者先前公布的數字。

## 原始研究

- Shazeer 等人（2017）：[Sparsely-Gated Mixture-of-Experts](https://arxiv.org/abs/1701.06538)。
- Fedus、Zoph、Shazeer（2021，2022 修訂）：[Switch Transformers](https://arxiv.org/abs/2101.03961)。
- Wang 等人（2024）：[Mixture-of-Agents](https://arxiv.org/abs/2406.04692)。

這些論文提供研究背景；本專案沒有重現其基準測試或宣稱相同成果。請只提交通用研究、合成範例或授權明確的公開資料，避免加入正式服務或客戶資料。詳見[貢獻說明](CONTRIBUTING.md)。

由 [Ithy](https://ithy.com) 維護的教學專案。採 MIT 授權，見 [LICENSE](LICENSE)。[English](README.md)。
