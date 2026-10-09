#!/usr/bin/env python3
"""
SOIL Teaching Deck Builder - Antigravity Edition
===============================================
A modular Python utility for generating beautiful, editable 16:9 educational PowerPoint decks (.pptx).
Compliant with CLT (Cognitive Load Theory) and SOIL teaching structure.
"""

import os
import sys
from typing import List, Tuple, Optional
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE


# ---------------------------------------------------------------------------
# Default Theme & Typography (macOS / Windows cross-platform compatible)
# ---------------------------------------------------------------------------
DEFAULT_FONT_TITLE = "Microsoft JhengHei"
DEFAULT_FONT_BODY = "Microsoft JhengHei"

# Color Palette (Warm Academic)
COLOR_BG_LIGHT = RGBColor(248, 249, 250)      # #F8F9FA Soft warm white
COLOR_TEXT_MAIN = RGBColor(30, 41, 59)        # #1E293B Slate 800
COLOR_TEXT_MUTED = RGBColor(100, 116, 139)    # #64748B Slate 500
COLOR_PRIMARY = RGBColor(30, 58, 138)         # #1E3A8A Royal Indigo
COLOR_ACCENT = RGBColor(234, 88, 12)          # #EA580C Bright Coral / Orange
COLOR_SUCCESS = RGBColor(16, 185, 129)        # #10B981 Emerald
COLOR_CARD_BG = RGBColor(255, 255, 255)       # Pure White
COLOR_CARD_BORDER = RGBColor(226, 232, 240)   # #E2E8F0 Light Slate


class SoilDeck:
    """Helper class to build a 16:9 SOIL teaching presentation."""

    def __init__(
        self,
        title: str = "SOIL 教學簡報",
        font_title: str = DEFAULT_FONT_TITLE,
        font_body: str = DEFAULT_FONT_BODY
    ):
        self.prs = Presentation()
        # Set 16:9 widescreen dimensions (13.333" x 7.5")
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)
        self.blank_layout = self.prs.slide_layouts[6]  # Blank slide layout
        self.font_title = font_title
        self.font_body = font_body
        self.deck_title = title

    def _set_slide_bg(self, slide, color: RGBColor = COLOR_BG_LIGHT):
        """Set solid background color for a slide using a full-bleed shape."""
        bg = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, 0, 0, self.prs.slide_width, self.prs.slide_height
        )
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def _add_speaker_notes(self, slide, notes: str):
        """Attach speaker notes for teacher's oral script."""
        if notes:
            notes_slide = slide.notes_slide
            tf = notes_slide.notes_text_frame
            tf.text = notes

    def add_cover_slide(
        self,
        title: str,
        subtitle: str,
        presenter: str = "",
        date_str: str = "",
        image_path: Optional[str] = None,
        notes: str = ""
    ):
        """
        1. 封面頁 (Cover Slide)
        Huge title, clear pedagogical subtitle, presenter, optional right hero visual.
        """
        slide = self.prs.slides.add_slide(self.blank_layout)
        self._set_slide_bg(slide, COLOR_BG_LIGHT)

        # Left Column for Text
        left = Inches(0.8)
        top = Inches(1.6)
        width = Inches(6.8) if image_path else Inches(11.7)
        height = Inches(4.5)

        tx_box = slide.shapes.add_textbox(left, top, width, height)
        tf = tx_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Title
        p_title = tf.paragraphs[0]
        p_title.text = title
        p_title.font.name = self.font_title
        p_title.font.size = Pt(64)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_PRIMARY
        p_title.space_after = Pt(20)

        # Subtitle
        p_sub = tf.add_paragraph()
        p_sub.text = subtitle
        p_sub.font.name = self.font_body
        p_sub.font.size = Pt(26)
        p_sub.font.color.rgb = COLOR_TEXT_MUTED
        p_sub.space_after = Pt(36)

        # Presenter & Date
        if presenter or date_str:
            p_meta = tf.add_paragraph()
            p_meta.text = f"{presenter}   |   {date_str}" if presenter and date_str else (presenter or date_str)
            p_meta.font.name = self.font_body
            p_meta.font.size = Pt(18)
            p_meta.font.color.rgb = COLOR_TEXT_MUTED

        # Optional Right Hero Visual
        if image_path and os.path.exists(image_path):
            img_left = Inches(7.8)
            img_top = Inches(1.2)
            img_width = Inches(4.8)
            img_height = Inches(5.1)
            slide.shapes.add_picture(image_path, img_left, img_top, img_width, img_height)

        self._add_speaker_notes(slide, notes)
        return slide

    def add_hook_question_slide(
        self,
        question: str,
        pain_point: str,
        badge_text: str = "引起動機・生活觀察",
        image_path: Optional[str] = None,
        notes: str = ""
    ):
        """
        2. 引起動機頁 (Hook Question Slide)
        Large question, real-life context / cognitive dissonance, optional visual anchor.
        """
        slide = self.prs.slides.add_slide(self.blank_layout)
        self._set_slide_bg(slide, COLOR_BG_LIGHT)

        # Badge
        tx_badge = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(4.0), Inches(0.6))
        tf_b = tx_badge.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = badge_text
        p_b.font.name = self.font_body
        p_b.font.size = Pt(16)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_ACCENT

        # Question Title
        text_width = Inches(6.8) if image_path else Inches(11.7)
        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.6), text_width, Inches(4.8))
        tf = tx_box.text_frame
        tf.word_wrap = True

        p_q = tf.paragraphs[0]
        p_q.text = question
        p_q.font.name = self.font_title
        p_q.font.size = Pt(46)
        p_q.font.bold = True
        p_q.font.color.rgb = COLOR_TEXT_MAIN
        p_q.space_after = Pt(24)

        # Pain point / Context description
        p_desc = tf.add_paragraph()
        p_desc.text = pain_point
        p_desc.font.name = self.font_body
        p_desc.font.size = Pt(22)
        p_desc.font.color.rgb = COLOR_TEXT_MUTED
        p_desc.line_spacing = 1.3

        if image_path and os.path.exists(image_path):
            slide.shapes.add_picture(image_path, Inches(7.8), Inches(1.4), Inches(4.8), Inches(4.8))

        self._add_speaker_notes(slide, notes)
        return slide

    def add_myth_buster_slide(
        self,
        title: str,
        myth_text: str,
        truth_text: str,
        explanation: str,
        notes: str = ""
    ):
        """
        3. 迷思澄清頁 (Myth Buster Slide)
        Two distinct cards: Common Misconception (Red/Grey) vs Scientific Truth (Green/Indigo).
        """
        slide = self.prs.slides.add_slide(self.blank_layout)
        self._set_slide_bg(slide, COLOR_BG_LIGHT)

        # Slide Title
        self._add_header(slide, title, "迷思澄清・破除盲點")

        # Card 1: Common Misconception
        card1_left = Inches(0.8)
        card_top = Inches(1.8)
        card_width = Inches(5.6)
        card_height = Inches(4.8)

        # Card 1 Background
        c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, card1_left, card_top, card_width, card_height)
        c1.fill.solid()
        c1.fill.fore_color.rgb = RGBColor(254, 242, 242)  # Soft red tint
        c1.line.color.rgb = RGBColor(254, 202, 202)

        tf1 = c1.text_frame
        tf1.word_wrap = True
        tf1.margin_left = tf1.margin_right = Inches(0.5)
        tf1.margin_top = Inches(0.5)

        p1_tag = tf1.paragraphs[0]
        p1_tag.text = "❌ 常見誤解"
        p1_tag.font.name = self.font_title
        p1_tag.font.size = Pt(24)
        p1_tag.font.bold = True
        p1_tag.font.color.rgb = RGBColor(220, 38, 38)
        p1_tag.space_after = Pt(16)

        p1_body = tf1.add_paragraph()
        p1_body.text = myth_text
        p1_body.font.name = self.font_body
        p1_body.font.size = Pt(20)
        p1_body.font.color.rgb = COLOR_TEXT_MAIN
        p1_body.line_spacing = 1.3

        # Card 2: Truth
        card2_left = Inches(6.9)
        c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, card2_left, card_top, card_width, card_height)
        c2.fill.solid()
        c2.fill.fore_color.rgb = RGBColor(240, 253, 244)  # Soft emerald tint
        c2.line.color.rgb = RGBColor(187, 247, 208)

        tf2 = c2.text_frame
        tf2.word_wrap = True
        tf2.margin_left = tf2.margin_right = Inches(0.5)
        tf2.margin_top = Inches(0.5)

        p2_tag = tf2.paragraphs[0]
        p2_tag.text = "✅ 正確理解"
        p2_tag.font.name = self.font_title
        p2_tag.font.size = Pt(24)
        p2_tag.font.bold = True
        p2_tag.font.color.rgb = COLOR_SUCCESS
        p2_tag.space_after = Pt(16)

        p2_body = tf2.add_paragraph()
        p2_body.text = truth_text
        p2_body.font.name = self.font_body
        p2_body.font.size = Pt(20)
        p2_body.font.bold = True
        p2_body.font.color.rgb = COLOR_TEXT_MAIN
        p2_body.space_after = Pt(16)

        p2_exp = tf2.add_paragraph()
        p2_exp.text = f"💡 原理解析：\n{explanation}"
        p2_exp.font.name = self.font_body
        p2_exp.font.size = Pt(18)
        p2_exp.font.color.rgb = COLOR_TEXT_MUTED
        p2_exp.line_spacing = 1.3

        self._add_speaker_notes(slide, notes)
        return slide

    def add_three_cards_slide(
        self,
        title: str,
        subtitle: str,
        cards: List[Tuple[str, str, str]],  # List of (badge, header, description)
        notes: str = ""
    ):
        """
        4. 三欄結構化卡片頁 (Three Cards Slide)
        Cognitive chunking: splits concept into 3 easy-to-absorb parts.
        """
        slide = self.prs.slides.add_slide(self.blank_layout)
        self._set_slide_bg(slide, COLOR_BG_LIGHT)
        self._add_header(slide, title, subtitle)

        card_width = Inches(3.64)
        card_height = Inches(4.7)
        card_top = Inches(1.8)
        spacing = Inches(0.4)

        for i, (badge, cheader, cdesc) in enumerate(cards[:3]):
            card_left = Inches(0.8) + i * (card_width + spacing)
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, card_left, card_top, card_width, card_height)
            card.fill.solid()
            card.fill.fore_color.rgb = COLOR_CARD_BG
            card.line.color.rgb = COLOR_CARD_BORDER

            tf = card.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_right = Inches(0.35)
            tf.margin_top = Inches(0.4)

            # Badge
            p_badge = tf.paragraphs[0]
            p_badge.text = badge
            p_badge.font.name = self.font_body
            p_badge.font.size = Pt(14)
            p_badge.font.bold = True
            p_badge.font.color.rgb = COLOR_PRIMARY
            p_badge.space_after = Pt(10)

            # Header
            p_head = tf.add_paragraph()
            p_head.text = cheader
            p_head.font.name = self.font_title
            p_head.font.size = Pt(22)
            p_head.font.bold = True
            p_head.font.color.rgb = COLOR_TEXT_MAIN
            p_head.space_after = Pt(14)

            # Description
            p_desc = tf.add_paragraph()
            p_desc.text = cdesc
            p_desc.font.name = self.font_body
            p_desc.font.size = Pt(16)
            p_desc.font.color.rgb = COLOR_TEXT_MUTED
            p_desc.line_spacing = 1.3

        self._add_speaker_notes(slide, notes)
        return slide

    def add_takeaway_slide(
        self,
        title: str,
        takeaway_sentence: str,
        three_points: List[str],
        action_step: str = "",
        notes: str = ""
    ):
        """
        5. 總結與外帶一句話 (Takeaway & Action Slide)
        Final synthesis: Solidifies student's long-term memory.
        """
        slide = self.prs.slides.add_slide(self.blank_layout)
        self._set_slide_bg(slide, COLOR_BG_LIGHT)
        self._add_header(slide, title, "課堂總結・觀念沉澱")

        # Big Gold / Indigo Golden Takeaway Box
        box_left = Inches(0.8)
        box_top = Inches(1.8)
        box_width = Inches(11.733)
        box_height = Inches(1.7)

        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, box_left, box_top, box_width, box_height)
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_PRIMARY
        box.line.fill.background()

        tf_box = box.text_frame
        tf_box.word_wrap = True
        tf_box.margin_left = tf_box.margin_right = Inches(0.5)
        tf_box.margin_top = Inches(0.25)

        p_pre = tf_box.paragraphs[0]
        p_pre.text = "🎯 帶走一句話 (Key Takeaway)"
        p_pre.font.name = self.font_body
        p_pre.font.size = Pt(14)
        p_pre.font.color.rgb = RGBColor(224, 231, 255)  # Light lavender
        p_pre.space_after = Pt(8)

        p_sent = tf_box.add_paragraph()
        p_sent.text = takeaway_sentence
        p_sent.font.name = self.font_title
        p_sent.font.size = Pt(26)
        p_sent.font.bold = True
        p_sent.font.color.rgb = RGBColor(255, 255, 255)

        # 3 Key Points Cards underneath
        card_y = Inches(3.8)
        card_h = Inches(2.7)
        for i, point in enumerate(three_points[:3]):
            w = Inches(3.64)
            x = Inches(0.8) + i * (w + Inches(0.4))
            c = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, card_y, w, card_h)
            c.fill.solid()
            c.fill.fore_color.rgb = COLOR_CARD_BG
            c.line.color.rgb = COLOR_CARD_BORDER

            tf_c = c.text_frame
            tf_c.word_wrap = True
            tf_c.margin_left = tf_c.margin_right = Inches(0.35)
            tf_c.margin_top = Inches(0.3)

            p_num = tf_c.paragraphs[0]
            p_num.text = f"重點 0{i+1}"
            p_num.font.name = self.font_body
            p_num.font.size = Pt(13)
            p_num.font.bold = True
            p_num.font.color.rgb = COLOR_ACCENT
            p_num.space_after = Pt(8)

            p_pt = tf_c.add_paragraph()
            p_pt.text = point
            p_pt.font.name = self.font_body
            p_pt.font.size = Pt(17)
            p_pt.font.color.rgb = COLOR_TEXT_MAIN
            p_pt.line_spacing = 1.25

        self._add_speaker_notes(slide, notes)
        return slide

    def _add_header(self, slide, title: str, subtitle: str = ""):
        """Helper to create consistent top header across slides."""
        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.733), Inches(1.0))
        tf = tx_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = self.font_title
        p.font.size = Pt(36)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_MAIN

        if subtitle:
            p_sub = tf.add_paragraph()
            p_sub.text = subtitle
            p_sub.font.name = self.font_body
            p_sub.font.size = Pt(16)
            p_sub.font.color.rgb = COLOR_TEXT_MUTED
            p_sub.space_before = Pt(4)

    def save(self, filepath: str) -> str:
        """Save presentation to file."""
        abs_path = os.path.abspath(filepath)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        self.prs.save(abs_path)
        return abs_path


if __name__ == "__main__":
    # Self-test script generating an illustrative sample deck
    output_demo = os.path.join(os.path.dirname(__file__), "..", "output", "demo_soil_deck.pptx")
    deck = SoilDeck(title="國小四年級數學：角的大小與度量")

    # 1. Cover
    deck.add_cover_slide(
        title="角的大小與度量",
        subtitle="從生活中的開合角度，發現角度的秘密",
        presenter="教學演示教師",
        date_str="2026 學年度",
        notes="【引起動機引導】：小朋友，拿出你的雙手，跟著老師一起像剪刀一樣慢慢張開..."
    )

    # 2. Hook
    deck.add_hook_question_slide(
        question="邊長越長的角，角度真的比較大嗎？",
        pain_point="很多小朋友看到長長的兩條邊，就直覺以為這個角一定比較大！真的是這樣嗎？",
        badge_text="引起動機・常見疑惑",
        notes="【引導提問】：展示兩把不同長度但開合一樣的剪刀，讓學生進行猜想並投票。"
    )

    # 3. Myth Buster
    deck.add_myth_buster_slide(
        title="辨析：邊長 vs 開合程度",
        myth_text="畫在黑板上的大三角形，角一定比畫在作業簿上的小三角形還要大！",
        truth_text="角的大小，只決定於「兩條邊張開的程度」，跟邊畫多長完全沒有關係！",
        explanation="邊只是射線，可以無限延伸。決定角度的是射線之間的夾角大小。",
        notes="【概念澄清】：用透明量角器重疊比對，直接破除學生典型視覺迷思。"
    )

    # 4. Three Cards
    deck.add_three_cards_slide(
        title="測量角度的三大關鍵步驟",
        subtitle="維持注意・量角器精準定位法",
        cards=[
            ("步驟一", "對準中心點", "把量角器的中心點，精準對齊角的頂點。"),
            ("步驟二", "重疊零度線", "讓量角器的 0 度基準線，與角的其中一條邊完全重疊。"),
            ("步驟三", "讀取另一邊", "從 0 度那端開始往內圈或外圈數，讀出另一條邊所指的刻度。")
        ],
        notes="【課堂練習】：引導全班依序喊出三口訣：『中心對頂點、零線對一邊、順著零讀度數』。"
    )

    # 5. Takeaway
    deck.add_takeaway_slide(
        title="下課前的最重要的收穫",
        takeaway_sentence="角的大小看開合，中心對齊零線合！",
        three_points=[
            "角的大小只跟兩邊張開程度有關，與邊的長度無關。",
            "量角器中心點一定要精準鎖定角的頂點。",
            "讀刻度時先看基準邊是在 0 度內圈還是外圈。"
        ],
        notes="【收束行動】：回家請每位小朋友在家中找出 3 個大於 90 度的鈍角拍照記錄。"
    )

    saved_path = deck.save(output_demo)
    print(f"✅ Demo SOIL deck successfully created at: {saved_path}")
