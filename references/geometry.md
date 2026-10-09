# Geometry & Diagrams（精確幾何與圖表規範）

在數學、自然科學或工程教學簡報中，幾何圖形、函數圖形或統計圖表必須具備「精確幾何正確性與比例尺」。

嚴禁使用 AI 生圖（Image Generation）生成幾何量角、垂直符號、平行線、圓形截角等圖形，避免產生 AI 幻覺與教學誤導。一律使用 Python 程式化（`matplotlib`、`PIL`、`svgwrite`）繪製向量圖或高解析度透明 PNG 插入簡報中。

---

## 一、幾何需求規劃規格 (Planning Fields)

在 SOIL 頁面架構規劃時，若該頁需要幾何圖形，需明確定義：

```yaml
geometry:
  id: slide_04_fig_triangle_sum
  type: triangle
  purpose: 展示三角形內角和 180 度與外角定理
  labels: [A, B, C]
  highlights:
    - angle: A
      color: primary
    - angle: B
      color: accent
  canvas:
    width: 1200
    height: 800
    dpi: 300
    transparent: true
```

---

## 二、Python 程式化生成指引 (Rendering Approach)

1. **圖形庫選擇**：
   - 數學與統計圖表、坐標系：優先使用 `matplotlib.pyplot`。
   - 純幾何向量圖（三角形、圓、輔助虛線、角度弧線）：使用 `matplotlib.patches` 或 `PIL` / `svgwrite`。
2. **視覺外觀與投影片整合**：
   - **背景透明**：`plt.savefig('output.png', transparent=True, dpi=300)`。
   - **線條粗細**：線條（`linewidth`）設定為 `2.5~4 pt`，確保在投影機上清晰可見。
   - **文字標籤**：標籤字體大小（`fontsize`）至少 `18~24 pt`，並指定相容字型（如 `PingFang TC` 或 `Arial`）。
   - **配色一致**：使用與當前簡報風格色票相同的顏色標記角度、邊長與輔助線。

---

## 三、常用幾何類型範本 (Supported Common Types)

- **三角形 (Triangles)**：銳角/直角/鈍角三角形、等腰/等邊、外心/內心/重心輔助線。
- **四邊形 (Quadrilaterals)**：平行四邊形、梯形、菱形、矩形與對角線。
- **圓與弦切角 (Circles)**：圓心、半徑、直徑、弧長、圓心角與圓周角。
- **平面直角坐標系 (Cartesian Plane)**：原點、格線、向量箭頭、函數曲線。
- **平行線與截角 (Parallel Lines & Transversals)**：同位角、內錯角、同側內角標記。
- **立體圖透視 (3D Geometry)**：長方體、圓柱體、角錐、展開圖。

---

## 四、嵌入 PPTX 流程

1. 執行 Python 繪圖腳本，輸出至專案 `assets/geometry/` 或臨時目錄。
2. 使用 `python-pptx` 的 `slide.shapes.add_picture(img_path, left, top, width, height)` 精準置入投影片指定欄位。
3. 圖形周圍搭配 PowerPoint 原生文字標註或問題引導。
