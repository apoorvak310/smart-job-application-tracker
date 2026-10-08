#repository's job is database operations only
from models.user import User
from database.connection import get_connection

def add_user(user):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO users(name, email, phone, education)
    VALUES (?, ?, ?, ?)
""", (
    user.name,
    user.email,
    user.phone,
    user.education
))
    connection.commit()
    connection.close()

def get_all_users():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    connection.close()
    return rows
