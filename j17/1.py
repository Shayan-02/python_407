import sqlite3
conn = sqlite3.connect('./mydatabase.db')
c = conn.cursor()

sql = """
create table if not exists user (
    id integer,
    name varchar(255),
    tel varchar(255),
    adress text
"""

c.execute(sql)
conn.commit()