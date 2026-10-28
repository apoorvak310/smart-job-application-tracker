from database.connection import get_connection

def add_skill(user_id, skill_name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO skills (user_id, skill_name)
        VALUES (?, ?)
    """, (user_id, skill_name))
    connection.commit()
    connection.close()
def get_skills_by_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""select * from skills where user_id = ?""", (user_id,))
    skills = cursor.fetchall()
    connection.close()
    return skills