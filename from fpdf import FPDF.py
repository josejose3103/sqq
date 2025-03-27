from fpdf import FPDF
import pandas as pd
import psycopg2

# PostgreSQL データベース接続情報
DB_HOST = 'localhost'
DB_NAME = 'media'
DB_USER = 'tsuboisatoshino'
DB_PASSWORD = '3103kazu'

# SQLクエリ
sql_query = """
SELECT number as 番号, byoumei as 病名, kingaku as 金額, day as 日付
FROM article3
WHERE day BETWEEN '2022-01-01' AND '2022-01-28'
AND kumikanbangou = '22.0';
"""

# PDFファイル名
pdf_filename = 'article3_data_postgresql.pdf'

conn = None
try:
    # PostgreSQL データベースに接続
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)

    # SQLクエリを実行し、pandas DataFrameに読み込む
    df = pd.read_sql(sql_query, conn)

    # FPDFオブジェクトを作成
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 10)  # 日本語フォントを設定 (環境によっては変更が必要)

    # ヘッダーの出力
    for col in df.columns:
        pdf.cell(40, 10, col, border=1, align='C')
    pdf.ln()

    # データの出力
    for index, row in df.iterrows():
        for item in row:
            pdf.cell(40, 10, str(item), border=1, align='L')
        pdf.ln()

    # PDFファイルを保存
    pdf.output(pdf_filename, "F")

    print(f"PDFファイル '{pdf_filename}' が作成されました。")

except psycopg2.Error as e:
    print(f"PostgreSQL データベースエラー: {e}")

finally:
    if conn:
        conn.close()