import psycopg2

# PostgreSQLの接続情報を設定
DB_NAME = "media"
DB_USER = "tsuboisatoshino"
DB_PASSWORD = "3103kazu"
DB_HOST = "localhost"
DB_PORT = "5432"  # PostgreSQLのデフォルトポート

# データベースに接続
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()

    # クエリを実行
    query = """
    SELECT number, byoumei, kingaku, day
    FROM article3
    WHERE day BETWEEN '2022-01-01' AND '2022-01-28'
    AND kumikanbangou = '18.0';
    """

    cursor.execute(query)

    # 結果を取得
    results = cursor.fetchall()

    # 結果を表示
    for row in results:
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    # リソースを解放
    if cursor:
        cursor.close()
    if conn:
        conn.close()
