from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# PDFファイル名
pdf_file = "test_table.pdf"

# フォント登録
font_path = "/Library/Fonts/ipaexg.ttf"
pdfmetrics.registerFont(TTFont("IPAexGothic", font_path))

# PDFを作成
doc = SimpleDocTemplate(pdf_file, pagesize=A4)

# テストデータ
data = [
    ["ID", "名前", "年齢"],
    ["001", "山田 太郎", "30"],
    ["002", "佐藤 花子", "25"],
    ["003", "鈴木 一郎", "40"]
]

# テーブル作成
table = Table(data)

# **フォントをテーブル全体に適用**
style = TableStyle([
    ('FONTNAME', (0, 0), (-1, -1), 'IPAexGothic'),  # フォント適用（全体）
    ('FONTSIZE', (0, 0), (-1, -1), 12),  # フォントサイズ
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # すべて中央揃え
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # ヘッダー背景
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # ヘッダー文字色
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # 枠線
])

table.setStyle(style)

# PDFに追加
doc.build([table])

print(f"✅ 日本語テーブルPDF '{pdf_file}' を出力しました！")
