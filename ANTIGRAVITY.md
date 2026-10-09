# ANTIGRAVITY.md — SOIL Teaching Deck 入口導引

本專案為 **SOIL Teaching Deck** 於 Antigravity 2 環境下的專屬工作區與技能實踐中樞。

---

## 📌 專案與環境資訊
- **專案名稱**：SOIL Teaching Deck（可編輯教學簡報生成中樞）
- **主要工作目錄**：`/Users/tunyuan/anti/soil-teaching-deck`
- **全域技能位置**：`~/.gemini/config/skills/soil-teaching-deck`
- **Obsidian 專案駕駛艙**：`/Users/tunyuan/opencode_0715/04-專案/soil-teaching-deck-專案駕駛艙.md`

---

## 🧭 核心導航與重要檔案
1. **核心規則守則**：詳閱 [AGENTS.md](AGENTS.md)（CLT 認知負荷控制、原生可編輯文字、資安規範）。
2. **完整技能規範**：詳閱 [SKILL.md](SKILL.md)（SOIL 產出契約、六大核心引擎、16:9 規範）。
3. **版型與引擎參考庫**：
   - [references/soil-engines.md](references/soil-engines.md)：SOIL 6 大引擎規格與概念定位稿。
   - [references/layout-recipes.md](references/layout-recipes.md)：16:9 版面網格與版型配方。
   - [references/visual-assets.md](references/visual-assets.md)：AI 底圖留白提示詞與素材內嵌規範。
   - [references/geometry.md](references/geometry.md)：Python 精確幾何圖表程式化生成指南。
   - [references/validation.md](references/validation.md)：交付前自我檢驗與跑版防護清單。
4. **生成腳本與模組**：
   - [scripts/soil_deck_builder.py](scripts/soil_deck_builder.py)：Python-pptx 16:9 簡報生成器核心模組。
5. **交接紀錄**：詳閱 [handoff.md](handoff.md)。

---

## 🚀 快速啟動指令
```bash
# 執行生成示範簡報
uv run python scripts/soil_deck_builder.py

# 產出位置
ls -lh output/demo_soil_deck.pptx
```
