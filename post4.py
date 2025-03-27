import psycopg2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate

# PostgreSQLの接続情報
DB_NAME = "media"
DB_USER = "tsuboisatoshino"
DB_PASSWORD = "3103kazu"
DB_HOST = "localhost"
DB_PORT = "5432"

# PDFファイル名
PDF_FILENAME = "output.pdf"

try:
    # データベース接続
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()

    # クエリ実行
    query = """
    SELECT number, byoumei, to_char(kingaku, '¥9,999,999'), day
    FROM article3
    WHERE day BETWEEN '2022-01-01' AND '2022-01-28'
    AND kumikanbangou = '22.0';
    """
    cursor.execute(query)
    results = cursor.fetchall()

    # PDF作成
    doc = SimpleDocTemplate(PDF_FILENAME, pagesize=A4)

    # 日本語フォントを登録
    #font_path = "/System/Library/Fonts/Supplemental/HiraginoSans-W3.ttc"  # Mac の場合
    #pdfmetrics.registerFont(TTFont("Hiragino", font_path))

    #font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
    #pdfmetrics.registerFont(TTFont("Arial", font_p    
    #pdfmetrics.registerFont(TTFont("ArialUnicode", font_path))
    #pdfmetrics.registerFont(TTFont("Arial", font_path))
    #pdf.setFont("Arial", 12)
    #pdf.drawString(50, 800, "クエリ結果: 日本語表示テスト")
    #pdf.drawString(50, 800, "クエリ結果")  # ← 日本語対応
    #pdf.line(50, 795, 550, 795)  # 線を引く
    #font_path = "/System/Library/Fonts/Supplemental/ipaexg.ttf"
    font_path = "/Library/Fonts/ipaexg.ttf"
    pdfmetrics.registerFont(TTFont("IPAexGothic", font_path))

    # ヘッダー行を追加
    headers = ["番号", "病名", "金額", "日付"]
    table_data = [headers] + results  # ヘッダー＋データを結合

    # テーブルを作成
    table = Table(table_data, colWidths=[60, 200, 100, 100])

    # スタイルを適用
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # ヘッダーの背景色
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # ヘッダーの文字色
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # すべての列を中央揃え
        ('FONTNAME', (0, 0), (-1, -1), 'IPAexGothic'),  # ヘッダーのフォント
        ('FONTSIZE', (0, 0), (-1, -1), 12),  # 文字サイズ
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),  # ヘッダーの余白
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # 表に枠線をつける
    ])

    table.setStyle(style)

    # PDFに追加
    elements = [table]
    doc.build(elements)

    print(f"✅ PDFが {PDF_FILENAME} に出力されました！")


finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
