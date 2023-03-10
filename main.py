# /usr/bin/env python3

import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres")

cur = conn.cursor()

# write table to post gres db
cur.execute("""CREATE TABLE IF NOT EXISTS person (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT
);
""")

cur.execute("""SELECT * FROM person WHERE age < 50""")
print(cur.fetchone())

conn.commit()
cur.close()
conn.close()

def write_to_db():

    # sql, make sure to lint/update code editor
    cur.execute(""" INSERT INTO person (id, name, age) VALUES
    (1, 'guy', 30),
    (2, 'person', 94)
    """)