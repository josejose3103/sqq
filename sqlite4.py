import sqlite3

# SQLiteデータベースに接続（データベースファイル名を指定）
conn = sqlite3.connect("media")
cursor = conn.cursor()

# ユーザーから日付範囲と農家名を入力してもらう
#start_date = input("開始日 (YYYY/MM/DD): ")
#end_date = input("終了日 (YYYY/MM/DD): ")
#noukamei = input("農家名: ")

# SQLite は日付を 'YYYY-MM-DD' 形式で扱うため、変換が必要かも
#start_date = start_date.replace("/", "-")
#end_date = end_date.replace("/", "-")

# SQLクエリを実行
query = "SELECT * FROM article4 WHERE day BETWEEN 2024/6/1 AND 2024/6/18 AND noukamei = '坂上孝行'"
#cursor.execute(query, (start_date, end_date, noukamei))

# 結果を取得
rows = cursor.fetchall()

# 結果を表示
if rows:
    for row in rows:
        print(row)
else:
    print("該当するデータがありません。")

# 接続を閉じる
conn.close(）


