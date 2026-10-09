# SOIL Teaching Deck (SOIL 教學投影片生成中樞)

> **基於認知負荷理論（CLT）與 SOIL 架構的 Antigravity 2 原生教學簡報建置中樞**

本專案將教材、教學大綱或教學主題，轉化為具備「教學傳達力」、「視覺留白質感」與「完全可編輯」的標準 16:9 PowerPoint（`.pptx`）教學投影片。

---

## 🌟 核心特色 (Core Features)

1. **PowerPoint 原生可編輯文字 (Editable Native Text)**：
   - 投影片內所有標題、副標題、正文與卡片皆為原生文字方塊（Text Box），教師在課堂前可直接於 Microsoft PowerPoint 或 Apple Keynote 任意修改微調，絕非一張不可編輯的圖片。
2. **SOIL 教學節奏 (Pedagogical Rhythm)**：
   - **S (Structure 結構化脈絡)**：引起動機 (Hook 20%) -> 維持注意 (Explain & Practice 60%) -> 喚起行動 (Takeaway & Action 20%)。
   - **O (Objective 單一目標)**：落實「一頁一核心概念」(One Core Point per Slide)，資訊不超載。
   - **I (Interaction 互動提問)**：精心安排生活痛點提問與迷思澄清對照（常見誤解 ❌ vs 正確理解 ✅）。
   - **L (Load 認知減負)**：嚴格落實認知負荷理論（CLT），標題 <= 10 個中文字，長篇背景說明移至演講者備忘稿（Speaker Notes）。
3. **AI 情境留白底圖 + Python 精確幾何圖形 (Hybrid Visuals)**：
   - **情境視覺**：調用 Antigravity 原生 `generate_image` 或 `antigravity-draw` 技能，提示詞鎖定負空間（Negative Space）預留文字平靜區，產出質感插圖與滿版底圖。
   - **數學/幾何圖形**：嚴禁依賴 AI 生圖產生幾何幻覺，一律以 Python（`matplotlib` / `PIL` / `svgwrite`）程式化繪製高解析度向量圖或透明 PNG 內嵌。
4. **macOS / Windows 跨平台相容排版**：
   - 預設微軟正黑體（Microsoft JhengHei）與蘋方（PingFang TC），確保字型不走樣、排版不跑版。

---

## 📂 專案架構 (Project Structure)

```
soil-teaching-deck/
├── SKILL.md                 # Antigravity 專案技能核心規格檔
├── AGENTS.md                # Antigravity 2 專案規則與安全守則
├── ANTIGRAVITY.md           # 專案快速入口導覽
├── README.md                # 專案說明文件
├── handoff.md               # 多 Agent 交接與版本演進紀錄
├── pyproject.toml           # 專案 Python 相依定義 (uv 相容)
├── references/              # SOIL 規範與技術參考庫
│   ├── soil-engines.md      # SOIL 六大引擎（概念定位、脈絡、頁面架構等）
│   ├── layout-recipes.md    # 16:9 版面網格與排版配方
│   ├── visual-assets.md     # AI 留白底圖提示詞與素材內嵌規範
│   ├── geometry.md          # 精確幾何圖形 Python 程式化生成指南
│   └── validation.md        # 簡報交付前自我檢核清單
├── scripts/                 # 自動化生成腳本
│   └── soil_deck_builder.py # 模組化 16:9 PPTX 簡報生成器
└── output/                  # 簡報輸出目錄
    └── demo_soil_deck.pptx  # 示範教學投影片產出
```

---

## 🚀 快速開始 (Quick Start)

本專案使用 `uv` 管理 Python 虛擬環境與相依套件：

```bash
# 1. 執行範例生成腳本
uv run python scripts/soil_deck_builder.py

# 2. 檢視生成的教學簡報
open output/demo_soil_deck.pptx
```

---

## 🛠️ 在 Antigravity 中使用此技能

本技能已同步部署至 Antigravity 全域技能庫：
`~/.gemini/config/skills/soil-teaching-deck`

當您對 Antigravity 說出以下關鍵字時，將會自動觸發此技能：
- 「幫我做這單元的教學簡報」
- 「把這份教材轉成 SOIL 教學投影片」
- 「請用 SOIL 架構規劃一堂課的簡報」
- 「幫我診斷這份教學簡報的認知負荷並重新設計」

---

## 📋 課綱與教學審查整合

本技能與全域 `g4-curriculum-review` 技能完全接軌，生成小學至各級教材時，遵循三階漏斗審查（課綱版本紅線、認知負荷 CLT 審查、典型迷思誘答標註），並在產出交付時附帶 AI 自我檢測審查報告。
