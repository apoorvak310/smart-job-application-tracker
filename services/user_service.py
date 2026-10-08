from repositories.user_repository import add_user, get_all_users
def save_user(user):
    return add_user(user)
def get_users():
    return get_all_users()