# Visual Assets（視覺素材規範）

在教學簡報中，視覺素材的價值在於「促進理解、錨定注意力、建立情境」，而非單純裝飾。

所有非幾何圖像（插圖、背景底圖、章節過渡圖、情境圖）必須優先使用 Antigravity 原生 `generate_image` 工具或 `antigravity-draw` 技能生成。嚴禁以單純空白色塊或隨機低品質佔位圖敷衍取代。

---

## 一、視覺角色分類 (Visual Roles)

| 角色 | 應用情境 | 建議版面配置 |
|---|---|---|
| `illustration` | 概念或情境插圖 | 右側欄位（40~50% 寬度）或文字下方嵌入 |
| `background` | 封面、行動頁、章節首頁底圖 | 滿版（Full Bleed），需帶有預留之平靜留白區 |
| `hero` | 視覺震撼之主圖（如引發痛點之情境） | 佔畫面右半部或左半部（1:1 分欄） |
| `side_panel` | 側邊情境飾條（具概念意義） | 左邊界或右邊界垂直面板 |
| `section_divider` | 單元／章節過渡頁 | 滿版大圖搭配中央極簡標題與半透明微光面板 |
| `accent` | 輔助標記小圖、關鍵字意象圖 | 緊鄰對應文字或卡片右上角 |

---

## 二、Antigravity 提示詞原則 (Prompt Rules)

1. **風格一致性 (Style Token)**：從風格引擎選定統一風格標籤（例如：`modern flat educational illustration, clean lines, gentle pedagogical lighting, soft pastel palette, minimalism`）。
2. **文字淨空 (No Baked-in Text)**：在提示詞中明確要求 `textless, no words, clean negative space`，除非是特定物理圖表或符號標註，否則文字一律留待 PowerPoint 原生文字方塊處理。
3. **預留文字留白區 (Negative Space for Text)**：
   - 若為「左側文字、右側主圖」，提示詞需指定：`subject positioned on the right side, wide clean calm empty space on the left side for overlay text`。
   - 若為「右側文字、左側主圖」，提示詞需指定：`subject on the left side, wide neutral empty background on the right side`。
4. **生成品質與比例**：
   - 投影片比例請指定 `16:9`。
   - 一般草稿與卡片配圖可用標準品質，封面與單元過渡頁使用高品質生成。

---

## 三、AI 底圖 + 原生可編輯文字排版法則 (Editable Plate Rules)

當製作「AI 情境底圖 + 可編輯 PowerPoint 文字」時：

1. **底圖即為版型**：生成底圖時即應將「留白區域」視為版面設計的一環，而非生成一張塞滿細節的圖再來貼黑塊遮擋。
2. **避免大面積遮罩**：不要在整張圖片上覆蓋大片深色不透明方塊（遮蔽面積不宜超過 35%），若文字辨識度不佳，應重新生成帶有更平靜背景的圖片，或使用輕微的漸層柔光。
3. **單一文字方塊**：文字保持為獨立、乾淨的單一可編輯方塊，避免為了陰影而疊加雙層文字方塊（會增加編輯繁瑣度）。
4. **資訊過密則拆頁**：若該頁內容過多，應拆分為兩頁或改為雙欄卡片，切勿為了塞字而強行壓縮圖片。

---

## 四、檔案內嵌規範 (Final Deck Rule)

所有生成的圖片（PNG/JPG）在透過腳本建置 PPTX 時，必須直接寫入 PowerPoint 檔案結構內部（二進位內嵌），嚴禁使用外部相對路徑鏈結，以防檔案轉移後發生破圖或遺失。
