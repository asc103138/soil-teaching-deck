# SOIL Teaching Deck - AGENTS.md

## 專案資訊
- **專案名稱**：SOIL Teaching Deck（SOIL 教學投影片生成中樞）
- **專案用途**：建立、診斷與生成高質感、可編輯、符合認知負荷理論（CLT）之 16:9 教學 PowerPoint 簡報（.pptx）
- **主要工作目錄**：`/Users/tunyuan/anti/soil-teaching-deck`
- **GitHub Repo**：(待本機確認後建立或關聯)
- **全域技能路徑**：`~/.gemini/config/skills/soil-teaching-deck`

## Obsidian 關聯筆記
- **Vault 路徑**：`/Users/tunyuan/opencode_0715`
- **專案駕駛艙**：`/Users/tunyuan/opencode_0715/04-專案/soil-teaching-deck-專案駕駛艙.md`

## 工作與安全規則
1. **回應語言**：一律使用繁體中文（台灣）。
2. **生命週期標準流程**：
   - **開工時**：讀取本檔、讀取 Obsidian 專案駕駛艙、檢視 Git 狀態。
   - **收工時**：更新 Obsidian 駕駛艙、檢查敏感資料與 Git diff，只提交本次相關檔案，嚴禁無差別 `git add .`。
3. **資訊安全紅線**：
   - 絕不 commit API Key、Token、密碼或個人隱私資料。
   - 學生資料僅記錄班級代號與座號，嚴禁儲存或呈現學生真名。
4. **全域教材審查規範（三階漏斗）**：
   - 凡涉及生成教學簡報、學習單或教材，必須嚴格落實三階審查：
     - **第一階（最低門檻紅線）**：符合對應年級先備經驗、108 課綱表現/內容代碼、對齊教科書版本。
     - **第二階（中階目標 CLT）**：嚴格控制認知負荷，標題 <= 10 字，工作記憶塊控制在 3~4 個內，適度留白。
     - **第三階（加分亮點）**：迷思概念誘答設計、在地化情境融入。
     - 通過自我檢測並隨附審查報告後始得交付。

## 簡報排版與技術原則
1. **畫布規範**：一律採用標準 16:9 寬螢幕（13.333" × 7.5"）。
2. **原生文字可編輯性**：投影片標題與內文一律為 PowerPoint 原生文字方塊，不可使用整頁圖片取代文字。
3. **AI 視覺素材**：
   - 非幾何圖像優先使用 Antigravity 原生 `generate_image` 或 `antigravity-draw` 產出。
   - 提示詞需預先規劃文字留白區（Negative Space），避免產生深色雜亂畫面後再蓋黑塊。
4. **幾何與數學圖形**：
   - 精確數學幾何圖形嚴禁由 AI 生成，一律以 Python（`matplotlib` / `PIL` / `svgwrite`）程式化生成高解析透明 PNG 後嵌入。
5. **備忘稿機制**：
   - 畫面維持極簡重點，教師詳細解說與口述情境一律存入演講者備忘稿（Speaker Notes）。
6. **執行環境**：
   - macOS 系統環境，命令列使用 zsh/bash。
   - 依賴管理使用 `uv run python scripts/...`，核心套件為 `python-pptx`、`matplotlib`、`pillow`。
