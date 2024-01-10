# Bert-VITS2-Colab
簡單寫一個Colab記事本，方便來使用 Colab 訓練 [Bert-VITS2](https://github.com/fishaudio/Bert-VITS2)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ADT109119/Bert-VITS2-colab/blob/main/Bert-VITS2.ipynb)

https://colab.research.google.com/github/ADT109119/Bert-VITS2-colab/blob/main/Bert-VITS2.ipynb

![image](https://github.com/ADT109119/Bert-VITS2-Colab/assets/106337749/61951fb5-0025-46f4-9075-48584fb2141c)


## 專案用途

此專案提供一個可以簡單、易於操作的 Colab 記事本，讓大家可以輕鬆的訓練 [Bert-VITS2](https://github.com/fishaudio/Bert-VITS2)

## 目前專案功能及進度

目前支援以下幾種功能
- [x] 無須手動配置環境
- [x] 自動下載 Bert 等需要的模型
- [x] 可快速處理資料集
- [x] 支援使用 Whisper 自動標註音檔
- [x] 支援 TensorBoard 監看訓練狀況
- [x] 一鍵部屬到 HuggingFace Spaces (經測已能用，但不確定是否有Bug

## 畫面

> 操作示意 安裝函式庫>上傳資料集>訓練時監看 TensorBoard

![安裝函式庫](https://github.com/ADT109119/Bert-VITS2-Colab/assets/106337749/41b448eb-9ef8-4ec8-a783-1ae7501a35f7)
![上傳資料集](https://github.com/ADT109119/Bert-VITS2-Colab/assets/106337749/9d9d3b8f-8790-425d-b2af-bd633174b08a)
![訓練時監看 TensorBoard](https://github.com/ADT109119/Bert-VITS2-Colab/assets/106337749/590e2936-0981-411a-8326-651e2d1bbe2c)

## 音檔切割程式

本專案內有一個以srt切割音檔並生成標註的程式 `processing.py`，若要使用請依照以下的檔案命名方式 **(對應的音檔與字幕取相同的名字 僅副檔名不同)**:

```
{說話者}_{語言}_{隨編一個編號}.wav
```

以及將檔案用以下方式存放，音檔存在 `audio` 資料夾，字幕檔存放在 `srt` 資料夾，再執行 `processing.py`。便可以生成 `esd.list` 檔案，以及切分音檔(切分好的音檔放在 `raw` 資料夾中)

```
├── audio
│   ├── ****.wav
│   ├── ...
├── srt
│   ├── ****.srt
│   ├── ...
├── processing.py
```

## 專案技術

- Python
- Jupyter Notebook

## 聯絡作者

你可以透過以下方式與我聯絡

- [Email: 2.jerry32262686@gmail.com](mailto:2.jerry32262686@gmail.com)
...
