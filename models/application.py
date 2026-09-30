from util.validators import validate_status
class Application:

    def __init__(
        self,
        company,
        role,
        date_applied,
        status="Applied",
        job_url=None,
        work_mode=None,
        location=None,
        salary=None,
        notes=None,
        interview_date=None,
        follow_up_date=None,
        id = None
    ):
        self.company = company
        self.role = role
        self.date_applied = date_applied
        self.status = status
        self.job_url = job_url
        self.work_mode = work_mode
        self.location = location
        self.salary = salary
        self.notes = notes
        self.interview_date = interview_date
        self.follow_up_date = follow_up_date
        self.id = id

    def update_status(self, new_status):
        valid_status = validate_status(new_status)

        if valid_status is None:
            return False

        self.status = valid_status
        return True

    def display(self):
        print("-" * 40)
        print(f"Company: {self.company}")
        print(f"Role: {self.role}")
        print(f"Status: {self.status}")
        print(f"Job URL: {self.job_url}")
        print(f"Work Mode: {self.work_mode}")
        print(f"Location: {self.location}")
        print(f"Salary: {self.salary}")
        print(f"Notes: {self.notes}")
        print(
            "Interview Date:",
            self.interview_date.strftime("%Y-%m-%d")
            if self.interview_date else None
        )
        print(
            "Follow Up Date:",
            self.follow_up_date.strftime("%Y-%m-%d")
            if self.follow_up_date else None
        )
        print(
            "Date Applied:",
            self.date_applied.strftime("%Y-%m-%d")
        )
        print("-" * 40)
        