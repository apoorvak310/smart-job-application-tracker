from util.validators import (
    validate_required,
    validate_date,
    validate_status,
    validate_salary,
    validate_work_mode,
    validate_job_url,
    validate_location,
    validate_notes
)
def title():
    print("-"*40)
    print(" "*6+"Smart job application system"+" "*6)
    print("-"*40)

def show_menu():
    print()
    print("1. Add Application")
    print("2. View Applications")
    print("3. Update Application Status")
    print("4. Exit")
    print("5. About\n")

applications = []
class Application:

    def __init__(self, company, role, date_applied, status="Applied",job_url=None, work_mode = None, location = None, salary = None, notes = None, interview_date = None, follow_up_date = None):
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
    def update_status(self,new_status):
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
        print("Interview Date:", self.interview_date.strftime("%d-%m-%Y") if self.interview_date else None)
        print("Follow Up Date:", self.follow_up_date.strftime("%d-%m-%Y") if self.follow_up_date else None)
        print("Date Applied:", self.date_applied.strftime("%d-%m-%Y"))
        print("-" * 40)
        
def add_application():
    company = input("Enter company name: ").strip()
    if not validate_required(company):
        print("Company cannot be empty. Please try again.")
        return
    role = input("Enter job role: ").strip()
    if not validate_required(role):
        print("Role cannot be empty. Please try again.")
        return
    date_applied = input("Enter date applied (DD-MM-YYYY): ")
    validated_date = validate_date(date_applied)
    if validated_date is False:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return
    salary = input("Enter expected salary: ").strip()
    validated_salary = validate_salary(salary)
    if validated_salary is None:
        print("Invalid salary. Please enter a positive number.")
        return
    work_mode = input("Enter the work mode: ").strip()
    work = validate_work_mode(work_mode)
    if work is None:
        print("Invalid work mode. Please try again")
        return
    job_url = input("Enter the Job URL (optional): ")
    validated_job_url = validate_job_url(job_url)
    if validated_job_url is False:
        print("Invalid URL. Please enter a valid HTTP/HTTPS URL.")
        return
    location = input("Enter job location (optional): ")
    validated_location = validate_location(location)
    interview_date = input("Enter interview date (ignore if not known, DD-MM-YYYY):").strip()
    valid_interview = validate_date(interview_date)
    if valid_interview is False:
        print("Enter a valid date ")
        return
    follow_up_date = input("Enter the follow up date (ignore if not known, DD-MM-YYYY): ").strip()
    valid_follow_up = validate_date(follow_up_date)
    if valid_follow_up is False:
        print("Enter a valid follow up date")
        return
    notes = input("Enter notes (optional)")
    validated_notes = validate_notes(notes)
    application = Application(company, role, date_applied= validated_date, interview_date=valid_interview, salary=validated_salary,work_mode= work, job_url= validated_job_url, location= validated_location, notes=validated_notes, follow_up_date=valid_follow_up)
    print("Status:", application.status)
    applications.append(application)
    
def view_applications():
    if len(applications) == 0:
        print("No applications found")
    for app in applications:
        app.display()

def update_application_status():
    cmpny = input("Enter company name: ").strip()

    if not validate_required(cmpny):
        print("Company name cannot be empty.")
        return

    for app in applications:
        if app.company.strip().lower() == cmpny.lower():
            print(f"Current status: {app.status}")

            new_status = input("Enter new status: ").strip()

            if app.update_status(new_status):
                print(f"Status updated to {app.status}")
            else:
                print("Invalid status. Please try again.")

            break
    else:
        print("Company not found.")

def show_about():
    return "Smart Job Application Tracker\nA Python CLI application for managing job applications.\n"

def main():
    title()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            update_application_status()
        elif choice == "4":
            print("Exiting the application")
            break
        elif choice == '5':
            print(show_about())
        else:
            print("Invalid Choice\nEnter between 1-5")

if __name__ == "__main__":
    main()
