from repositories.user_repository import add_user, get_all_users, update_user, delete_user
def save_user(user):
    return add_user(user)
def get_users():
    return get_all_users()
def edit_user(user):
    return update_user(user)
def remove_user(user_id):
    return delete_user(user_id)