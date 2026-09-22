#Creating a reusable database connection or how do i connect

import sqlite3
def get_connection(): #handles the connection. when called
    connection = sqlite3.connect("data/job_tracker.db")
    return connection