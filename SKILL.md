---
name: soil-teaching-deck
description: >
  建立、分析或優化 SOIL 教學架構的 PowerPoint 簡報（.pptx）。當使用者需要製作教學投影片、課堂簡報、教材轉投影片、
  SOIL 簡報、教學視覺設計，或需要針對現有教學簡報進行認知負荷（CLT）與教學節奏診斷時使用。產出具備原生可編輯文字物件、
  16:9 寬螢幕、AI 高質感底圖/插圖、精確幾何圖表及 SOIL 教學結構（引起動機 -> 維持注意 -> 喚起行動）的教學簡報。
metadata:
  short-description: SOIL 原生可編輯教學 PPTX 簡報生成中樞
---

# SOIL Teaching Deck（SOIL 教學投影片生成中樞）

本技能專門用於產出原生可編輯的教學用 PowerPoint 簡報（`.pptx`）。
核心原則：**教學傳達與清晰度第一，視覺美感與認知減負第二，檔案正確性與可編輯性為基準底線。**

---

## 🎯 產出契約 (Output Contract)

1. **格式保證**：除非使用者明確指定僅進行診斷或風格設計，否則必須產出可於 Microsoft PowerPoint / Keynote 直接編輯的標準 16:9 `.pptx` 檔案。
2. **原生文字物件**：投影片內所有文字皆必須保留為 PowerPoint 原生文字方塊（Text Box），嚴禁以純圖片取代投影片文字。
3. **視覺素材規格**：
   - 所有非幾何視覺圖像（包含封面主視覺、情境底圖、插圖、章節過渡圖、卡片配圖），優先調用 Antigravity 原生 `generate_image` 工具（指定 16:9 比例）或搭配 `antigravity-draw` 技能生成。
   - 嚴禁以本機色塊或低質佔位圖敷衍取代 AI 教學情境圖。
4. **數學與精確幾何圖形**：
   - 數學幾何（三角形、坐標系、輔助線等）嚴禁依賴 AI 生圖（避免產生幻覺與幾何誤差），應以 Python（`matplotlib` / `PIL` / `svgwrite`）程式化精確繪製向量圖/高解析 PNG 嵌入。
   - 數學公式採「雙層文字方塊」或「高解析透明公式圖 + 旁附可編輯中文說明」，確保排版穩定。
5. **圖片嵌入**：所有圖片一律直接二進位嵌入 `.pptx` 檔內，嚴禁使用相對路徑外連。
6. **最終交付**：回報最終生成的 `.pptx` 絕對路徑與投影片結構檢核表。

---

## 🧭 運作模式選擇 (Mode Selection)

依使用者需求選擇路徑：
- **完整教材轉簡報 (Material to Deck)**：依序執行 SOIL 引擎 1～6。
- **純主題發想 (Topic Only)**：先展開精簡教學大綱與對象確認，再執行 SOIL 引擎 1～6。
- **現有簡報審查 (Deck Review)**：檢視現有簡報，進行認知負荷（CLT）診斷，提出具體修訂建議或直接重構。
- **風格定義 (Style Definition)**：僅執行風格引擎（Engine 5），產出可重複使用的視覺與字級規範。

> [!TIP]
> 若使用者已提供完整教材或清晰主題，無需進行冗長訪談；僅需確認關鍵變數（授課對象年級/先備經驗、課堂時間長度），即可迅速推進產出。

---

## ⚙️ SOIL 核心工作流程 (Core Workflow)

1. **概念定位 (Concept Positioning - Engine 1)**：
   提煉「一個總概念 (One Big Idea)」、「三個子概念」、「三個常見迷思與澄清」、「帶走一句話 (Takeaway)」、「最小事實包」與「投影片 vs 講稿分配」。詳閱 `references/soil-engines.md`。
2. **脈絡節奏 (Context Positioning - Engine 2)**：
   安排經典三段式教學節奏：
   - **引起動機 (Hook)**：痛點、好奇、提問、真實生活情境。
   - **維持注意 (Explain & Practice)**：概念解析、對比、分類、視覺化演示、隨堂小試。
   - **喚起行動 (Takeaway & Action)**：決策、行動步驟、總結一句話、課後延伸。
   典型 10 頁簡報配置比例約為 **2 : 6 : 2**。
3. **頁面架構 (Page Architecture - Engine 3)**：
   定義每頁的角色、單一核心觀念、版型配方（Layout Recipe）、畫面文字、演講者備忘稿（Speaker Notes）、配圖任務或幾何需求。詳閱 `references/layout-recipes.md`。
4. **認知編修 (Cognitive Editing - Engine 4)**：
   貫徹六大認知減負法則：**降雜訊、區塊化、增資訊、結構化、順脈絡、步驟化**。
5. **風格構建 (Style Construction - Engine 5)**：
   確定色票（背景、主色、強調色、輔助色）、字型與階層比例、形狀語言、AI 底圖提示詞風格規範。
6. **產出與驗證 (Build & Verify - Engine 6)**：
   使用 Python `python-pptx` 腳本精準建置 `.pptx`。完成後執行 `references/validation.md` 之交付檢核清單。

---

## 🎨 設計與排版規範 (Design Rules)

- **畫布比例**：標準 16:9 寬螢幕（13.333 × 7.5 英吋 / 1920 × 1080）。
- **字級階層**：
  - 封面大標題：`72~84 pt`
  - 投影片頁標題：`44~56 pt`
  - 副標題 / 卡片標題：`28~34 pt`
  - 正文：`18~21 pt`
  - 註釋 / 補充說明：`14~16 pt`
  - 標籤 / Badge：`18~22 pt`
- **中文字型設定**：
  - 預設採用 macOS 與 Windows 雙向相容且易讀之中文字型：首選「Microsoft JhengHei」（微軟正黑體）、「PingFang TC」（蘋方）或「Noto Sans TC」（思源黑體）。
- **標題精準原則**：投影片標題宜精簡有力，建議不超過 10 個中文字。
- **邊距與網格**：左右留白至少 `0.6~0.7 英吋`，確保投影畫面不切邊。
- **單一焦點**：每頁必須具備明確焦點（單一強烈提問、對照卡片、流程步驟圖、或情境主視覺）。
- **色彩控制**：主色 1 種、強調色 1~2 種，避免色彩雜亂造成認知負載。

---

## 📚 參考規範 (References)

- `references/soil-engines.md`：SOIL 6 大引擎規格與產出結構。
- `references/layout-recipes.md`：頁面版型配方與 AI 底圖留白（Negative Space）排版法則。
- `references/visual-assets.md`：AI 視覺生圖提示詞策略與文字留白底圖規範。
- `references/geometry.md`：數學與幾何圖形程式化生成指南。
- `references/validation.md`：簡報交付前自我檢驗與跑版防護清單。

---

## 🍎 Antigravity 適性化原則 (Antigravity Adaptation Notes)

1. **環境相容**：
   - 運行環境為 macOS，命令列一律使用原生終端機語法（`zsh` / `bash`），非 PowerShell。
   - Python 環境支援 `python3` 及 `uv run python`，相依套件以 `python-pptx`、`matplotlib`、`pillow` 為核心。
2. **生圖與視覺能力**：
   - 充分運用 Antigravity 原生 `generate_image` 工具（支援 `16:9`、`3:2` 等比例，自動留存 Artifact），生成前務必在提示詞中規劃好文字留白區（Negative Space）。
3. **教育課綱審查連動**：
   - 與全域 `g4-curriculum-review` 技能連動，若製作國小四年級（或特定年級）教材，需檢核先備知識，遵守三階漏斗審查原則（課綱規範、CLT 認知負荷理論、迷思概念誘答）。
4. **筆記同步**：
   - 階段性成果與教學紀錄可記錄於專案 `handoff.md`，並與 Obsidian 專案駕駛艙同步。
