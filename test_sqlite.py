from database.schema import create_tables
from repositories.application_repository import add_application
from repositories.application_repository import get_all_applications

from main import Application
from datetime import datetime

create_tables()

application = Application(
    company="Google",
    role="Python Developer",
    date_applied=datetime(2026, 9, 22),
    status="Applied",
    salary=500000,
    work_mode="Remote",
    location="Hyderabad"
)

add_application(application)
applications = get_all_applications()
for application in applications:
    print(application)
