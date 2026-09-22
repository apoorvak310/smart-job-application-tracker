# add_application()
# get_all_applications()
# update_application_status()
# delete_application()

#python object -> database row
from datetime import datetime
from models.application import Application
from database.connection import get_connection
def format(date):
    if date is None:
        return None
    return date.strftime("%d-%m-%Y")

def add_application(application): #receiving object
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    insert into applications(company, role, date_applied, status, job_url, work_mode, location, salary, notes, interview_date, follow_up_date) values (?,?,?,?,?,?,?,?,?,?,?)""",(
    application.company, 
    application.role,
    format(application.date_applied),
    application.status, 
    application.job_url,
    application.work_mode,
    application.location,
    application.salary,
    application.notes,
    format(application.interview_date),
    format(application.follow_up_date)
    ))
    connection.commit()
    connection.close()
def get_all_applications():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("select * from applications")
    rows = cursor.fetchall()
    connection.close()
    return [row_to_application(row) for row in rows]
def row_to_application(row):
    application = Application(
        company=row[1],
        role=row[2],
        date_applied=datetime.strptime(row[3], "%Y-%m-%d"),
        status=row[4],
        job_url=row[5],
        work_mode=row[6],
        location=row[7],
        salary=row[8],
        notes=row[9],
        interview_date=datetime.strptime(row[10], "%Y-%m-%d") if row[10] else None,
        follow_up_date=datetime.strptime(row[11], "%Y-%m-%d") if row[11] else None
    )

    return application