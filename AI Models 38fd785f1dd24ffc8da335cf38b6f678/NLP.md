# NLP

[進入 NLP 世界的最佳橋樑：寫給所有人的自然語言處理與深度學習入門指南](https://leemeng.tw/shortest-path-to-the-nlp-world-a-gentle-guide-of-natural-language-processing-and-deep-learning-for-everyone.html)

> 找出這筆數據的 **baseline** ，可以讓我們判斷手上訓練出來的機器學習模型有多少潛在價值、值不值得再繼續花費自己的研究時間與電腦計算能力。

[Majority rule](https://en.wikipedia.org/wiki/Majority_rule)

## Text Segmentation 文本分詞

The Very First Thing：資料前處理，讓機器能夠處理文字

[Text segmentation](https://en.wikipedia.org/wiki/Text_segmentation)

文本分詞是一個將一連串文字切割成多個有意義的單位的步驟。

（不同NLP任務會有不同的切割需求，但很常見的是以單字為單位來切）/character/word/sentence

（中文斷詞工具：jieba）為每個詞彙附上對應的詞性-Flag。

[fxsjy/jieba](https://github.com/fxsjy/jieba)

不管最後是使用哪種切法，切完之後的每個文字片段在 NLP 領域裡頭習慣上會被稱之為 **Token**。

然後將這些詞彙轉換成一個數字序列（所謂的索引index），分別對應到特定的詞彙，就可以把句子轉成數字序列。（每個數字就是一個token）

*keras\preprocessing\text\ `Tokenizer`*

文本的集合習慣被稱為語料庫（text corpus）= 所有文本數據

## 序列的 Zero Padding

設定一個 `max_sequence_length` 來讓所有序列的長度一樣

keras函式/ `pad_sequence` 

## 把分類欄位 label 做 One-hot Encoding
