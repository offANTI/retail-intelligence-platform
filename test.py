import sqlite3

conn = sqlite3.connect("retail_intelligence.db")
cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type IN ('table','view');
""")

for row in cursor.fetchall():
    print(row[0])

conn.close()
