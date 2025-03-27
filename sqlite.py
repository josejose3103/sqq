import sqlite3

# SQLiteデータベースに接続（データベースファイル名を指定）
conn = sqlite3.connect("media")
cursor = conn.cursor()

# ユーザーから日付範囲を入力してもらう
start_date = input("開始日 (YYYY/MM/DD): ")
end_date = input("終了日 (YYYY/MM/DD): ")

# SQLクエリを実行
query = "SELECT * FROM article4 WHERE day BETWEEN ? AND ?"
cursor.execute(query, (start_date, end_date))

# 結果を取得
rows = cursor.fetchall()

# 結果を表示
for row in rows:
    print(row)

# 接続を閉じる
conn.close()
