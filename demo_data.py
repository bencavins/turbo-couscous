import sqlite3


create_demo_table = """
CREATE TABLE IF NOT EXISTS demo (
	s VARCHAR(1),
	x INTEGER,
	y INTEGER
);
"""

insert_demo_data = """
INSERT INTO demo
(s, x, y)
VALUES
("g", 3, 9),
("v", 5, 7),
("f", 8, 7);
"""

row_count_query = """
SELECT COUNT(*)
FROM demo;
"""

xy_at_least_5_query = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5 AND y >= 5;
"""

unique_y_query = """
SELECT COUNT(DISTINCT y)
FROM demo;
"""

def connect_to_db(db_name='demo_data.sqlite3'):
    return sqlite3.connect(db_name)

def exectute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def execute_ddl(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)


row_count = [(3,)]
xy_at_least_5 = [(2,)]
unique_y = [(2,)]


if __name__ == '__main__':
    conn = connect_to_db()
    # execute_ddl(conn, create_demo_table)
    # execute_ddl(conn, insert_demo_data)
    # conn.commit()

    result = exectute_query(conn, unique_y_query)
    print(result)