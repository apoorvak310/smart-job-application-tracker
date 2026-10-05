from repositories.application_repository import (add_application, get_all_applications, update_application_status)
from util.validators import validate_status
def save_application(application):
    add_application(application)

def get_applications(): #Because the service doesn't need to expose the database-specific wording.
    return get_all_applications()

def update_status(application_id, new_status):
    validated_status = validate_status(new_status)
    if validated_status is None:
        return False
    return update_application_status(application_id, validated_status)