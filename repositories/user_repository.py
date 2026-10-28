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
    return [row_to_user(row) for row in rows]

def row_to_user(row):
    user = User(
        id=row[0],
        name=row[1],
        email=row[2],
        phone=row[3],
        education=row[4]
    )
    return user
def update_user(user):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    update users set name = ?,email=?,phone=?,education=? where id = ?
    """,(user.name, user.email, user.phone, user.education, user.id))
    connection.commit()

def delete_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    delete from users where id=?""",(user_id,))
    cnt = cursor.rowcount
    connection.commit()
    connection.close()
    return cnt > 0