#what tables should exist

from database.connection import get_connection
def create_tables():
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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            education TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()