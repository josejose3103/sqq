import psycopg2
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# PostgreSQLの接続情報
DB_NAME = "media"
DB_USER = "tsuboisatoshino"
DB_PASSWORD = "3103kazu"
DB_HOST = "localhost"
DB_PORT = "5432"

# 出力するPDFファイル名
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

    # PDFを作成
    pdf = canvas.Canvas(PDF_FILENAME, pagesize=A4)
    pdf.setFont("Helvetica", 12)

    # ヘッダー
    pdf.drawString(50, 800, "Query Results")
    pdf.line(50, 795, 550, 795)  # 線を引く

    # データの描画
    y = 780  # 初期位置
    for row in results:
        pdf.drawString(50, y, f"Number: {row[0]}, Byoumei: {row[1]}, Kingaku: {row[2]}, Day: {row[3]}")
        y -= 20
        if y < 50:  # ページの下まで行ったら新しいページへ
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
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
