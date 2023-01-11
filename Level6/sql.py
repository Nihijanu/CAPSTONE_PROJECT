import sqlite3
connect=sqlite3.connect("c://sqllite//hcl.db")
cur=connect.cursor()
# cur.execute("select*from filelog")
# sql="""insert into filelog values(?,?);"""
# data=(100,"c://capstone//r1.txt")
# cur.execute(sql,data)
# connect.commit()
cur.execute("select * from filelog1 where id=1")
rows=cur.fetchall()
for r in rows:
    print(r)