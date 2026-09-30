from database.schema import create_tables
from repositories.application_repository import add_application
from repositories.application_repository import get_all_applications
from repositories.application_repository import update_application_status
from repositories.application_repository import delete_application

from models.application import Application
from datetime import datetime

create_tables()

application = Application(
    company="ey",
    role="Full Stack Developer",
    date_applied=datetime(2026, 9, 30),
    status="Applied",
    salary=450000,
    work_mode="Hybrid",
    location="Delhi"
)

add_application(application)
print("New application ID: ",application.id)
applications = get_all_applications()


deleted = delete_application(1)
print("Deleted Application", deleted)
for application in applications:
    print(application.id, application.company, application.role)
