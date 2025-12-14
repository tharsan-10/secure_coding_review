import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username, hashed_password)
)

result = cursor.fetchone()

if result:
    print("Login successful")
else:
    print("Invalid login")
