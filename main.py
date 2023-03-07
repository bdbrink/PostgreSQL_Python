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

conn.commit()
cur.close()
conn.close()