import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
cur.execute("create table new(id primary key,sort,name)")
cur.execute("insert into new values(1,1,'computer')")
cur.execute("insert into new values(?,?,?)", (2, 3, 'lillt'))
cur.execute("select * from new")
print(cur.fetchall())
for row in cur.execute("select * from new"):
    print(row[0], row[1], row[2])
cur.close()
con.close()
