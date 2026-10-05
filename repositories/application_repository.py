# add_application()
# get_all_applications()
# update_application_status()
# delete_application()

#python object -> database row
from datetime import datetime
from models.application import Application
from database.connection import get_connection
def format_date(date):
    if date is None:
        return None
    return date.strftime("%Y-%m-%d")

def add_application(application): #receiving object
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    insert into applications(company, role, date_applied, status, job_url, work_mode, location, salary, notes, interview_date, follow_up_date) values (?,?,?,?,?,?,?,?,?,?,?)""",(
    application.company, 
    application.role,
    format_date(application.date_applied),
    application.status, 
    application.job_url,
    application.work_mode,
    application.location,
    application.salary,
    application.notes,
    format_date(application.interview_date),
    format_date(application.follow_up_date)
    ))
    application.id = cursor.lastrowid
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
        id=row[0],
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
def update_application_status(application_id,new_status):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE applications SET status = ? WHERE id = ?",(new_status, application_id))
    if cursor.rowcount == 0:
        connection.close()
        return False
    connection.commit()
    connection.close()
    return True
def delete_application(application_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM applications WHERE id = ?",(application_id,))
    if cursor.rowcount == 0:
        connection.close()
        return False
    connection.commit()
    connection.close()
    return True

def search_applications(search_term):
    connection = get_connection()
    cursor = connection.cursor()
    search_pattern = f"%{search_term}%"
    cursor.execute("SELECT * FROM applications WHERE company LIKE ? OR role LIKE ? OR location LIKE ? OR status LIKE ?",(search_pattern, search_pattern, search_pattern, search_pattern))
    rows = cursor.fetchall()
    connection.close()
    return [row_to_application(row) for row in rows]

results = search_applications("python")
for application in results:
    application.display()