import sqlite3

connection = sqlite3.connect("table.db")

crsr = connection.cursor()

# sql_command = """
#     CREATE TABLE emp (
#         staff_number INTEGER PRIMARY KEY,
#         fname VARCHAR(20),
#         lname VARCHAR(30),
#         gender CHAR(1),
#         joining DATE
#     );
# """
#
# cursor.execute(sql_command)

# sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
# crsr.execute(sql_command)

crsr.execute("SELECT staff_number FROM emp WHERE joining LIKE '199_-__-__' OR '200_-__-__'")
ans = crsr.fetchall()
for row in ans:
    print(row)

connection.commit()

connection.close()
