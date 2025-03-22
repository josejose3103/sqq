import psycopg2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

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
    SELECT number, byoumei, kingaku, day
    FROM article3
    WHERE day BETWEEN '2022-01-01' AND '2022-01-28'
    AND kumikanbangou = '22.0';
    """
    cursor.execute(query)
    results = cursor.fetchall()

    # PDF作成
    pdf = canvas.Canvas(PDF_FILENAME, pagesize=A4)

    # 日本語フォントを登録

    font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"


    #font_path = "/System/Library/Fonts/Supplemental/Hiragino Sans.ttc"
    pdfmetrics.registerFont(TTFont("Arial", font_path))
    #font_path = "/System/Library/Fonts/NotoSansCJKjp-Regular.otf"  # フォントパス
    #pdfmetrics.registerFont(TTFont("Noto", font_path))
    #pdf.setFont("Noto", 12)
    # 日本語フォントを適用
    pdf.setFont("Arial", 12)
    pdf.drawString(50, 800, "クエリ結果: 日本語表示テスト")
    # ヘッダー
    pdf.drawString(50, 800, "クエリ結果")  # ← 日本語対応
    pdf.line(50, 795, 550, 795)  # 線を引く

    # データの描画
    y = 780
    for row in results:
        pdf.drawString(50, y, f"番号: {row[0]}, 病名: {row[1]}, 金額: {row[2]}, 日付: {row[3]}")
        y -= 20
        if y < 50:
            pdf.showPage()
            pdf.setFont("Hiragino", 12)
            y = 800

    # PDFを保存
    pdf.save()
    print(f"PDFが {PDF_FILENAME} に出力されました！")

except Exception as e:
    print("Error:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
