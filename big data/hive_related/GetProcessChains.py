import pyhdb


#host = "10.99.202.96"
#port = 30015
#user = "IT_WANGYANG37"
#passwd = "Abcd1234"

conn = pyhdb.connect(
    host="10.99.202.96",
    port=30015,
    user="IT_WANGYANG37",
    password="Abcd1234"
);

cursor = conn.cursor();
cursor.execute("SELECT SCHEMA_NAME, TABLE_NAME FROM TABLES")
cursor.fetchone();
conn.close();