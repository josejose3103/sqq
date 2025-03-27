import sqlite3

# SQLiteデータベースに接続
conn = sqlite3.connect("media")
cursor = conn.cursor()

# ユーザー入力
start_date = input("開始日 (YYYY/MM/DD): ").replace("/", "-")
end_date = input("終了日 (YYYY/MM/DD): ").replace("/", "-")
noukamei = input("農家名: ").strip()  # スペースを削除

# SQLクエリを実行 (LIKE を使用して部分一致検索)
query = "SELECT * FROM article4 WHERE day BETWEEN ? AND ? AND noukamei LIKE ?"
cursor.execute(query, (start_date, end_date, f"%{noukamei}%"))

# 結果を取得
rows = cursor.fetchall()

# 結果を表示
if rows:
    for row in rows:
        print(row)
else:
    print("該当するデータがありません。")

# 接続を閉じる
conn.close()

