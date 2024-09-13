from mysql.connector import connect, Error

try:
    myconn = connect(host='localhost', user='sag', password='sagar@2003', database='sagar')
    c1 = myconn.cursor()
    c1.execute("CREATE TABLE student (std_id VARCHAR(20) PRIMARY KEY, sname VARCHAR(20))")
    print("Table 'student' created successfully.")
except Error as e:
    print(f"Error creating table: {e}")
finally:
    if myconn.is_connected():
        c1.close()
        myconn.close()
