from datetime import datetime
from urllib.parse import urlparse

VALID_STATUSES = [
    "Applied",
    "Assessment",
    "Interview",
    "HR Round",
    "Offer",
    "Rejected",
    "Withdrawn"
]

VALID_WORK_MODES = [
    "Remote",
    "Hybrid",
    "On-site"
]

def validate_required(s):
    if s.strip():
        return True
    else:
        return False

def validate_date(date_str):
    date = date_str.strip()
    if date == "":
        return None
    try:
        date = datetime.strptime(date, "%d-%m-%Y")
        return date
    except ValueError:
        return False
    
def validate_status(status):
    for s in VALID_STATUSES:
        if s.lower() == status.lower():
            return s
    else:
        return None

def validate_salary(salary_str):
    try:
        amount = float(salary_str)
        if amount > 0:
            return amount
        return None
    except ValueError:
        return None

def validate_work_mode(mode):
    for work_mode in VALID_WORK_MODES:
        if work_mode.lower() == mode.lower():
            return work_mode
    return None

def validate_job_url(job_url):
    url = job_url.strip()
    if url == "":
        return None
    parsed = urlparse(url)
    if parsed.scheme == 'http' or parsed.scheme == 'https':
        if parsed.netloc:
            return url
    return False
def validate_location(location):
    loc = location.strip()
    if loc == "":
        return None
    return loc
def validate_notes(notes):
    nts = notes.strip()
    if nts == "":
        return None
    return nts