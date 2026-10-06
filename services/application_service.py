from repositories.application_repository import (
    add_application,
    get_all_applications, 
    update_application_status, 
    delete_application, 
    search_applications,
    filter_by_status,
    sort_applications
    )
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

def delete_application_by_id(application_id):
    return delete_application(application_id)

def search(search_term):
    return search_applications(search_term)

def filter_status(status):
    validated_status = validate_status(status)
    if validated_status is None:
        return []
    return filter_by_status(validated_status)
def sort_applications_service(sort_by,descending=False):
    return sort_applications(sort_by,descending)