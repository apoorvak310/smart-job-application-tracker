#what tables should exist

from database.connection import get_connection
def create_tables(): #gets us connected to the database.
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY,
        company TEXT NOT NULL,
        role TEXT NOT NULL,
        date_applied TEXT NOT NULL,
        status TEXT NOT NULL,
        job_url TEXT,
        work_mode TEXT,
        location TEXT,
        salary REAL,
        notes TEXT,
        interview_date TEXT,
        follow_up_date TEXT
        )
    """)
    connection.commit()
    connection.close()