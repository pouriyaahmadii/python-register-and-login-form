# Import the pymysql library
import pymysql

# Define the connection string
connection_string = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "my_database",
}

# Define the login function
def login():
    username = input("نام کاربری خود را وارد کنید: ")
    password = input("رمز عبور خود را وارد کنید: ")

    with pymysql.connect(**connection_string) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM users
            WHERE username = %s AND password = %s
        """, (username, password))

        user = cursor.fetchone()

        if user:
            print("ورود با موفقیت انجام شد!")
        else:
            print("نام کاربری یا رمز عبور اشتباه است.")

# Call the login function
login()
