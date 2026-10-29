from repositories.skill_repository import add_skill, get_skills_by_user
import sqlite3

def save_skill(user_id, skill_name):
    try:
        add_skill(user_id, skill_name)
    except sqlite3.IntegrityError:
        return False
    return True

def view_skills(user_id):
    return get_skills_by_user(user_id)
